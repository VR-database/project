import { createRouter, createWebHistory } from "vue-router";
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/Login",
      component: () => import("../components/LoginComp.vue"),
    },
    {
      path: "/Table",
      component: () => import("../components/TableComp.vue"),
    },
    {
      path: "/Add",
      component: () => import("../components/AddComp.vue"),
    },
    {
      path: "/test",
      component: () => import("../components/testcomp.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ErrorComp.vue"),
    },

  ],
  scrollBehavior: function(to, from, savedPosition) {
    if (to.hash) {

        //Or for Vue 3:
      return {el: to.hash}
    } else {
        return { x: 0, y: 0 }
    }
},
});
