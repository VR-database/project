import { createRouter, createWebHistory } from "vue-router";
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/Login",
      component: () => import("../components/LoginComp.vue"),
    },
    {
      path: "/",
      component: () => import("../components/Enter.vue"),
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
      path: "/Edit",
      component: () => import("../components/EditComp.vue"),
    },
    {
      path: "/Modal",
      component: () => import("../components/ModalComp.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ErrorComp.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ErrorComp.vue"),
    },
    {
      path: "/AcceptPassword",
      component: () => import("../components/Accept.vue"),
    },
    {
      path: "/AdminPassword",
      component: () => import("../components/AdminPassword.vue"),
    },
    {
      path: "/UserPassword",
      component: () => import("../components/UserPassword.vue"),
    },
    {
      path: "/SignUp",
      component: () => import("../components/SignUp.vue"),
    },
    {
      path: "/CodeEmail",
      component: () => import("../components/EmailCode.vue"),
    },
    {
      path: "/Enter",
      component: () => import("../components/Enter.vue"),
    },
    {
      path: "/Profile",
      component: () => import("../components/Profile.vue"),
    },
    {
      path: "/Table/:id",
      component: () => import("../components/MyTable.vue"),
    },
  ],
});
