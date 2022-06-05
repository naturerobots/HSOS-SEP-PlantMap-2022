<!---
TODO: Create the date in the store or service. Must then also be changed in WeatherComp.
-->
<template>
  <div class="text-center">
    <div class="text-weight-bold text-primary_hover">
      <!--TODO: Maybe move language and date options to settings?-->
      {{ forecast.dt.toLocaleString("de-DE", dateOptions) }}
    </div>
    <figure>
      <q-img
        :src="`http://openweathermap.org/img/wn/${forecast.icon}@2x.png`"
        style="width: 90px"
      />
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
