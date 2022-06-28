<template>
  <!-- <q-layout view="lHh lpr lFf" class="h-full"> -->
  <!-- <div class="relative h-full"> -->
  <!-- <div class="row flex justify-between h-full"> -->
  <!--items-start-->
  <div class="flex flex-row h-full flex-nowrap">
    <router-view name="sidebar"></router-view>
    <main class="flex flex-col flex-1 w-full h-full">
      <router-view></router-view>
    </main>
  </div>

  <!-- </div> -->
  <!-- </div> -->
  <!-- </q-layout> -->
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { weatherDataStore } from "@/stores/weatherDataStore";
import { sensorStore } from "@/stores/sensorStore";
import { cropsStore } from "./stores/cropsStore";

onMounted(() => {
  weatherDataStore().initWeatherData();
  sensorStore().loadDataFromApi();
  cropsStore().loadDataFromApi();
});
</script>
