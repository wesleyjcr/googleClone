import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Searchbox from '@/components/Searchbox'
import Insert from '@/components/Insert'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Searchbox',
      component: Searchbox
    },
    {
      path: '/insert',
      name: 'Insert',
      component: Insert
    }
  ]
})
