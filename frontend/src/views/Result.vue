<template>
  <div class="min-h-screen bg-bg2">
    <nav class="h-[52px] bg-bg border-b border-bd flex items-center px-6 gap-3 sticky top-0 z-40">
      <div class="text-[16px] font-semibold text-t cursor-pointer flex items-center gap-[6px]"
        @click="router.push('/')">
        <IconLeaf size="18" /> NutriPlan
      </div>
      <div class="flex-1 flex gap-1">
        <div
          class="px-[10px] py-[5px] text-[13px] text-tx2 rounded-r8 cursor-pointer font-medium hover:bg-bg2 hover:text-tx"
          @click="router.push('/input')">
          <IconArrowLeft size="14" class="inline" /> Ubah data
        </div>
      </div>
      <span v-if="isReuse" class="badge b-teal"><IconCheck size="14" /> Rekomendasi tersedia</span>
      <span v-else-if="isRevise" class="badge b-amber"><IconAlertTriangle size="14" /> Rekomendasi tersedia</span>
      <span v-else-if="result" class="badge b-red"><IconClock size="14" /> Menunggu tinjauan pakar</span>
    </nav>

    <div v-if="!result" class="p-10 text-center text-tx2">
      Belum ada data. Silakan isi form di halaman Beranda.
    </div>

    <div v-else class="max-w-[1040px] mx-auto py-6 px-5">

      <div class="grid grid-cols-2 gap-4 mb-4">
        <!-- Ringkasan data kesehatan -->
        <div class="card">
          <div class="card-t">
            <IconUser size="16" /> Ringkasan data kesehatanmu
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
            <div class="text-tx3 font-medium">Usia</div>
            <div class="text-tx">{{ patient.age }} tahun</div>
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
            <div class="text-tx3 font-medium">BMI</div>
            <div class="text-tx">{{ patient.bmi.toFixed(1) }}</div>
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
            <div class="text-tx3 font-medium">Jenis penyakit</div>
            <div class="text-tx capitalize">{{ patient.disease_type === 'none' ? 'Tidak ada' : patient.disease_type }}</div>
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
            <div class="text-tx3 font-medium">Tekanan darah</div>
            <div class="text-tx">{{ patient.blood_pressure || '—' }} mmHg</div>
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 border-b border-bd text-[12px]">
            <div class="text-tx3 font-medium">Kolesterol</div>
            <div class="text-tx">{{ patient.cholesterol || '—' }} mg/dL</div>
          </div>
          <div class="grid grid-cols-[130px_1fr] gap-1 py-1.5 text-[12px]">
            <div class="text-tx3 font-medium">Glukosa</div>
            <div class="text-tx">{{ patient.glucose || '—' }} mg/dL</div>
          </div>
        </div>

        <!-- Program diet — REUSE -->
        <div v-if="isReuse" class="card">
          <div class="card-t"><IconSparkles size="16" /> Program diet untukmu</div>
          <span class="badge b-teal mb-3"><IconCheck size="12" /> Direkomendasikan sistem</span>
          <div class="text-[22px] font-semibold tracking-tight capitalize mb-1">
            {{ humanizeLabel(result.diet_recommendation_label) }}
          </div>
          <div class="text-[12px] text-tx2 mb-4">
            Program diet ini dipilih karena profil kesehatanmu sangat mirip dengan data pasien sebelumnya yang telah ditangani.
          </div>
        </div>

        <!-- Program diet — REVISE (rule-based) -->
        <div v-else-if="isRevise" class="card">
          <div class="card-t"><IconSparkles size="16" /> Program diet untukmu</div>
          <span class="badge b-amber mb-3"><IconAlertTriangle size="12" /> Berdasarkan kondisi kesehatanmu</span>
          <div class="text-[22px] font-semibold tracking-tight capitalize mb-1">
            {{ humanizeLabel(result.diet_recommendation_label) }}
          </div>
          <div class="text-[12px] text-tx2 mb-4">
            Rekomendasi ini diberikan berdasarkan analisis kondisi kesehatan yang kamu masukkan.
          </div>
        </div>

        <!-- NEEDS_EXPERT_REVISION -->
        <div v-else class="card">
          <div class="card-t"><IconClock size="16" /> Status rekomendasi</div>
          <span class="badge b-red mb-3"><IconClock size="12" /> Menunggu tinjauan pakar</span>
          <div class="text-[22px] font-semibold tracking-tight text-[#C0392B] mb-1">
            Belum ada rekomendasi
          </div>
          <div class="text-[12px] text-tx2 mb-4">
            Kondisi kesehatanmu memerlukan perhatian khusus sehingga sistem belum dapat memberikan rekomendasi secara otomatis.
          </div>
          <div class="bg-[#FFF0F0] border border-[#FFCDD2] rounded-r8 p-3 text-[12px] text-[#B71C1C]">
            Data kamu telah dikirim ke dokter/ahli gizi untuk ditinjau.
            Rekomendasi diet yang tepat akan segera tersedia setelah ditinjau.
          </div>
        </div>
      </div>

      <div class="bg-bg border border-bd rounded-r12 p-4 flex justify-end gap-2.5">
        <button class="btn btn-out btn-sm" @click="router.push('/input')">
          <IconRefresh size="14" /> Mulai baru
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import {
  IconLeaf, IconArrowLeft, IconCheck, IconUser,
  IconSparkles, IconRefresh, IconAlertTriangle, IconClock
} from '@tabler/icons-vue'
import { humanizeLabel } from '../utils/helper'

const router = useRouter()
const store = useNutriStore()

const result = computed(() => store.recommendationResult)
const patient = computed(() => store.patientData)

const isReuse = computed(() => result.value?.status === 'REUSE')
const isRevise = computed(() => result.value?.status === 'REVISE')
</script>
