import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      name: 'TaskList',
      component: () => import('@/views/TaskList/index.vue'),
    },
    {
      path: '/task/:taskId',
      name: 'TaskDetail',
      component: () => import('@/views/TaskDetail/index.vue'),
    },
  ],
  scrollBehavior() {
    return {
      left: 0,
      top: 0,
    }
  },
})

export default router