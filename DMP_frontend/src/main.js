// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import router from './router'
import VueCookies from 'vue-cookies'

import 'element-ui/lib/theme-chalk/index.css'

Vue.use(VueCookies);
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueResource)
Vue.prototype.$axios = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
