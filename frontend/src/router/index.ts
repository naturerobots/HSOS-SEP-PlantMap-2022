import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue";
import CropsView from "../views/CropsView.vue";
import Crops3dView from "../views/Crops3dView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/dashboard",
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashboardView,
    },
    {
      path: "/crops",
      name: "crops",
      component: CropsView,
    },
    {
      path: "/3d",
      name: "3d",
      component: Crops3dView,
    },
  ],
});

export default router;
