import { defineStore } from 'pinia'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export const useNutriStore = defineStore('nutri', {
  state: () => ({
    patientData: null,
    recommendationResult: null,
    expertToken: localStorage.getItem('expertToken') || null,
    pendingCases: [],
    historyCases: []
  }),
  actions: {
    async submitRecommendation(data) {
      try {
        const res = await axios.post(`${API_URL}/recommend`, data)
        this.patientData = data
        this.recommendationResult = res.data
        return res.data
      } catch (err) {
        console.error("Error submitting recommendation", err)
        throw err
      }
    },
    async loginExpert(username, password) {
      try {
        const res = await axios.post(`${API_URL}/auth/login`, { username, password })
        this.expertToken = res.data.access_token
        localStorage.setItem('expertToken', this.expertToken)
        return true
      } catch (err) {
        console.error("Login failed", err)
        return false
      }
    },
    logoutExpert() {
      this.expertToken = null
      localStorage.removeItem('expertToken')
    },
    async fetchPending() {
      try {
        const res = await axios.get(`${API_URL}/expert/pending`)
        this.pendingCases = res.data
      } catch (err) {
        console.error("Fetch pending failed", err)
      }
    },
    async fetchHistory() {
      try {
        const res = await axios.get(`${API_URL}/expert/history`)
        this.historyCases = res.data
      } catch (err) {
        console.error("Fetch history failed", err)
      }
    },
    async validateCase(case_id, status) {
      try {
        await axios.post(`${API_URL}/expert/validate`, { case_id, status })
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
