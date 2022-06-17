<!---
TODO: If no weather information is available because the API is not accessible or the location cannot be found,
the component should be extended to include a message indicating that no weather data is available.
-->

<!-- v-if="Object.keys(current).length > 0 && Object.keys(forecast).length > 0"-->
<template>
  <div class="card bg-white">
    <div class="card-body">
      <div class="grid grid-cols-3">
        <div class="flex items-center justify-center">
          <img
            :src="`http://openweathermap.org/img/wn/${current.weather[0].icon}@2x.png`"
          />
        </div>
        <div>
          <div class="mt-2 text-primary-focus text-4xl font-bold">
            {{ current?.main?.temp?.toFixed(0) }} °C
          </div>
          <div class="text-primary-focus text-2xl">
            {{ (forecast.daily ?? {})[0]?.temp?.min?.toFixed(0) ?? "N/A" }}° /
            {{ (forecast.daily ?? {})[0]?.temp?.max?.toFixed(0) ?? "N/A" }}°
          </div>
        </div>
        <div>
          <div class="mt-2 text-primary-focus text-2xl font-bold">
            {{ current.name }}
          </div>
          <div
            class="mt-2 text-primary-focus text-base font-bold text-gray-500"
          >
            {{
              new Date(current.dt * 1000).toLocaleString("de-DE", dateOptions)
            }}
          </div>
        </div>
      </div>
      <weather-chart-comp :chart-type="'rainPop'"></weather-chart-comp>
    </div>

    <!--TODO: 3 day forecast necessary?-->
    <!--
    <div v-if="forecast.daily" class="grid grid-cols-3 mt-5">
      <div :key="forecastDaily.dt" v-for="forecastDaily in forecast.daily.slice(1, 4)">
        <weather-forecast :forecast="forecastDaily"></weather-forecast>
      </div>
    </div>
     -->
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { weatherDataStore } from "@/stores/weatherDataStore";
import WeatherForecast from "@/components/Weather/WeatherForecast.vue";
import type { Ref } from "vue";
import type {
  WeatherDataForecast,
  WeatherDataCurrent,
} from "@/types/weatherData";
import WeatherChartComp from "./WeatherChartComp.vue";

const current: Ref<WeatherDataCurrent> = storeToRefs(
  weatherDataStore()
).getCurrent;
const forecast: Ref<WeatherDataForecast> = storeToRefs(
  weatherDataStore()
).getForecast;

const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "long",
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
};
</script>

<style></style>
