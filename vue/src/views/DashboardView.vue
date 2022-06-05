<template>
  <header-bar title="Dashboard"></header-bar>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-6">
    <div>
      <weather-comp></weather-comp>
    </div>
    <div class="col-span-2 row-span-2">
      <div class="h-full">
        <garden-map></garden-map>
      </div>
    </div>
    <div>
      <sensor-comp></sensor-comp>
    </div>
  </div>

  <!-- DEMO LAYOUTS -->
  <!-- <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <div>
      <div class="bg-gray-200 h-96 p-2">Weather</div>
    </div>
    <div class="col-span-3 row-span-2 order-last">
      <div class="bg-gray-200 h-96 p-2">Garden</div>
    </div>
    <div>
      <div class="bg-gray-200 h-full p-2">Sensor</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
  </div> -->

  <!-- <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <div>
      <div class="bg-gray-200 h-96 p-2">Weather</div>
    </div>
    <div>
      <div class="bg-gray-200 h-full p-2">Sensor</div>
    </div>
    <div class="col-span-1 row-span-2">
      <div class="bg-gray-200 h-full p-2">Garden</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
  </div> -->
</template>

<script setup lang="ts">
//####################################
//Test for weather / can be cleaned up
import { onMounted } from "vue";
import { weatherStore } from "../stores/weatherStore";
import { sensorStore } from "../stores/sensorStore";

import WeatherComp from "@/components/WeatherComp.vue";
// import SensorComp from "@/components/SensorComp.vue";
import SensorComp from "@/components/SensorCompQuasar.vue";
import GardenMap from "@/components/GardenMap.vue";
import HeaderBar from "@/components/HeaderBar.vue";

onMounted(() => {
  weatherStore().loadDataFromApi();
  sensorStore().loadDataFromApi();
});
//####################################
</script>
