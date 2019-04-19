import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      name: 'Search',
      component: () =>
        import("@/views/index")
    },
    {
      path: '/:query',
      name: 'Results',
      component: () =>
        import("@/views/results")
    },
    {
      path: "*",
      redirect: { name: 'Search' }
    }

  ]
})