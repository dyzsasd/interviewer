import { createApp } from 'vue'
import Vue from 'vue'
import App from './App.vue'
import './assets/tailwind.css'
import axios from 'axios'
import VueI18n from 'vue-i18n'

Vue.config.productionTip = false
Vue.use(VueI18n)

// 配置 Axios
Vue.prototype.$axios = axios
axios.defaults.baseURL = 'http://localhost:8000' // 调整为 Django 服务器的地址

// 国际化的消息
const messages = {
    en: {
      message: {
        hello: 'hello world'
      }
    },
    zh: {
      message: {
        hello: '你好，世界'
      }
    }
  }

// 创建 VueI18n 实例
const i18n = new VueI18n({
  locale: 'en', // 设置地区
  messages, // 设置地区信息
})

new Vue({
  i18n,
  render: h => h(App),
}).$mount('#app')
