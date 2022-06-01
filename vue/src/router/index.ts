import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "@/views/DashboardView.vue";
import CropsView from "@/views/CropsView.vue";
import Crops3dView from "@/views/Crops3dView.vue";
import LoginView from "@/views/LoginView.vue";
import ImageUploadView from "@/views/ImageUploadView.vue";
import Sidebar from "@/components/SidebarMenu.vue";
import CropImageView from "@/views/CropImageView.vue";

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
    },
    {
      path: "/crops",
      name: "crops",
      components: {
        default: CropsView,
        sidebar: Sidebar,
      },
    },
    {
      path: "/3d",
      name: "3d",
      components: {
        default: Crops3dView,
        sidebar: Sidebar,
      },
    },
    {
      path: "/imageupload",
      name: "imageupload",
      components: {
        default: ImageUploadView,
        sidebar: Sidebar,
      },
    },
    {
      path: "/cropimage",
      name: "cropimage",
      components: {
        default: CropImageView,
        sidebar: Sidebar,
      },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
  ],
});

export default router;
