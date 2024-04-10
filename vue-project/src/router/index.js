import { createRouter, createWebHashHistory } from "vue-router";
export default createRouter({
  history: createWebHashHistory(),
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
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ErrorComp.vue"),
    },
  ],
});
