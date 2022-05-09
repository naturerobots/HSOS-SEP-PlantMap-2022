<!---
TODO: Create the date in the store or service. Must then also be changed in WeatherComp.
-->
<template>
  <div class="text-center">
    <h2 class="font-bold text-primary-focus">
      {{ new Date(forecast.dt * 1000).toLocaleString("de-DE", dateOptions) }}
    </h2>
    <figure>
      <img :src="`http://openweathermap.org/img/wn/${forecast.icon}@2x.png`" />
    </figure>
    <p class="weather-forecasts">
      {{ forecast.tempMin.toFixed(1) }} / {{ forecast.tempMax.toFixed(1) }}°C
    </p>
    <p class="weather-forecasts">{{ forecast.description }}</p>
  </div>
</template>

<script setup lang="ts">
import type { WeatherForecast } from "../types/weather";

//https://stackoverflow.com/questions/66590691/typescript-type-string-is-not-assignable-to-type-numeric-2-digit-in-d
const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "short",
  day: "2-digit",
  month: "2-digit",
};

defineProps<{
  forecast: WeatherForecast;
}>();
</script>
