import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "@/views/DashboardView.vue";
import CropsView from "@/views/CropsView.vue";
import Crops3dView from "@/views/Crops3dView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import ImageUploadView from "@/views/ImageUploadView.vue";
import Sidebar from "@/components/SidebarMenuQuasar.vue";
import CropImageView from "@/views/CropImageView.vue";
import WeatherCharts from "@/views/WeatherCharts.vue";
import { userStore } from "@/stores/userStore";

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
      components: {
        default: DashboardView,
        sidebar: Sidebar,
      },
      meta: { requiresAuth: true },
    },
    {
      path: "/crops",
      name: "crops",
      components: {
        default: CropsView,
        sidebar: Sidebar,
      },
      meta: { requiresAuth: true },
    },
    {
      path: "/3d",
      name: "3d",
      components: {
        default: Crops3dView,
        sidebar: Sidebar,
      },
      meta: { requiresAuth: true },
    },
    {
      path: "/imageupload",
      name: "imageupload",
      components: {
        default: ImageUploadView,
        sidebar: Sidebar,
      },
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: "/cropimage",
      name: "cropimage",
      components: {
        default: CropImageView,
        sidebar: Sidebar,
      },
      meta: { requiresAuth: true },
    },
    {
      path: "/weathercharts",
      name: "weathercharts",
      components: {
        default: WeatherCharts,
        sidebar: Sidebar,
      },
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (import.meta.env.VITE_AUTH_REQUIRED === "true" && to.meta.requiresAuth) {
    if (userStore().isAuthenticated) {
      next();
    } else {
      next("/login");
    }
  } else {
    next();
  }
});

export default router;
