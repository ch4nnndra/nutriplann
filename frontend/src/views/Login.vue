<template>
  <div class="min-h-screen bg-p flex items-center justify-center p-5">
    <div class="bg-bg rounded-r20 px-8 py-9 w-[380px]">
      <div class="text-[15px] font-semibold text-p mb-1.5 flex items-center gap-1.5">
        <IconLeaf class="text-t" size="18" /> NutriPlan
      </div>
      <div class="inline-flex items-center gap-1 bg-p50 text-p px-2.5 py-1 rounded-full text-[11px] font-semibold uppercase tracking-widest mb-3.5">
        <IconShieldCheck size="14" /> Portal pakar
      </div>
      <h1 class="text-[22px] font-semibold tracking-tight mb-1">Masuk ke akun pakar</h1>
      <p class="text-[13px] text-tx2 mb-6">Akses dashboard untuk meninjau dan memvalidasi program diet yang direkomendasikan sistem kepada pasien.</p>
      
      <div class="fg">
        <label>Username / Email</label>
        <input type="text" v-model="username" placeholder="pakar@example.com">
      </div>
      <div class="fg">
        <label>Kata sandi</label>
        <div class="relative">
          <input :type="showPwd ? 'text' : 'password'" v-model="password" placeholder="••••••••">
          <button @click="showPwd = !showPwd" class="absolute right-2.5 top-1/2 -translate-y-1/2 bg-none border-none cursor-pointer text-tx3">
            <IconEyeOff v-if="showPwd" size="18" />
            <IconEye v-else size="18" />
          </button>
        </div>
      </div>
      
      <button class="btn btn-p w-full justify-center py-2.5 mt-1 text-[14px]" @click="login">
        <IconLogin size="18" /> Masuk ke dashboard
      </button>
      
      <div class="text-center mt-3.5 text-[12px] text-tx2">
        Bukan pakar? <span class="text-t cursor-pointer font-medium" @click="router.push('/')">Kembali ke beranda</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useNutriStore } from '@/stores/useNutriStore'
import { IconLeaf, IconShieldCheck, IconEye, IconEyeOff, IconLogin } from '@tabler/icons-vue'

const router = useRouter()
const store = useNutriStore()

const username = ref('pakar@example.com')
const password = ref('12345678')
const showPwd = ref(false)

const login = async () => {
  const success = await store.loginExpert(username.value, password.value)
  if (success) {
    router.push('/expert/dashboard')
  } else {
    alert("Login gagal, cek username dan password")
  }
}
</script>
