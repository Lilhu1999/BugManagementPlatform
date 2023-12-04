import Vue from 'vue'
import Router from 'vue-router'
import Layout from "../layout/Mainlayout.vue";
import Cookies from "vue-cookies"

Vue.use(Cookies)

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path:'/login',
      name:'login',
      component:() =>import('../main_page/login.vue')
    },
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      redirect:'/home',
      children:[
        {
          path:'/home',
          name:'home',
          component:() => import('../main_page/home.vue')
        },
        {
          path:'/document',
          name:'document',
          component:() => import('../main_page/document.vue')
        },
        {
          path:'/project',
          name:'project',
          component:() => import('../main_page/project.vue'),
        },
        {
          path: '/pj',
          name:'pj',
          component:()=>import('../layout/project_layout.vue'),
          children:[
            {
              path:'requirement',
              name:'requirement',
              component:()=>import('../project_page/requirement_page.vue'),
            },
            {
              path:'defect',
              name:'defect',
              component:()=>import('../project_page/defect_page.vue'),
            },
            {
              path:'testCase',
              name:'testCase',
              component:()=>import('../project_page/testCase_page.vue'),
            },
            {
              path:'document',
              name:'document',
              component:()=>import('../project_page/document_page.vue'),
            },
            {
              path:'iteration',
              name:'iteration',
              component:()=>import('../project_page/iteration_page.vue'),
            },
          ]
        },
        {
          path:'/autoTest',
          name:'autoTest',
          component:() => import('../main_page/autoTest.vue')
        },
        {
          path:'/setting',
          name:'setting',
          component:() => import('../main_page/setting.vue'),
          beforeEnter:(to, from, next)=>{
            const userType = window.$cookies.get('user_type')
            if (userType !== '管理员') {
              next('/home')
              alert('对不起，您暂时无权查看')
            }else {
              next()
            }
          },
        },
        {
          path:'/projectManager',
          name:'projectManager',
          component:() => import('../sys_child_page/project_manager.vue')
        },
        {
          path:'/partManager',
          name:'partManager',
          component:() => import('../sys_child_page/part_manager.vue')
        },
        {
          path:'/documentManage',
          name:'documentManage',
          component:() => import('../sys_child_page/document_manage.vue')
        },
      ]
    },
  ]
})

export default router;

router.beforeEach((to, from, next) => {
  const isLoggedIn = window.$cookies.get('username') // 根据实际情况判断用户是否已登录
  if (to.path !== '/login' && !isLoggedIn) {
    // 如果用户未登录且访问的不是登录页，则重定向到登录页
    alert('登录过期')
    next('/login');
  } else {
    // 已登录或者访问的是登录页，则正常跳转
    next();
  }
});
