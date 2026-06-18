<template>
  <div class="flex min-h-screen">
    <SidebarExpert />
    <div class="flex-1 p-6 px-7 bg-bg2">
      <div class="mb-5">
        <h1 class="text-[20px] font-semibold tracking-tight">Riwayat Kasus</h1>
        <div class="text-[12px] text-tx2 mt-0.5">Daftar kasus yang telah divalidasi</div>
      </div>

      <div class="card">
        <div v-if="store.historyCases.length === 0" class="text-center text-tx3 text-[14px] py-10">
          Belum ada riwayat kasus
        </div>
        <table v-else class="w-full text-[13px] border-collapse">
          <thead>
            <tr>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                ID Kasus</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Usia / BMI</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Tekanan Darah</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Kolesterol</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Glukosa</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Kondisi Medis</th>
              <th
                class="px-3 py-3 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">
                Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="c in store.historyCases" :key="c.patient_id" class="hover:bg-bg2 transition-colors">
              <td class="px-3 py-3 border-b border-bd font-mono font-medium">{{ c.patient_id }}</td>
              <td class="px-3 py-3 border-b border-bd">{{ c.age }} thn / BMI {{ parseFloat(c.bmi).toFixed(1) }}</td>
              <td class="px-3 py-3 border-b border-bd font-mono font-medium">{{ c.blood_pressure }}</td>
              <td class="px-3 py-3 border-b border-bd font-mono font-medium">{{ c.cholesterol }}</td>
              <td class="px-3 py-3 border-b border-bd font-mono font-medium">{{ c.glucose }}</td>
              <td class="px-3 py-3 border-b border-bd capitalize">
                <span :class="['badge', c.disease_type === 'none' ? 'b-green' : 'b-red']">{{ c.disease_type }}</span>
              </td>
              <td class="px-3 py-3 border-b border-bd">
                <!-- <span class="badge b-green" v-if="c.status === 'approved'">Disetujui</span> -->
                <span class="badge b-green">Direvisi</span>
                <!-- <span class="badge b-red" v-else>Ditolak</span> -->
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
import { useNutriStore } from '@/stores/useNutriStore'
import SidebarExpert from '@/components/SidebarExpert.vue'

const store = useNutriStore()

onMounted(() => {
  store.fetchHistory()
})
</script>
