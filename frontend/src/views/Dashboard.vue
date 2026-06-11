<template>
  <div class="flex min-h-screen">
    <SidebarExpert />
    <div class="flex-1 p-6 px-7 bg-bg2">
      <div class="mb-5">
        <h1 class="text-[20px] font-semibold tracking-tight">Dashboard</h1>
        <div class="text-[12px] text-tx2 mt-0.5">Selamat datang, dr. Wayan Supriana</div>
      </div>

      <div class="grid grid-cols-4 gap-3 mb-5">
        <div class="card">
          <div class="w-9 h-9 rounded-r8 flex items-center justify-center text-[18px] mb-2.5 bg-am50 text-am">
            <IconClock size="20" />
          </div>
          <div class="text-[28px] font-semibold leading-none mb-1 text-am">{{ store.pendingCases.length }}</div>
          <div class="text-[11px] text-tx2 font-medium uppercase tracking-wider">Menunggu tinjauan</div>
        </div>
        <div class="card">
          <div class="w-9 h-9 rounded-r8 flex items-center justify-center text-[18px] mb-2.5 bg-t50 text-t">
            <IconCheck size="20" />
          </div>
          <div class="text-[28px] font-semibold leading-none mb-1 text-t">{{ store.historyCases.length }}</div>
          <div class="text-[11px] text-tx2 font-medium uppercase tracking-wider">Tervalidasi</div>
        </div>
        <div class="card">
          <div class="w-9 h-9 rounded-r8 flex items-center justify-center text-[18px] mb-2.5 bg-p50 text-p">
            <IconDatabase size="20" />
          </div>
          <div class="text-[28px] font-semibold leading-none mb-1 text-p">1.137</div>
          <div class="text-[11px] text-tx2 font-medium uppercase tracking-wider">Data referensi</div>
        </div>
        <div class="card">
          <div class="w-9 h-9 rounded-r8 flex items-center justify-center text-[18px] mb-2.5 bg-[#E6F1FB] text-[#185FA5]">
            <IconStopwatch size="20" />
          </div>
          <div class="text-[28px] font-semibold leading-none mb-1 text-[#185FA5]">4.2</div>
          <div class="text-[11px] text-tx2 font-medium uppercase tracking-wider">Menit/tinjauan</div>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div class="card">
          <div class="card-t"><IconChartBar size="16" /> Distribusi program diet</div>
          <div class="mb-2.5">
            <div class="text-[12px] font-medium text-tx2 mb-1 flex justify-between"><span>Diet Seimbang</span><span>42%</span></div>
            <div class="h-[7px] bg-bg3 rounded-full overflow-hidden"><div class="h-full bg-p400" style="width: 42%"></div></div>
          </div>
          <div class="mb-2.5">
            <div class="text-[12px] font-medium text-tx2 mb-1 flex justify-between"><span>Diet Rendah Sodium</span><span>32%</span></div>
            <div class="h-[7px] bg-bg3 rounded-full overflow-hidden"><div class="h-full bg-p400" style="width: 32%"></div></div>
          </div>
          <div class="mb-2.5">
            <div class="text-[12px] font-medium text-tx2 mb-1 flex justify-between"><span>Diet Rendah Karbohidrat</span><span>26%</span></div>
            <div class="h-[7px] bg-bg3 rounded-full overflow-hidden"><div class="h-full bg-p400" style="width: 26%"></div></div>
          </div>
        </div>

        <div class="card">
          <div class="card-t justify-between">
            <span><IconClock size="16" class="inline" /> Kasus terbaru menunggu tinjauan</span>
            <button class="btn btn-sm btn-out-p" @click="router.push('/expert/pending')">Lihat semua</button>
          </div>
          <div v-if="store.pendingCases.length === 0" class="text-center text-tx3 text-[12px] py-4">
            Tidak ada kasus pending
          </div>
          <table v-else class="w-full text-[13px] border-collapse">
            <thead>
              <tr>
                <th class="px-2 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">ID</th>
                <th class="px-2 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Kondisi</th>
                <th class="px-2 py-2 text-left text-[11px] font-medium text-tx2 bg-bg2 border-b border-bd uppercase tracking-wider">Aksi</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in store.pendingCases.slice(0, 5)" :key="c.case_id" class="hover:bg-bg2">
                <td class="px-2 py-2 border-b border-bd font-mono text-[11px]">{{ c.case_id }}</td>
                <td class="px-2 py-2 border-b border-bd capitalize"><span class="badge b-red">{{ c.patient_data.disease_type }}</span></td>
                <td class="px-2 py-2 border-b border-bd"><button class="btn btn-sm btn-p" @click="router.push(`/expert/detail/${c.case_id}`)">Tinjau</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import SidebarExpert from '@/components/SidebarExpert.vue'
import { 
  IconClock, IconCheck, IconDatabase, IconStopwatch, IconChartBar
} from '@tabler/icons-vue'

const router = useRouter()
const store = useNutriStore()

onMounted(() => {
  store.fetchPending()
  store.fetchHistory()
})
</script>
