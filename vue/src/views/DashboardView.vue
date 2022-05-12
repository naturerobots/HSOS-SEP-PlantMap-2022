<template>
  <h1>Dashboard</h1>
  <!--Test for weather / can be removed-->
  <weather-comp></weather-comp>
  <sensor-comp></sensor-comp>
</template>

<script setup lang="ts">
//####################################
//Test for weather / can be cleaned up
import { onMounted } from "vue";
import { weatherStore } from "../stores/weatherStore";

import WeatherComp from "@/components/WeatherComp.vue";
import SensorComp from "@/components/SensorComp.vue";

onMounted(() => {
  weatherStore().loadDataFromApi();
});
//####################################
</script>
