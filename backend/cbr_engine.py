import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from collections import defaultdict
import os

# Base directory for the backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, '..', 'Personalized_Diet_Recommendations.csv')

def bmi_category(v):
    if v < 18.5:   return 'UW'
    elif v < 25.0: return 'NR'
    elif v < 30.0: return 'OW'
    else:          return 'OB'

def bp_category(v):
    if v < 120:    return 'Low'
    elif v < 130:  return 'Normal'
    elif v < 140:  return 'High1'
    else:          return 'High2'

def build_index_key(disease, bmi_val, bp_val):
    d = str(disease).strip().lower().replace(' ', '_')
    return f"{d}_{bmi_category(bmi_val)}_{bp_category(bp_val)}"

class CBREngine:
    def __init__(self):
        self.df_cbr = None
        self.X_train = None
        self.y_train = None
        self.raw_train = None
        self.scaler = MinMaxScaler()
        self.le = LabelEncoder()
        self.hash_table = defaultdict(list)
        self.weight_config = {
            'disease_type': 0.30,
            'bmi': 0.20,
            'cholesterol': 0.15,
            'blood_pressure': 0.15,
            'age': 0.10,
            'glucose': 0.10,
        }
        self.numeric_feats = ['bmi', 'cholesterol', 'blood_pressure', 'age', 'glucose']
        self.disease_cols = []
        self.col_weights = {}
        self.feature_order = []
        self.w_vec = None
        self.Xtr = None
        self.ytr = None
        
        self.load_and_train()

    def load_and_train(self):
        # 1. Load & Cleaning
        df_diet = pd.read_csv(DATA_FILE)
        
        df_diet.rename(columns={
            'Patient_ID': 'patient_id',
            'Age': 'age',
            'BMI': 'bmi',
            'Chronic_Disease': 'disease_type',
            'Cholesterol_Level': 'cholesterol',
            'Blood_Sugar_Level': 'glucose',
            'Recommended_Meal_Plan': 'diet_recommendation'
        }, inplace=True)

        df_diet['blood_pressure'] = df_diet['Blood_Pressure_Systolic']
        df_diet['disease_type'] = df_diet['disease_type'].fillna('None')

        text_cols = ['disease_type', 'diet_recommendation']
        for col in text_cols:
            if col in df_diet.columns:
                df_diet[col] = df_diet[col].astype(str).str.strip().str.lower()

        df_cbr = df_diet[['patient_id', 'age', 'bmi', 'disease_type', 'cholesterol', 'glucose', 'blood_pressure', 'diet_recommendation']].copy()

        num_check = ['age', 'bmi', 'cholesterol', 'glucose', 'blood_pressure']
        for c in num_check:
            df_cbr[c] = pd.to_numeric(df_cbr[c], errors='coerce')
            df_cbr[c] = df_cbr[c].fillna(df_cbr[c].median())

        self.df_cbr = df_cbr

        # 3. Features
        X = df_cbr[['disease_type'] + self.numeric_feats].copy()
        y = df_cbr['diet_recommendation'].copy()

        X = pd.get_dummies(X, columns=['disease_type'], prefix='disease_type')
        self.disease_cols = [c for c in X.columns if c.startswith('disease_type_')]
        
        # We use all data as train for the backend since we are retrieving
        self.X_train = X.copy()
        self.y_enc = self.le.fit_transform(y)
        self.y_train = self.y_enc
        
        self.X_train[self.numeric_feats] = self.scaler.fit_transform(self.X_train[self.numeric_feats])
        self.X_train[self.disease_cols] = self.X_train[self.disease_cols].astype(float)

        # 5. Weights
        self.col_weights = {f: self.weight_config[f] for f in self.numeric_feats}
        for c in self.disease_cols:
            self.col_weights[c] = self.weight_config['disease_type'] / len(self.disease_cols)

        total = sum(self.col_weights.values())
        self.col_weights = {k: v / total for k, v in self.col_weights.items()}

        self.feature_order = self.numeric_feats + self.disease_cols
        self.w_vec = np.array([self.col_weights[f] for f in self.feature_order], dtype=float)

        self.Xtr = self.X_train[self.feature_order].to_numpy(dtype=float)
        self.ytr = np.asarray(self.y_train)

        # 6. Indexing
        self.raw_train = df_cbr[['disease_type', 'bmi', 'blood_pressure', 'patient_id', 'diet_recommendation']].copy()
        for i, row in self.raw_train.iterrows():
            key = build_index_key(row['disease_type'], row['bmi'], row['blood_pressure'])
            self.hash_table[key].append(i)

    def predict(self, new_case_dict, top_k=5):
        # Transform new case
        df_new = pd.DataFrame([new_case_dict])
        num_check = ['age', 'bmi', 'cholesterol', 'glucose', 'blood_pressure']
        for c in num_check:
            df_new[c] = pd.to_numeric(df_new[c], errors='coerce')
        df_new['disease_type'] = df_new['disease_type'].astype(str).str.strip().str.lower()

        # Build index key
        key = build_index_key(df_new.loc[0, 'disease_type'], df_new.loc[0, 'bmi'], df_new.loc[0, 'blood_pressure'])
        candidate_indices = self.hash_table.get(key, [])
        
        if not candidate_indices:
            # Fallback to all if no exact hash match
            candidate_indices = list(range(len(self.raw_train)))
            
        # One hot encode
        X_new = df_new[['disease_type'] + self.numeric_feats].copy()
        for c in self.disease_cols:
            X_new[c] = (X_new['disease_type'] == c.replace('disease_type_', '')).astype(float)
        
        # Scale
        X_new[self.numeric_feats] = self.scaler.transform(X_new[self.numeric_feats])
        xte = X_new[self.feature_order].to_numpy(dtype=float)[0]

        # Calculate distances
        X_cand = self.Xtr[candidate_indices]
        y_cand = self.ytr[candidate_indices]
        
        # Weighted Euclidean distance
        diff = X_cand - xte
        dist_sq = np.sum(self.w_vec * (diff ** 2), axis=1)
        distances = np.sqrt(dist_sq)
        
        # Similarity = 1 - distance (since scaled to 0-1)
        similarities = 1 - distances
        
        # Get top k
        top_idx_rel = np.argsort(distances)[:top_k]
        top_idx_abs = [candidate_indices[i] for i in top_idx_rel]
        top_sims = similarities[top_idx_rel]
        
        similar_cases = []
        for i, abs_idx in enumerate(top_idx_abs):
            case_data = self.raw_train.iloc[abs_idx]
            similar_cases.append({
                'id': str(case_data['patient_id']),
                'disease_type': str(case_data['disease_type']),
                'bmi': float(case_data['bmi']),
                'similarity': float(top_sims[i] * 100),
                'recommendation': str(case_data['diet_recommendation'])
            })

        # Majority vote among top K
        top_y = y_cand[top_idx_rel]
        unique, counts = np.unique(top_y, return_counts=True)
        pred_enc = unique[np.argmax(counts)]
        pred_label = str(self.le.inverse_transform([pred_enc])[0])

        return pred_label, similar_cases

engine = CBREngine()
