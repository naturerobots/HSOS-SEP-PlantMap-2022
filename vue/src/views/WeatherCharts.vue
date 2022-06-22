<template>
  <h1>Weather Charts</h1>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <weather-chart-comp :chartType="'rainPop'"></weather-chart-comp>
  </div>
</template>

<script setup lang="ts">
//import { weatherDataStore } from "@/stores/weatherDataStore";
import WeatherChartComp from "@/components/weather/WeatherChartComp.vue";
</script>
