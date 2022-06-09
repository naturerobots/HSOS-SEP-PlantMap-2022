<template>
  <h1>Weather Charts</h1>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <chart-hourly-rain-pop></chart-hourly-rain-pop>
    <chart-hourly-temp></chart-hourly-temp>
    <chart-hourly-wind></chart-hourly-wind>
    <weather-chart-comp :chartType="'rainPop'"></weather-chart-comp>
  </div>
</template>

<script setup lang="ts">
//import { weatherDataStore } from "@/stores/weatherDataStore";
import ChartHourlyRainPop from "@/components/Weather/ChartHourlyRainPop.vue";
import ChartHourlyTemp from "@/components/Weather/ChartHourlyTemp.vue";
import ChartHourlyWind from "@/components/Weather/ChartHourlyWind.vue";
import WeatherChartComp from "@/components/Weather/WeatherChartComp.vue";
</script>
