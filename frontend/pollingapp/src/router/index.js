import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { userData } from '@/stores/user'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: "/login",
    name: "login",
    component: () => import ('../views/LoginView.vue')
  },
  {
    path: "/participants",
    name: "participants",
    component: () => import ('../views/ParticipantsView.vue')
  },
  {
    path: "/register",
    name: "register",
    component: () => import('../views/RegisterView')
  },
  {
    path: "/admin",
    name: "admin",
    component: () => import('../views/AdminView')
  },
  {path: "/participant/:id",
  name: "DetailedView",
  props: true,
  component: () => import('../views/ParticipantDetailedView')}
]

const router = new VueRouter({
  routes
})



export default router
