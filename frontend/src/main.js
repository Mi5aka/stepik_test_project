// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSSE from 'vue-sse'

import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/darcula.css'
import 'codemirror/mode/python/python.js'

import App from './App.vue'
import store from './store'
// import * as router from './router'

Vue.use(VueAxios, axios)
Vue.use(VueSSE)
Vue.use(Vuex)
Vue.use(VueCodemirror, {
  options: {
    theme: 'darcula',
    mode: 'python',
    tabSize: 4,
    lineNumbers: true,
    line: true,
    placeholder: '#',
    value: '# write here',
    lineWrapping: true,
    inputStyle: 'textarea'

  }
})

Vue.config.productionTip = false

new Vue({ // eslint-disable-line no-new
  el: '#app',
  store,
  // router,
  template: '<App/>',
  render: h => h(App),
  components: { App }
})
