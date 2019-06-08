import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: "/",
      component: () => import("@/containers/default"),
      redirect: { name: "Search" },
      name: "Root",
      children: [
        {
          path: "/_",
          name: "Search",
          component: () => import("@/views/Search")
        },
        {
          path: "/results",
          name: "Results",
          component: () => import("@/views/Results")
        }
      ]
    },
    {
      path: "*",
      redirect: { name: "Search" }
    }
  ]
});
