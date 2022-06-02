<!---
TODO: If no weather information is available because the API is not accessible or the location cannot be found,
the component should be extended to include a message indicating that no weather data is available.
-->

<template>
  <div v-if="weather.current" class="card h-full w-full shadow-sm bg-[#fdfff9]">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">
        Wetter {{ weather.current.name }}
      </h2>
      <div class="card card-side">
        <figure>
          <img
            :src="`http://openweathermap.org/img/wn/${weather.current.icon}@2x.png`"
          />
        </figure>
        <div class="card-body">
          <h2 class="font-bold text-primary-focus">
            <!--TODO: Maybe move language and date options to settings?-->
            {{ weather.current.dt.toLocaleString("de-DE", dateOptions) }}
          </h2>
          <p class="mt-2 text-primary-focus text-2xl">
            {{ weather.current.tempMin.toFixed(1) }} /
            {{ weather.current.tempMax.toFixed(1) }}°C
          </p>
          <p class="mt-2 text-primary-focus">
            {{ weather.current.description }}
          </p>
        </div>
      </div>
      <!--<div class="grid grid-cols-3 mt-5">
        TODO: slice parameters could be added to later settings
        <div
          :key="forecast.dt.getDate"
          v-for="forecast in weather.forecast.slice(1, 4)"
        >
          <weather-forecast :forecast="forecast"></weather-forecast>
        </div>
      </div>-->
    </div>

    <test-line-chart></test-line-chart>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { weatherStore } from "../stores/weatherStore";
//import WeatherForecast from "@/components/WeatherForecast.vue";
//import TestBarChart from "@/components/TestBarChart.vue";
import TestLineChart from "@/components/TestLineChart.vue";

//const weather: Ref<Weather> = storeToRefs(weatherStore()).getWeather;
const { weather } = storeToRefs(weatherStore());

const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "long",
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
};
</script>
