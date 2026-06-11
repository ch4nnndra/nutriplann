<template>
  <div class="min-h-screen bg-bg3">
    <NavbarPublic />
    
    <div class="flex px-6 py-4 bg-bg border-b border-bd">
      <div :class="['flex-1 flex items-center gap-2 relative', step > 1 ? 'done' : step === 1 ? 'act' : '']">
        <div class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
             :class="step >= 1 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">1</div>
        <div :class="['text-[11px] font-medium z-10 whitespace-nowrap', step > 1 ? 'text-tx2' : step === 1 ? 'text-[#085041]' : 'text-tx3']">Data pribadi</div>
      </div>
      <div :class="['flex-1 flex items-center gap-2 relative', step > 2 ? 'done' : step === 2 ? 'act' : '']">
        <div class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
             :class="step >= 2 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">2</div>
        <div :class="['text-[11px] font-medium z-10 whitespace-nowrap', step > 2 ? 'text-tx2' : step === 2 ? 'text-[#085041]' : 'text-tx3']">Kondisi medis</div>
      </div>
      <div :class="['flex-1 flex items-center gap-2 relative', step > 3 ? 'done' : step === 3 ? 'act' : '']">
        <div class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
             :class="step >= 3 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">3</div>
        <div :class="['text-[11px] font-medium z-10 whitespace-nowrap', step > 3 ? 'text-tx2' : step === 3 ? 'text-[#085041]' : 'text-tx3']">Gaya hidup</div>
      </div>
      <div :class="['flex-1 flex items-center gap-2 relative', step === 4 ? 'act' : '']">
        <div class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
             :class="step >= 4 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">4</div>
        <div :class="['text-[11px] font-medium z-10 whitespace-nowrap', step === 4 ? 'text-[#085041]' : 'text-tx3']">Nutrisi & preferensi</div>
      </div>
    </div>

    <div class="bg-bg2 min-h-[calc(100vh-100px)]">
      <div class="max-w-[680px] mx-auto py-6 px-5">
        
        <!-- Step 1 -->
        <div v-show="step === 1">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconUser size="16" /> Data pribadi
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Usia (tahun) <span class="text-[#E24B4A]">*</span></label>
                <input type="number" v-model="form.age" placeholder="Cth: 35">
              </div>
              <div class="fg">
                <label>Jenis kelamin <span class="text-[#E24B4A]">*</span></label>
                <div class="flex gap-2">
                  <div @click="form.gender = 'm'" :class="['flex-1 px-2.5 py-2 border rounded-r8 text-[12px] font-medium cursor-pointer text-center transition-all', form.gender === 'm' ? 'border-t bg-t50 text-[#085041]' : 'border-bd2 text-tx2']">Laki-laki</div>
                  <div @click="form.gender = 'f'" :class="['flex-1 px-2.5 py-2 border rounded-r8 text-[12px] font-medium cursor-pointer text-center transition-all', form.gender === 'f' ? 'border-t bg-t50 text-[#085041]' : 'border-bd2 text-tx2']">Perempuan</div>
                </div>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Tinggi badan (cm) <span class="text-[#E24B4A]">*</span></label>
                <input type="number" v-model="form.height" placeholder="Cth: 170">
              </div>
              <div class="fg">
                <label>Berat badan (kg) <span class="text-[#E24B4A]">*</span></label>
                <input type="number" v-model="form.weight" placeholder="Cth: 65">
              </div>
            </div>
            <div class="fg mb-0">
              <label>Indeks Massa Tubuh / BMI (dihitung otomatis)</label>
              <div class="bg-bg2 border border-bd rounded-r8 p-3 text-center mt-2">
                <div class="text-[28px] font-semibold leading-none">{{ bmiFormatted }}</div>
                <div class="text-[11px] font-semibold uppercase tracking-widest mt-1 text-tx2">{{ bmiCategory }}</div>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center py-4 border-t border-bd mt-2">
            <span></span>
            <button class="btn btn-t" @click="step = 2">Selanjutnya <IconArrowRight size="16" /></button>
          </div>
        </div>

        <!-- Step 2 -->
        <div v-show="step === 2">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconHeartRateMonitor size="16" /> Kondisi medis
            </div>
            <div class="fg">
              <label>Kondisi kesehatan saat ini <span class="text-[#E24B4A]">*</span></label>
              <select v-model="form.disease_type">
                <option value="none">Tidak ada kondisi khusus</option>
                <option value="diabetes">Diabetes</option>
                <option value="hypertension">Hipertensi</option>
                <option value="obesity">Obesitas</option>
              </select>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Tekanan darah sistolik (mmHg)</label>
                <input type="number" v-model="form.blood_pressure_sys" placeholder="Cth: 120">
                <div class="hint">Normal: 90–120 mmHg</div>
              </div>
              <div class="fg">
                <label>Tekanan darah diastolik (mmHg)</label>
                <input type="number" v-model="form.blood_pressure_dia" placeholder="Cth: 80">
                <div class="hint">Normal: 60–80 mmHg</div>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Kolesterol total (mg/dL)</label>
                <input type="number" v-model="form.cholesterol" placeholder="Cth: 200">
                <div class="hint">Normal: &lt;200 mg/dL</div>
              </div>
              <div class="fg">
                <label>Gula darah puasa (mg/dL)</label>
                <input type="number" v-model="form.glucose" placeholder="Cth: 100">
                <div class="hint">Normal: 70–99 mg/dL</div>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center py-4 border-t border-bd mt-2">
            <button class="btn btn-out" @click="step = 1"><IconArrowLeft size="16" /> Sebelumnya</button>
            <button class="btn btn-t" @click="step = 3">Selanjutnya <IconArrowRight size="16" /></button>
          </div>
        </div>

        <!-- Step 3 -->
        <div v-show="step === 3">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconRun size="16" /> Gaya hidup
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Konsumsi alkohol</label>
                <select><option>Tidak ada</option><option>Sesekali</option><option>Rutin</option></select>
              </div>
              <div class="fg">
                <label>Kualitas pola makan</label>
                <select><option>Kurang baik</option><option>Cukup</option><option>Baik</option></select>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center py-4 border-t border-bd mt-2">
            <button class="btn btn-out" @click="step = 2"><IconArrowLeft size="16" /> Sebelumnya</button>
            <button class="btn btn-t" @click="step = 4">Selanjutnya <IconArrowRight size="16" /></button>
          </div>
        </div>

        <!-- Step 4 -->
        <div v-show="step === 4">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconApple size="16" /> Preferensi & pantangan
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3.5">
              <div class="fg">
                <label>Jenis masakan favorit</label>
                <select><option>Masakan Indonesia</option><option>Mediterania</option><option>Barat</option></select>
              </div>
              <div class="fg">
                <label>Makanan dihindari</label>
                <select><option>Tidak ada</option><option>Manis</option><option>Asin</option></select>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center py-4 border-t border-bd mt-2">
            <button class="btn btn-out" @click="step = 3"><IconArrowLeft size="16" /> Sebelumnya</button>
            <button class="btn btn-t btn-t-lg" @click="submit" :disabled="loading">
              <span v-if="loading">Menganalisis...</span>
              <span v-else><IconSparkles size="16" /> Analisis & dapatkan program</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import NavbarPublic from '@/components/NavbarPublic.vue'
