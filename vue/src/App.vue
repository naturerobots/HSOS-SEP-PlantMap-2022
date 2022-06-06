<template>
  <div class="h-screen overflow-hidden relative">
    <div class="flex items-start justify-between">
      <router-view name="sidebar"></router-view>
      <main class="flex flex-col w-full p-2">
        <div>
          <router-view></router-view>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeMount, onMounted } from "vue";
import { weatherDataStore } from "@/stores/weatherDataStore";

onMounted(async () => {
  console.log("onBeforeMount start");
  weatherDataStore().initWeatherData();
  console.log("onBeforeMount end");
});
</script>
