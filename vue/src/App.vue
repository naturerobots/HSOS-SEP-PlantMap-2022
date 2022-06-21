<template>
  <q-layout view="lHh lpr lFf">
    <div class="relative">
      <div class="row flex justify-between">
        <!--items-start-->
        <router-view name="sidebar"></router-view>
        <main class="flex flex-col ml-28 w-full">
          <div>
            <router-view></router-view>
          </div>
        </main>
      </div>
    </div>
  </q-layout>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { weatherDataStore } from "@/stores/weatherDataStore";
import { sensorStore } from "@/stores/sensorStore";

onMounted(() => {
  weatherDataStore().initWeatherData();
  sensorStore().loadDataFromApi();
});
</script>