import { 
  IconUser, IconArrowRight, IconArrowLeft, IconHeartRateMonitor,
  IconRun, IconApple, IconSparkles
} from '@tabler/icons-vue'

const router = useRouter()
const store = useNutriStore()

const step = ref(1)
const loading = ref(false)

const form = ref({
  age: 45,
  gender: 'm',
  height: 170,
  weight: 80,
  disease_type: 'diabetes',
  blood_pressure_sys: 135,
  blood_pressure_dia: 85,
  cholesterol: 210,
  glucose: 130
})

const bmi = computed(() => {
  if (form.value.height && form.value.weight) {
    return form.value.weight / Math.pow(form.value.height / 100, 2)
  }
  return 0
})

const bmiFormatted = computed(() => {
  return bmi.value ? bmi.value.toFixed(1) : '—'
})

const bmiCategory = computed(() => {
  if (!bmi.value) return 'Masukkan tinggi dan berat badan'
  if (bmi.value < 18.5) return 'Kurus'
  if (bmi.value < 25) return 'Normal'
  if (bmi.value < 30) return 'Overweight'
  return 'Obesitas'
})

const submit = async () => {
  loading.value = true
  const data = {
    ...form.value,
    bmi: bmi.value
  }
  try {
    await store.submitRecommendation(data)
    router.push('/result')
  } catch(e) {
    alert("Gagal memproses data")
  } finally {
    loading.value = false
  }
}
</script>
