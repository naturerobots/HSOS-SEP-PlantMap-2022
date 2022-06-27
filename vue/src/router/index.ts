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
      component: DashboardView,
      meta: { requiresAuth: false },
    },
    {
      path: "/crops",
      name: "crops",
      component: CropsView,
      meta: { requiresAuth: false },
    },
    {
      path: "/3d",
      name: "3d",
      component: Crops3dView,
      meta: { requiresAuth: false },
    },
    {
      path: "/imageupload",
      name: "imageupload",
      component: ImageUploadView,
      props: true,
      meta: { requiresAuth: false },
    },
    {
      path: "/cropimage",
      name: "cropimage",
      component: CropImageView,
      meta: { requiresAuth: false },
    },
    {
      path: "/weathercharts",
      name: "weathercharts",
      component: WeatherCharts,
      meta: { requiresAuth: false },
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
  if (to.meta.requiresAuth) {
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
