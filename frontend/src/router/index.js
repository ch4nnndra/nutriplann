import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Input from '@/views/Input.vue'
import Result from '@/views/Result.vue'
import Login from '@/views/Login.vue'
import Dashboard from '@/views/Dashboard.vue'
import Pending from '@/views/Pending.vue'
import History from '@/views/History.vue'
import Detail from '@/views/Detail.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/input', name: 'Input', component: Input },
  { path: '/result', name: 'Result', component: Result },
  { path: '/login', name: 'Login', component: Login },
  { path: '/expert/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/expert/pending', name: 'Pending', component: Pending },
  { path: '/expert/history', name: 'History', component: History },
  { path: '/expert/detail/:id', name: 'Detail', component: Detail },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  const expertRoutes = ['/expert/dashboard', '/expert/pending', '/expert/history']
  const isExpertRoute = expertRoutes.some(r => to.path.startsWith(r)) || to.path.startsWith('/expert/detail')
  if (isExpertRoute) {
    const token = localStorage.getItem('expertToken')
    if (!token) return '/login'
  }
})

export default router
