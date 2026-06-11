<template>
  <div class="w-[220px] bg-p shrink-0 flex flex-col min-h-screen">
    <div class="px-4 pt-[18px] pb-[14px] border-b border-white/10">
      <div class="text-[15px] font-semibold text-white flex items-center gap-1">
        <IconLeaf class="text-t100" size="18" /> NutriPlan
      </div>
      <div class="text-[10px] text-white/45 uppercase tracking-widest mt-px">Portal Pakar</div>
    </div>
    
    <div class="px-3.5 pt-3 pb-1 text-[10px] font-semibold uppercase tracking-widest text-white/35">Menu utama</div>
    
    <div :class="['flex items-center gap-2 px-3 py-[9px] mx-1.5 rounded-r8 text-[13px] cursor-pointer transition-all', $route.path === '/expert/dashboard' ? 'bg-white/20 text-white font-medium' : 'text-white/70 hover:bg-white/10 hover:text-white']" @click="router.push('/expert/dashboard')">
      <IconDashboard size="18" /> Dashboard
    </div>
    
    <div :class="['flex items-center gap-2 px-3 py-[9px] mx-1.5 rounded-r8 text-[13px] cursor-pointer transition-all', $route.path === '/expert/pending' ? 'bg-white/20 text-white font-medium' : 'text-white/70 hover:bg-white/10 hover:text-white']" @click="router.push('/expert/pending')">
      <IconClock size="18" /> Menunggu tinjauan
      <span v-if="nutriStore.pendingCases.length > 0" class="bg-am text-white text-[10px] px-1.5 py-px rounded-full ml-auto">{{ nutriStore.pendingCases.length }}</span>
    </div>
    
    <div :class="['flex items-center gap-2 px-3 py-[9px] mx-1.5 rounded-r8 text-[13px] cursor-pointer transition-all', $route.path === '/expert/history' ? 'bg-white/20 text-white font-medium' : 'text-white/70 hover:bg-white/10 hover:text-white']" @click="router.push('/expert/history')">
      <IconHistory size="18" /> Riwayat kasus
    </div>
    
    <div class="px-3.5 pt-3 pb-1 text-[10px] font-semibold uppercase tracking-widest text-white/35">Akun</div>
    <div class="flex items-center gap-2 px-3 py-[9px] mx-1.5 rounded-r8 text-[13px] text-white/70 cursor-pointer hover:bg-white/10 hover:text-white">
      <IconUserCircle size="18" /> dr. Wayan
    </div>
    
    <div class="mt-auto p-1.5 border-t border-white/10">
      <div class="flex items-center gap-2 px-3 py-[9px] rounded-r8 text-[13px] text-white/70 cursor-pointer hover:bg-white/10 hover:text-white" @click="logout">
        <IconLogout size="18" /> Keluar
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import { IconLeaf, IconDashboard, IconClock, IconHistory, IconUserCircle, IconLogout } from '@tabler/icons-vue'

const router = useRouter()
const nutriStore = useNutriStore()

const logout = () => {
  nutriStore.logoutExpert()
  router.push('/login')
}
</script>
