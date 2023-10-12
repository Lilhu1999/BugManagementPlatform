import Vue from 'vue'
import Router from 'vue-router'
import Layout from "../layout/Mainlayout.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      redirect:'/home',
      children:[
        {
          path:'home',
          name:'home',
          component:() => import('../main_page/home.vue')
        },
        {
          path:'document',
          name:'document',
          component:() => import('../main_page/document.vue')
        },
        {
          path:'project',
          name:'project',
          component:() => import('../main_page/project.vue')
        },
        {
          path:'message',
          name:'message',
          component:() => import('../main_page/message.vue')
        },
        {
          path:'setting',
          name:'setting',
          component:() => import('../main_page/setting.vue')
        },
        {
          path:'projectManager',
          name:'projectManager',
          component:() => import('../sys_child_page/project_manager.vue')
        },
        {
          path:'partManager',
          name:'partManager',
          component:() => import('../sys_child_page/part_manager.vue')
        },
      ]
    },
  ]
})
