import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createI18n } from 'vue-i18n';

// Axios 配置
const app = createApp(App);
app.config.globalProperties.$axios = axios; // 将 axios 设置为全局可用
axios.defaults.baseURL = 'http://localhost:8000'; // 设置默认的请求 URL

// I18n 配置
const messages = {
  en: {
    message: {
      hello: 'Hello world',
    },
  },
  zh: {
    message: {
      hello: '你好，世界',
    },
  },
};

const i18n = createI18n({
  locale: 'en', // 设置默认语言
  fallbackLocale: 'en', // 设置备用语言
  messages,
});

// 应用 I18n 插件
app.use(i18n);

app.mount('#app');
