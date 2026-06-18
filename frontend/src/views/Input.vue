<template>
  <div class="min-h-screen bg-bg3">
    <NavbarPublic />

    <!-- Step indicator -->
    <div class="flex px-6 py-4 bg-bg border-b border-bd">
      <div :class="['flex-1 flex items-center gap-2 relative', step > 1 ? 'done' : step === 1 ? 'act' : '']">
        <div
          class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
          :class="step >= 1 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">1</div>
        <div
          :class="['text-[11px] font-medium z-10 whitespace-nowrap', step > 1 ? 'text-tx2' : step === 1 ? 'text-[#085041]' : 'text-tx3']">
          Data fisik</div>
      </div>
      <div :class="['flex-1 flex items-center gap-2 relative', step === 2 ? 'act' : '']">
        <div
          class="w-[26px] h-[26px] rounded-full text-[11px] font-semibold flex items-center justify-center z-10 transition-all"
          :class="step >= 2 ? 'bg-t text-white' : 'bg-bg3 text-tx3'">2</div>
        <div :class="['text-[11px] font-medium z-10 whitespace-nowrap', step === 2 ? 'text-[#085041]' : 'text-tx3']">
          Data medis</div>
      </div>
    </div>

    <div class="bg-bg2 min-h-[calc(100vh-100px)]">
      <div class="max-w-[680px] mx-auto py-6 px-5">

        <!-- Step 1: Data Fisik -->
        <div v-show="step === 1">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div
              class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconUser size="16" /> Data fisik
            </div>

            <div class="fg">
              <label>Usia (tahun) <span class="text-[#E24B4A]">*</span></label>
              <input type="number" v-model.number="form.age" placeholder="Cth: 35" min="1" max="120">
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div class="fg">
                <label>Tinggi badan (cm) <span class="text-[#E24B4A]">*</span></label>
                <input type="number" v-model.number="form.height" placeholder="Cth: 170" min="50" max="250">
              </div>
              <div class="fg">
                <label>Berat badan (kg) <span class="text-[#E24B4A]">*</span></label>
                <input type="number" v-model.number="form.weight" placeholder="Cth: 65" min="10" max="300">
              </div>
            </div>

            <!-- BMI Result -->
            <div class="fg mb-0">
              <label>Indeks Massa Tubuh (BMI) — dihitung otomatis</label>
              <div class="bg-bg2 border border-bd rounded-r8 p-4 mt-1 flex items-center gap-4">
                <div class="text-center">
                  <div class="text-[32px] font-semibold leading-none" :class="bmiColor">{{ bmiFormatted }}</div>
                  <div class="text-[10px] text-tx3 mt-1">kg/m²</div>
                </div>
                <div class="flex-1">
                  <div class="text-[13px] font-semibold" :class="bmiColor">{{ bmiCategory }}</div>
                  <div class="text-[11px] text-tx3 mt-0.5">{{ bmiDesc }}</div>
                  <div class="h-[6px] bg-bg3 rounded-full mt-2 overflow-hidden">
                    <div class="h-full rounded-full transition-all" :class="bmiColor.replace('text-', 'bg-')"
                      :style="{ width: Math.min((bmi / 40) * 100, 100) + '%' }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="flex justify-end py-4 border-t border-bd mt-2">
            <button class="btn btn-t" @click="goStep2" :disabled="!canStep2">
              Selanjutnya
              <IconArrowRight size="16" />
            </button>
          </div>
        </div>

        <!-- Step 2: Data Medis -->
        <div v-show="step === 2">
          <div class="bg-bg border border-bd rounded-r12 p-5 mb-3">
            <div
              class="text-[12px] font-semibold uppercase tracking-widest text-t mb-3.5 flex items-center gap-1.5 border-b border-t50 pb-2">
              <IconHeartRateMonitor size="16" /> Data medis
            </div>

            <div class="fg">
              <label>Jenis penyakit / kondisi kesehatan <span class="text-[#E24B4A]">*</span></label>
              <select v-model="form.disease_type">
                <option value="none">Tidak ada kondisi khusus</option>
                <option value="diabetes">Diabetes</option>
                <option value="hypertension">Hipertensi</option>
                <option value="obesity">Obesitas</option>
              </select>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div class="fg">
                <label>Tekanan darah sistolik (mmHg)</label>
                <input type="number" v-model.number="form.blood_pressure_sys" placeholder="Cth: 120" min="60" max="250">
                <div class="hint">Normal: 90–120 mmHg</div>
              </div>
              <div class="fg">
                <label>Kolesterol total (mg/dL)</label>
                <input type="number" v-model.number="form.cholesterol" placeholder="Cth: 200" min="50" max="600">
                <div class="hint">Normal: &lt;200 mg/dL</div>
              </div>
            </div>

            <div class="fg mb-0">
              <label>Glukosa / gula darah puasa (mg/dL)</label>
              <input type="number" v-model.number="form.glucose" placeholder="Cth: 100" min="20" max="600">
              <div class="hint">Normal: 70–99 mg/dL</div>
            </div>
          </div>

          <!-- Ringkasan BMI -->
          <div class="bg-bg border border-bd rounded-r12 p-4 mb-3 flex items-center gap-3">
            <div class="w-9 h-9 rounded-r8 bg-t50 flex items-center justify-center text-t shrink-0">
              <IconUser size="18" />
            </div>
            <div class="flex-1 text-[12px]">
              <span class="text-tx2">Usia:</span> <strong>{{ form.age }} tahun</strong>
              <span class="mx-2 text-bd2">|</span>
              <span class="text-tx2">BMI:</span> <strong :class="bmiColor">{{ bmiFormatted }}</strong>
              <span class="text-tx3 ml-1">({{ bmiCategory }})</span>
            </div>
            <button class="btn btn-out btn-sm" @click="step = 1">
              <IconArrowLeft size="13" /> Edit
            </button>
          </div>

          <div class="flex justify-between py-4 border-t border-bd mt-2">
            <button class="btn btn-out" @click="step = 1">
              <IconArrowLeft size="16" /> Sebelumnya
            </button>
            <button class="btn btn-t btn-t-lg" @click="submit" :disabled="loading">
              <span v-if="loading">Menganalisis...</span>
              <span v-else class="inline-flex items-center gap-2">
                <IconSparkles size="16" /> Analisis & dapatkan program
              </span>
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
  IconUser, IconArrowRight, IconArrowLeft,
  IconHeartRateMonitor, IconSparkles
} from '@tabler/icons-vue'

