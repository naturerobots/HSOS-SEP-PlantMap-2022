<template>
  <h1>Weather Charts</h1>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <chart-rain-pop></chart-rain-pop>
    <chart-hourly-temp></chart-hourly-temp>
  </div>
</template>

<script setup lang="ts">
//import { weatherDataStore } from "@/stores/weatherDataStore";
import ChartRainPop from "@/components/Weather/ChartHourlyRainPop.vue";
import ChartHourlyTemp from "@/components/Weather/ChartHourlyTemp.vue";
</script>
