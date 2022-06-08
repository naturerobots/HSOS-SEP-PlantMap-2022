<template>
  <header-bar title="Dashboard"></header-bar>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-6">
    <div>
      <weather-comp></weather-comp>
    </div>
    <div class="col-span-2 row-span-2">
      <div class="h-full">
        <garden-map :sensors="sensors" @sensor-click="sensorClick"></garden-map>
      </div>
    </div>
    <div>
      <sensor-comp :sensors="sensors"></sensor-comp>
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
import { sensorStore } from "@/stores/sensorStore";

import WeatherComp from "@/components/WeatherComp.vue";
// import SensorComp from "@/components/SensorComp.vue";
import SensorComp from "@/components/SensorCompQuasar.vue";
import GardenMap from "@/components/GardenMap.vue";
import HeaderBar from "@/components/HeaderBar.vue";

import { storeToRefs } from "pinia";
import type { Ref } from "vue";
import type { Sensor } from "@/types/sensor";

const sensors: Ref<Sensor[]> = storeToRefs(sensorStore()).getSensors;

//same works for sensorEnter, sensorLeave
function sensorClick(sensorId: number) {
  //TODO: handle sensorId, for example for highlighting the table row
  console.log(sensorId);
}

//####################################
</script>
