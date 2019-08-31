import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Login from '@/components/Login'
import Registration from '@/components/Registration'
import Profile from '@/components/Profile'
import Troskovi from '@/components/Troskovi'
import Statistika from '@/components/Statistika'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/troskovi',
      name: 'Troskovi',
      component: Troskovi
    },
    {
      path: '/statistika',
      name: 'Statistika',
      component: Statistika
    },
    {
      path: '/*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
/*
const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/login', component: 'Login' },
  { path: '/registration', component: 'Registration' },
  { path: '/about', component: 'About' },
  { path: '/troskovi', component: 'Troskovi' },
  { path: '/*', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
export default new Router({
  routes,
  mode: 'history'
})
*/
