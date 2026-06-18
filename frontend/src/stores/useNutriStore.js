import { defineStore } from 'pinia'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export const useNutriStore = defineStore('nutri', {
  state: () => ({
    patientData: null,
    recommendationResult: null,
    expertToken: localStorage.getItem('expertToken') || null,
    expertData: null,
    pendingCases: [],
    historyCases: [],
    expertStatistics: {}
  }),
  actions: {
    async submitRecommendation(data) {      
      try {
        const res = await axios.post(`${API_URL}/predict`, data)
        this.patientData = data
        this.recommendationResult = res.data
        localStorage.setItem('patientData', JSON.stringify(data))
        localStorage.setItem('recommendationResult', JSON.stringify(res.data))
        return res.data
      } catch (err) {
        console.error("Error submitting recommendation", err)
        throw err
      }
    },
    async loginExpert(email, password) {
      try {
        const res = await axios.post(`${API_URL}/expert/login`, { email, password })
        console.log(res.data);
        this.expertToken = res.data.access_token
        localStorage.setItem('expertToken', this.expertToken)
        this.expertData = { name: res.data.expert.name, email: res.data.expert.email }
        return true
      } catch (err) {
        console.error("Login failed", err)
        return false
      }
    },
    logoutExpert() {
      this.expertToken = null
      this.expertData = null
      localStorage.removeItem('expertToken')
    },
    async fetchPending() {
      try {
        const res = await axios.get(`${API_URL}/expert/pending`, {
          headers: {
            'Authorization': `Bearer ${this.expertToken}`
          }
        })
        this.pendingCases = res.data.cases
      } catch (err) {
        console.error("Fetch pending failed", err)
      }
    },
    async fetchHistory() {
      try {
        const res = await axios.get(`${API_URL}/expert/history`, {
          headers: {
            'Authorization': `Bearer ${this.expertToken}`
          }
        })
        this.historyCases = res.data.cases
      } catch (err) {
        console.error("Fetch history failed", err)
      }
    },
    async fetchDashboard() {
      try {
        const res = await axios.get(`${API_URL}/expert/dashboard`, {
          headers: {
            'Authorization': `Bearer ${this.expertToken}`
          }
        })
        this.expertStatistics = res.data
      } catch (err) {
        console.error("Fetch history failed", err)
      }
    },
    async validateCase(case_id, solution) {
      try {
        await axios.post(`${API_URL}/expert/validate`, { case_id, solution }, {
          headers: {
            'Authorization': `Bearer ${this.expertToken}`
          }
        })
        await this.fetchPending()
        await this.fetchHistory()
        return true
      } catch (err) {
        console.error("Validation failed", err)
        return false
      }
    }
  }
})
