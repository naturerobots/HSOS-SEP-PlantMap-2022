<!---
TODO: If no weather information is available because the API is not accessible or the location cannot be found,
the component should be extended to include a message indicating that no weather data is available.
-->

<template>
  <div class="card shadow-1 bg-white p-4" v-if="weather.forecast">
    <div class="card-title text-h6">Wetter {{ weather.current.name }}</div>
    <q-card-section>
      <div class="row q-mt-lg">
        <div class="col-4">
          <figure>
            <img
              :src="`http://openweathermap.org/img/wn/${weather.current.icon}@2x.png`"
            />
          </figure>
        </div>
        <div class="col-8">
          <div class="text-xl font-bold text-primary_hover">
            <!--TODO: Maybe move language and date options to settings?-->
            {{ weather.current.dt.toLocaleString("de-DE", dateOptions) }}
          </div>
          <p class="q-mt-sm text-primary_hover text-subtitle1">
            {{ weather.current.tempMin.toFixed(1) }} /
            {{ weather.current.tempMax.toFixed(1) }}°C
          </p>
          <p class="q-mt-sm text-primary_hover text-subtitle1">
            {{ weather.current.description }}
          </p>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <div class="grid grid-cols-3 mt-5">
        <!--TODO: slice parameters could be added to later settings -->
        <div
          :key="forecast.dt.getDate"
          v-for="forecast in weather.forecast.slice(1, 4)"
        >
          <weather-forecast :forecast="forecast"></weather-forecast>
        </div>
      </div>
    </q-card-section>
  </div>
</template>

<script setup lang="ts">
//####################################
//Test for weather / can be cleaned up
import type { Ref } from "vue";
import type { Weather } from "../types/weather";
import { storeToRefs } from "pinia";
import { weatherStore } from "../stores/weatherStore";
import WeatherForecast from "@/components/WeatherForecast.vue";

const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "long",
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
};

const weather: Ref<Weather> = storeToRefs(weatherStore()).getWeather;
//####################################
</script>
