<template>
  <div class="text-center">
    <h2 class="font-bold text-primary-focus">Di. 22.05.</h2>
    <figure>
      <img :src="`http://openweathermap.org/img/wn/${forecast.icon}@2x.png`" />
    </figure>
    <p class="weather-forecasts">
      {{ forecast.tempMin }} / {{ forecast.tempMax }}°C
    </p>
    <p class="weather-forecasts">{{ forecast.description }}</p>
  </div>
</template>

<script setup lang="ts">
import type { WeatherForecast } from "../types/weather";

defineProps<{
  forecast: WeatherForecast;
}>();
</script>