const router = useRouter()
const store = useNutriStore()

const step = ref(1)
const loading = ref(false)

const form = ref({
  age: null,
  height: null,
  weight: null,
  disease_type: 'none',
  blood_pressure_sys: null,
  cholesterol: null,
  glucose: null,
})

const bmi = computed(() => {
  if (form.value.height && form.value.weight && form.value.height > 0) {
    return form.value.weight / Math.pow(form.value.height / 100, 2)
  }
  return 0
})

const bmiFormatted = computed(() => bmi.value ? bmi.value.toFixed(1) : '—')

const bmiCategory = computed(() => {
  if (!bmi.value) return 'Masukkan tinggi & berat badan'
  if (bmi.value < 18.5) return 'Berat Badan Kurang'
  if (bmi.value < 25) return 'Normal'
  if (bmi.value < 30) return 'Kelebihan Berat Badan'
  return 'Obesitas'
})

const bmiDesc = computed(() => {
  if (!bmi.value) return ''
  if (bmi.value < 18.5) return 'Di bawah rentang berat badan ideal'
  if (bmi.value < 25) return 'Dalam rentang berat badan ideal'
  if (bmi.value < 30) return 'Sedikit di atas berat badan ideal'
  return 'Jauh di atas berat badan ideal'
})

const bmiColor = computed(() => {
  if (!bmi.value) return 'text-tx3'
  if (bmi.value < 18.5) return 'text-[#185FA5]'
  if (bmi.value < 25) return 'text-t'
  if (bmi.value < 30) return 'text-am'
  return 'text-[#C0392B]'
})

const canStep2 = computed(() => form.value.age && form.value.height && form.value.weight && bmi.value > 0)

const goStep2 = () => {
  if (canStep2.value) step.value = 2
}

const submit = async () => {
  loading.value = true
  const data = {
    age: form.value.age,
    bmi: parseFloat(bmi.value.toFixed(2)),
    disease_type: form.value.disease_type,
    blood_pressure: form.value.blood_pressure_sys || 120,
    cholesterol: form.value.cholesterol || 200,
    glucose: form.value.glucose || 100
  }
  console.log(data)
  try {
    await store.submitRecommendation(data)
    router.push('/result')
  } catch (e) {
    alert('Gagal memproses data. Pastikan backend berjalan.')
  } finally {
    loading.value = false
  }
}
</script>
