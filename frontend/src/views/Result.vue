<template>
  <div class="min-h-screen bg-bg2">
    <nav class="h-[52px] bg-bg border-b border-bd flex items-center px-6 gap-3 sticky top-0 z-40">
      <div class="text-[16px] font-semibold text-t cursor-pointer flex items-center gap-[6px]" @click="router.push('/')">
        <IconLeaf size="18" /> NutriPlan
      </div>
      <div class="flex-1 flex gap-1">
        <div class="px-[10px] py-[5px] text-[13px] text-tx2 rounded-r8 cursor-pointer font-medium hover:bg-bg2 hover:text-tx" @click="router.push('/input')">
          <IconArrowLeft size="14" class="inline" /> Ubah data
        </div>
      </div>
      <span class="badge b-teal"><IconCheck size="14" /> Rekomendasi tersedia</span>
    </nav>

    <div v-if="!result" class="p-10 text-center text-tx2">
      Belum ada data. Silakan isi form di halaman Beranda.
    </div>

    <div v-else class="max-w-[1040px] mx-auto py-6 px-5">

      <div class="grid grid-cols-2 gap-4 mb-4">
        <!-- Ringkasan data kesehatan -->
        <div class="card">
          <div class="card-t"><IconUser size="16" /> Ringkasan data kesehatanmu</div>
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
            <div class="text-tx">{{ patient.blood_pressure_sys || '—' }} mmHg</div>
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

        <!-- Program diet -->
        <div class="card">
          <div class="card-t"><IconSparkles size="16" /> Program diet untukmu</div>
          <span class="badge b-teal mb-3"><IconCheck size="12" /> Direkomendasikan sistem</span>
          <div class="text-[22px] font-semibold tracking-tight capitalize mb-1">
            {{ result.recommendation.replaceAll('_', ' ') }}
          </div>
          <div class="text-[12px] text-tx2 mb-4">
            Berdasarkan analisis kemiripan profil kondisimu dengan {{ result.similar_cases.length }} data klinis referensi.
          </div>
          <div class="sep"></div>
          <div class="card-t"><IconChartPie size="16" /> Estimasi target nutrisi harian</div>
          <div class="grid grid-cols-4 gap-2">
            <div class="bg-bg2 rounded-r8 p-2 text-center">
              <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Kalori</div>
              <div class="text-[18px] font-semibold leading-none text-am">1.800</div>
              <div class="text-[9px] text-tx3">kkal</div>
            </div>
            <div class="bg-bg2 rounded-r8 p-2 text-center">
              <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Protein</div>
              <div class="text-[18px] font-semibold leading-none text-t">90</div>
              <div class="text-[9px] text-tx3">gram</div>
            </div>
            <div class="bg-bg2 rounded-r8 p-2 text-center">
              <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Karbo</div>
              <div class="text-[18px] font-semibold leading-none text-p400">150</div>
              <div class="text-[9px] text-tx3">gram</div>
            </div>
            <div class="bg-bg2 rounded-r8 p-2 text-center">
              <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Lemak</div>
              <div class="text-[18px] font-semibold leading-none text-[#185FA5]">60</div>
              <div class="text-[9px] text-tx3">gram</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Kasus serupa -->
      <div class="card mb-3">
        <div class="card-t"><IconUsers size="16" /> Kasus serupa dari data referensi (CBR)</div>
        <table class="w-full text-[13px] border-collapse">
          <thead>
            <tr>
              <th class="px-3 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">#</th>
              <th class="px-3 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Kondisi</th>
              <th class="px-3 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">BMI</th>
              <th class="px-3 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Kemiripan</th>
              <th class="px-3 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Rekomendasi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sim, index) in result.similar_cases" :key="index" class="hover:bg-bg2">
              <td class="px-3 py-2 border-b border-bd">{{ index + 1 }}</td>
              <td class="px-3 py-2 border-b border-bd capitalize">{{ sim.disease_type }}</td>
              <td class="px-3 py-2 border-b border-bd">{{ sim.bmi.toFixed(1) }}</td>
              <td class="px-3 py-2 border-b border-bd">
                <div class="flex items-center gap-2">
                  <div class="flex-1 h-[5px] bg-bg3 rounded-full overflow-hidden">
                    <div class="h-full bg-t rounded-full" :style="{ width: sim.similarity + '%' }"></div>
                  </div>
                  <div class="text-[11px] font-medium text-[#085041] min-w-[32px] text-right">{{ sim.similarity.toFixed(1) }}%</div>
                </div>
              </td>
              <td class="px-3 py-2 border-b border-bd capitalize">{{ sim.recommendation.replaceAll('_', ' ') }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="bg-bg border border-bd rounded-r12 p-4 flex justify-end gap-2.5">
        <button class="btn btn-out btn-sm" @click="router.push('/input')"><IconRefresh size="14" /> Mulai baru</button>
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
  IconSparkles, IconChartPie, IconUsers, IconRefresh
} from '@tabler/icons-vue'

const router = useRouter()
const store = useNutriStore()

const result = computed(() => store.recommendationResult)
const patient = computed(() => store.patientData)
</script>
