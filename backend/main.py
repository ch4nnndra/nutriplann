from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from typing import List, Optional
from cbr_engine import engine

app = FastAPI(title="NutriPlan API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "CBR Diet Recommendation API"
ALGORITHM = "HS256"

# Pydantic Models
class PatientData(BaseModel):
    age: int
    bmi: float
    disease_type: str
    blood_pressure_sys: float = None
    cholesterol: float = None
    glucose: float = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    blood_pressure_dia: Optional[float] = None

class LoginData(BaseModel):
    username: str
    password: str

class ValidateRequest(BaseModel):
    case_id: str
    status: str

# Mock Database for pending cases
pending_cases = []
history_cases = []

@app.post("/api/recommend")
async def recommend_diet(data: PatientData):
    # Convert input to dictionary for the engine
    # We use systolic pressure as representative for simplicity or average
    bp = data.blood_pressure_sys if data.blood_pressure_sys else 120
    
    case_dict = {
        'disease_type': data.disease_type,
        'bmi': data.bmi,
        'age': data.age,
        'cholesterol': data.cholesterol if data.cholesterol else 200,
        'glucose': data.glucose if data.glucose else 100,
        'blood_pressure': bp
    }
    
    pred_label, similar_cases = engine.predict(case_dict)
    
    case_id = f"CASE-{datetime.now().year}-{len(pending_cases) + len(history_cases) + 1:04d}"
    
    result = {
        "case_id": case_id,
        "recommendation": pred_label,
        "similar_cases": similar_cases,
        "patient_data": data.dict()
    }
    
    pending_cases.append(result)
    
    return result

@app.post("/api/auth/login")
async def login(data: LoginData):
    if data.username == "pakar@example.com" and data.password == "12345678":
        token = jwt.encode(
            {"sub": data.username, "exp": datetime.utcnow() + timedelta(hours=24)},
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Very basic auth dependency
async def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/api/expert/pending")
async def get_pending():
    return pending_cases

@app.get("/api/expert/history")
async def get_history():
    return history_cases

@app.post("/api/expert/validate")
async def validate_case(req: ValidateRequest):
    global pending_cases, history_cases
    case = next((c for c in pending_cases if c["case_id"] == req.case_id), None)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    
    case["status"] = req.status
    pending_cases = [c for c in pending_cases if c["case_id"] != req.case_id]
    history_cases.append(case)
    return {"message": "Success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
