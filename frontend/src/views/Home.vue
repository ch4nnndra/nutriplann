<template>
  <div class="min-h-screen bg-bg3">
    <NavbarPublic />

    <div class="px-8 pt-[60px] pb-[56px] bg-bg2">
      <div class="max-w-[960px] mx-auto grid grid-cols-2 gap-12 items-center">
        <div>
          <div class="text-[11px] font-semibold uppercase tracking-widest text-[#085041] bg-t50 px-2.5 py-1 rounded-full inline-block mb-3.5">
            Program diet personal
          </div>
          <h1 class="text-[36px] font-semibold leading-[1.15] tracking-tight mb-3.5">
            Rekomendasi diet <span class="text-t">tepat</span> untuk kondisi kesehatanmu
          </h1>
          <p class="text-[14px] text-tx2 leading-relaxed mb-6">
            Isi data kesehatanmu sekali — sistem kami menganalisis profil kondisimu dari 1.000+ data klinis dan menghasilkan program diet yang divalidasi langsung oleh pakar gizi sebelum diberikan padamu.
          </p>
          <div class="flex gap-2.5 items-center">
            <button class="btn btn-t btn-t-lg" @click="router.push('/input')">
              Mulai rekomendasi saya <IconArrowRight size="18" />
            </button>
            <button class="btn btn-out py-3" @click="router.push('/login')">
              Masuk sebagai pakar
            </button>
          </div>
        </div>
        <div>
          <div class="bg-bg border border-bd rounded-r16 p-5 relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-t rounded-t-r16"></div>
            <div class="flex items-center gap-2 mt-1 mb-3.5">
              <div class="w-9 h-9 bg-t50 rounded-full flex items-center justify-center text-t">
                <IconUser size="16" />
              </div>
              <div>
                <div class="text-[13px] font-semibold">Profil: Budi, 45 tahun</div>
                <div class="text-[11px] text-tx2">BMI 27.7 · Diabetes · Overweight</div>
              </div>
              <span class="badge b-green ml-auto"><IconCheck size="14" /> Tervalidasi</span>
            </div>
            
            <div class="bg-t50 rounded-r8 p-3.5 mb-3 border border-t100">
              <div class="text-[11px] font-semibold uppercase tracking-widest text-[#085041] mb-1">Program yang direkomendasikan</div>
              <div class="text-[17px] font-semibold text-[#085041]">Diet Rendah Karbohidrat</div>
              <div class="text-[11px] text-[#0F6E56] mt-0.5">untuk penderita diabetes dengan berat badan berlebih</div>
            </div>
            
            <div class="grid grid-cols-4 gap-2 mb-3">
              <div class="bg-bg2 rounded-r8 p-2 text-center">
                <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Kalori</div>
                <div class="text-[18px] font-semibold text-am">1.800</div>
                <div class="text-[9px] text-tx3">kkal</div>
              </div>
              <div class="bg-bg2 rounded-r8 p-2 text-center">
                <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Protein</div>
                <div class="text-[18px] font-semibold text-t">90</div>
                <div class="text-[9px] text-tx3">gram</div>
              </div>
              <div class="bg-bg2 rounded-r8 p-2 text-center">
                <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Karbo</div>
                <div class="text-[18px] font-semibold text-p400">150</div>
                <div class="text-[9px] text-tx3">gram</div>
              </div>
              <div class="bg-bg2 rounded-r8 p-2 text-center">
                <div class="text-[9px] font-semibold uppercase text-tx3 mb-0.5">Lemak</div>
                <div class="text-[18px] font-semibold text-[#185FA5]">60</div>
                <div class="text-[9px] text-tx3">gram</div>
              </div>
            </div>
            
            <div class="flex items-center gap-1.5 text-[11px] text-tx2 bg-bg2 px-2.5 py-2 rounded-r8">
              <IconStethoscope class="text-p" size="14" />
              Ditinjau dan dikonfirmasi oleh pakar gizi sebelum diberikan
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-t py-4 px-8 flex justify-center gap-[60px] text-white text-center">
      <div><div class="text-[24px] font-semibold">1.000+</div><div class="text-[11px] opacity-75 mt-0.5">Data klinis referensi</div></div>
      <div><div class="text-[24px] font-semibold">3</div><div class="text-[11px] opacity-75 mt-0.5">Program diet tersedia</div></div>
      <div><div class="text-[24px] font-semibold">100%</div><div class="text-[11px] opacity-75 mt-0.5">Divalidasi pakar</div></div>
      <div><div class="text-[24px] font-semibold">6</div><div class="text-[11px] opacity-75 mt-0.5">Faktor kesehatan dianalisis</div></div>
    </div>

    <div class="py-12 px-8">
      <div class="max-w-[960px] mx-auto">
        <div class="text-center mb-8">
          <div class="text-[11px] font-semibold uppercase tracking-widest text-[#085041] bg-t50 px-2.5 py-1 rounded-full inline-block mb-2.5">Cara kerja</div>
          <h2 class="text-[26px] font-semibold tracking-tight mb-2">Empat langkah menuju program diet yang tepat</h2>
          <p class="text-[14px] text-tx2 max-w-[480px] mx-auto">Dari mengisi data kondisimu hingga mendapat program diet yang sudah divalidasi pakar.</p>
        </div>
        
        <div class="grid grid-cols-4 gap-4">
          <div class="bg-bg border border-bd rounded-r12 p-5 text-center hover:border-t100 transition-colors">
            <div class="w-11 h-11 bg-t50 text-t rounded-r8 flex items-center justify-center mx-auto mb-3">
              <IconClipboardList size="20" />
            </div>
            <div class="text-[10px] font-semibold text-t100 uppercase tracking-widest mb-1.5">Langkah 1</div>
            <div class="text-[13px] font-semibold mb-1">Isi data kesehatan</div>
            <div class="text-[12px] text-tx2 leading-relaxed">Masukkan kondisi kesehatanmu: fisik, riwayat penyakit, gaya hidup, dan preferensi makan.</div>
          </div>
          
          <div class="bg-bg border border-bd rounded-r12 p-5 text-center hover:border-t100 transition-colors">
            <div class="w-11 h-11 bg-t50 text-t rounded-r8 flex items-center justify-center mx-auto mb-3">
              <IconSearch size="20" />
            </div>
            <div class="text-[10px] font-semibold text-t100 uppercase tracking-widest mb-1.5">Langkah 2</div>
            <div class="text-[13px] font-semibold mb-1">Analisis pencocokan</div>
            <div class="text-[12px] text-tx2 leading-relaxed">Sistem mencocokkan kondisimu dengan profil serupa dari 1.000+ data klinis untuk menghasilkan rekomendasi awal.</div>
          </div>
          
          <div class="bg-bg border border-bd rounded-r12 p-5 text-center hover:border-t100 transition-colors">
            <div class="w-11 h-11 bg-[#EEF2FF] text-[#4338CA] rounded-r8 flex items-center justify-center mx-auto mb-3">
              <IconUserCheck size="20" />
            </div>
            <div class="text-[10px] font-semibold text-t100 uppercase tracking-widest mb-1.5">Langkah 3</div>
            <div class="text-[13px] font-semibold mb-1">Validasi pakar gizi</div>
            <div class="text-[12px] text-tx2 leading-relaxed">Pakar gizi meninjau dan mengkonfirmasi rekomendasi sebelum program diet diberikan padamu.</div>
          </div>
          
          <div class="bg-bg border border-bd rounded-r12 p-5 text-center hover:border-t100 transition-colors">
            <div class="w-11 h-11 bg-[#EAF3DE] text-[#3B6D11] rounded-r8 flex items-center justify-center mx-auto mb-3">
              <IconRefresh size="20" />
            </div>
            <div class="text-[10px] font-semibold text-t100 uppercase tracking-widest mb-1.5">Langkah 4</div>
            <div class="text-[13px] font-semibold mb-1">Sistem terus berkembang</div>
            <div class="text-[12px] text-tx2 leading-relaxed">Setiap kasus baru yang tervalidasi memperkaya data referensi — rekomendasi semakin akurat dari waktu ke waktu.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import NavbarPublic from '@/components/NavbarPublic.vue'
import { 
  IconArrowRight, IconUser, IconCheck, IconStethoscope,
  IconClipboardList, IconSearch, IconUserCheck, IconRefresh
} from '@tabler/icons-vue'

const router = useRouter()
</script>
