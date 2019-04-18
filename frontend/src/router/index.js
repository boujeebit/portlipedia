import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      component: () =>
        import("@/containers/default"),
      redirect: { name: 'Search' },
      name: 'Root',
      children: [
        {
          path: '/_',
          name: 'Search',
          component: () =>
            import("@/views/index")
        },
        {
          path: '/search',
          name: 'Results',
          // props: (route) => ({ query: route.query.q }),
          props: true,
          component: () =>
            import("@/views/results")
        }
      ]
    },
    {
      path: "*",
      redirect: { name: 'Search' }
    }

  ]
})