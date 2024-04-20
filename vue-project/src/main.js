import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

axios.defaults.withCredentials = true
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
