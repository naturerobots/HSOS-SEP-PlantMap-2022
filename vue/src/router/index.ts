import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "@/views/DashboardView.vue";
import CropsView from "@/views/CropsView.vue";
import Crops3dView from "@/views/Crops3dView.vue";
import Crops3dViewScene from "@/views/Crops3dViewScene.vue";
import LoginView from "@/views/LoginView.vue";
import OnboardingCompany from "@/views/onboarding/OnboardingCompany.vue";
import OnboardingGarden from "@/views/onboarding/OnboardingGarden.vue";
import RegisterView from "@/views/RegisterView.vue";
import ImageUploadView from "@/views/ImageUploadView.vue";
import CropImageView from "@/views/CropImageView.vue";
import SettingsView from "@/views/SettingsView.vue";
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
      meta: { requiresAuth: true },
    },
    {
      path: "/crops",
      name: "crops",
      component: CropsView,
      meta: { requiresAuth: true },
    },
    {
      path: "/3d",
      name: "3d",
      component: Crops3dView,
      meta: { requiresAuth: true },
    },
    {
      path: "/3d/Scene",
      name: "3dscene",
      component: Crops3dViewScene,
      meta: { requiresAuth: true },
    },
    {
      path: "/imageupload",
      name: "imageupload",
      component: ImageUploadView,
      meta: { requiresAuth: true },
    },
    {
      path: "/cropimage",
      name: "cropimage",
      component: CropImageView,
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/settings",
      name: "settings",
      component: SettingsView,
      meta: { requiresAuth: true },
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/onboarding-company",
      name: "onboarding-company",
      component: OnboardingCompany,
      meta: { requiresAuth: true },
    },
    {
      path: "/onboarding-garden",
      name: "onboarding-garden",
      component: OnboardingGarden,
      meta: { requiresAuth: true },
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
