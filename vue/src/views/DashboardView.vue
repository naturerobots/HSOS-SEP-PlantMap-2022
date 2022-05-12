<template>
  <!-- <h1>Dashboard</h1> -->
  <!--Test for weather / can be removed-->
  <weather-comp></weather-comp>

  <!-- <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <div>
      <div class="bg-gray-200 h-96 p-2">Weather</div>
    </div>
    <div class="col-span-2 row-span-2">
      <div class="bg-gray-200 h-full p-2">Garden</div>
    </div>
    <div>
      <div class="bg-gray-200 h-48 p-2">Sensor</div>
    </div>
  </div> -->

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

import WeatherComp from "@/components/WeatherComp.vue";

onMounted(() => {
  weatherStore().loadDataFromApi();
});
//####################################
</script>
