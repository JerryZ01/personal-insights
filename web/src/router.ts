import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Skills from '../views/Skills.vue'
import Timeline from '../views/Timeline.vue'
import Health from '../views/Health.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/skills', name: 'Skills', component: Skills },
  { path: '/timeline', name: 'Timeline', component: Timeline },
  { path: '/health', name: 'Health', component: Health },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
