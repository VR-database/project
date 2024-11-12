import axios from 'axios'
axios.defaults.baseURL = 'https://api.ar-vmgh.ru/'

axios.defaults.withCredentials = true
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
