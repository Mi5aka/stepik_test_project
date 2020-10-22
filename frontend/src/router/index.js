import Vue from 'vue'
import VueRouter from 'vue-router'
// import Decisions from '../components/CodemirrorChild'

Vue.use(VueRouter)

export const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/'
      // component: Decisions
    }
  ]
})
