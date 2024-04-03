import { createRouter, createWebHashHistory } from "vue-router";
export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/Login",
      component: () => import("../components/LoginComp.vue"),
    },
  ],
});
