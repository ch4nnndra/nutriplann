<template>
  <div class="flex min-h-screen">
    <SidebarExpert />
    <div class="flex-1 p-6 px-7 bg-bg2">
      <div class="mb-5">
        <h1 class="text-[20px] font-semibold tracking-tight">Menunggu Tinjauan</h1>
        <div class="text-[12px] text-tx2 mt-0.5">Daftar kasus yang perlu divalidasi</div>
      </div>

      <div class="card">
        <div v-if="store.pendingCases.length === 0" class="text-center text-tx3 text-[14px] py-10">
          Tidak ada kasus pending
        </div>
        <table v-else class="w-full text-[13px] border-collapse">
          <thead>
            <tr>
              <th class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">ID Kasus</th>
              <th class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Usia / BMI</th>
              <th class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Kondisi Medis</th>
              <th class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Rekomendasi CBR</th>
              <th class="px-3 py-3 text-right text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="c in store.pendingCases" :key="c.case_id" class="hover:bg-bg2 transition-colors">
              <td class="px-3 py-3 border-b border-bd font-mono font-medium">{{ c.case_id }}</td>
              <td class="px-3 py-3 border-b border-bd">{{ c.patient_data.age }} thn / BMI {{ c.patient_data.bmi.toFixed(1) }}</td>
              <td class="px-3 py-3 border-b border-bd capitalize">
                <span :class="['badge', c.patient_data.disease_type === 'none' ? 'b-green' : 'b-red']">{{ c.patient_data.disease_type }}</span>
              </td>
              <td class="px-3 py-3 border-b border-bd capitalize font-medium">{{ c.recommendation.replaceAll('_', ' ') }}</td>
              <td class="px-3 py-3 border-b border-bd text-right">
                <button class="btn btn-sm btn-p" @click="router.push(`/expert/detail/${c.case_id}`)">Tinjau Detail</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import SidebarExpert from '@/components/SidebarExpert.vue'

const router = useRouter()
const store = useNutriStore()

onMounted(() => {
  store.fetchPending()
})
</script>
