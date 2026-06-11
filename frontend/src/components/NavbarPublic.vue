<template>
  <nav class="h-[52px] bg-bg border-b border-bd flex items-center px-6 gap-3 sticky top-0 z-40">
    <div class="text-[16px] font-semibold text-t cursor-pointer flex items-center gap-[6px]" @click="router.push('/')">
      <IconLeaf size="18" /> NutriPlan
    </div>
    <div class="flex-1 flex gap-1">
      <div class="px-[10px] py-[5px] text-[13px] text-tx2 rounded-r8 cursor-pointer font-medium hover:bg-bg2 hover:text-tx" @click="router.push('/')">Beranda</div>
      <div class="px-[10px] py-[5px] text-[13px] text-tx2 rounded-r8 cursor-pointer font-medium hover:bg-bg2 hover:text-tx">Cara kerja</div>
      <div class="px-[10px] py-[5px] text-[13px] text-tx2 rounded-r8 cursor-pointer font-medium hover:bg-bg2 hover:text-tx">Tentang</div>
    </div>
    <div class="flex gap-2">
      <button class="btn btn-out btn-sm" @click="router.push('/login')">
        <IconLock size="16" /> Portal pakar
      </button>
      <button class="btn btn-t btn-sm" @click="router.push('/input')">
        Mulai sekarang
      </button>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { IconLeaf, IconLock } from '@tabler/icons-vue'

const router = useRouter()
</script>
