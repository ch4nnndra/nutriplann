<template>
  <div class="flex min-h-screen">
    <SidebarExpert />
    <div class="flex-1 p-6 px-7 bg-bg2">
      <div class="mb-5 flex items-center justify-between">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <button class="btn btn-out btn-sm" @click="router.push('/expert/pending')"><IconArrowLeft size="14" /></button>
            <h1 class="text-[20px] font-semibold tracking-tight">Tinjauan Kasus {{ caseId }}</h1>
          </div>
        </div>
      </div>

      <div v-if="!caseData" class="text-center py-10 text-tx3">
        Data tidak ditemukan.
      </div>

      <div v-else class="grid grid-cols-2 gap-4">
        <div>
          <div class="card mb-4">
            <div class="card-t"><IconUser size="16" /> Data Pasien</div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
              <div class="text-tx3 font-medium">Usia</div><div class="text-tx">{{ caseData.patient_data.age }} tahun</div>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
              <div class="text-tx3 font-medium">BMI</div><div class="text-tx">{{ caseData.patient_data.bmi.toFixed(1) }}</div>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
              <div class="text-tx3 font-medium">Kondisi</div><div class="text-tx capitalize">{{ caseData.patient_data.disease_type }}</div>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
              <div class="text-tx3 font-medium">Tekanan darah</div><div class="text-tx">{{ caseData.patient_data.blood_pressure_sys }}/{{ caseData.patient_data.blood_pressure_dia }} mmHg</div>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
              <div class="text-tx3 font-medium">Kolesterol</div><div class="text-tx">{{ caseData.patient_data.cholesterol }} mg/dL</div>
            </div>
            <div class="grid grid-cols-[110px_1fr] gap-1 py-1.5 text-[12px]">
              <div class="text-tx3 font-medium">Gula darah</div><div class="text-tx">{{ caseData.patient_data.glucose }} mg/dL</div>
            </div>
          </div>
        </div>

        <div>
          <div class="card mb-4">
            <div class="card-t"><IconSparkles size="16" /> Rekomendasi Sistem (CBR)</div>
            <div class="text-[18px] font-semibold text-t mb-2 capitalize">{{ caseData.recommendation.replaceAll('_', ' ') }}</div>
            
            <div class="mt-4 border-t border-bd pt-4">
              <div class="card-t"><IconCheck size="16" /> Keputusan Pakar</div>
              <div class="flex gap-2 mb-4">
                <button class="btn btn-t flex-1 justify-center" @click="handleValidate('approved')">Setujui</button>
                <button class="btn btn-out flex-1 justify-center" @click="handleValidate('revised')">Revisi</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import SidebarExpert from '@/components/SidebarExpert.vue'
import { IconUser, IconSparkles, IconCheck, IconArrowLeft } from '@tabler/icons-vue'

const router = useRouter()
const route = useRoute()
const store = useNutriStore()

onMounted(() => {
  if (store.pendingCases.length === 0) store.fetchPending()
})

const caseId = route.params.id

const caseData = computed(() => {
  return store.pendingCases.find(c => c.case_id === caseId)
})

const handleValidate = async (status) => {
  const ok = await store.validateCase(caseId, status)
  if (ok) {
    router.push('/expert/pending')
  } else {
    alert("Gagal memvalidasi")
  }
}
</script>
