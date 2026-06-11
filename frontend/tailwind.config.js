/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        t: '#0F6E56',
        t50: '#E1F5EE',
        t100: '#9FE1CB',
        t200: '#5DCAA5',
        t400: '#1D9E75',
        p: '#3C3489',
        p50: '#EEEDFE',
        p100: '#CECBF6',
        p200: '#AFA9EC',
        p400: '#7F77DD',
        am: '#BA7517',
        am50: '#FAEEDA',
        am100: '#FAC775',
        bg: '#FFFFFF',
        bg2: '#F8F9FA',
        bg3: '#F1F3F5',
        tx: '#1A1A1A',
        tx2: '#555F6D',
        tx3: '#9AA3AC',
        bd: '#E5E7EB',
        bd2: '#D1D5DB',
      },
      borderRadius: {
        'r8': '8px',
        'r12': '12px',
        'r16': '16px',
        'r20': '20px',
      }
    },
  },
  plugins: [],
}
