<template>
  <div class="h-screen overflow-hidden relative">
    <div class="flex items-start justify-between">
      <Sidebar />
      <main class="flex flex-col w-full p-2">
        <div>
          <RouterView />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
import Sidebar from "@/components/SidebarMenu.vue";
</script>
