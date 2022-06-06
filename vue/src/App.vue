<template>
  <div class="relative">
    <div class="flex items-start justify-between">
      <router-view name="sidebar"></router-view>
      <main class="flex flex-col w-full">
        <div>
          <router-view></router-view>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { weatherStore } from "@/stores/weatherStore";
import { sensorStore } from "@/stores/sensorStore";

onMounted(() => {
  weatherStore().loadDataFromApi();
  sensorStore().loadDataFromApi();
});
</script>
