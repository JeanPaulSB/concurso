import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSocketIO from 'vue-socket.io';
import { createPinia, PiniaVuePlugin } from 'pinia'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueCompositionAPI from '@vue/composition-api'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(PiniaVuePlugin)
const pinia = createPinia()
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(VueCompositionAPI)
Vue.config.productionTip = false

const socketio = require("socket.io-client")
//export const SocketInstance = socketio('http://64.226.64.94:8000')
export const SocketInstance = socketio('https://www.concursoupb.com')
Vue.use(new VueSocketIO({
  debug:true,
  connection: SocketInstance
}))


new Vue({
  router,
  pinia,
  render: h => h(App)
}).$mount('#app')
