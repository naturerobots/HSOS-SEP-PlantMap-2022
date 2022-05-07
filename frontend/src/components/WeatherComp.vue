<!---
TODO: If no weather information is available because the API is not accessible or the location cannot be found,
the component should be extended to include a message indicating that no weather data is available.

TODO: date needs to be formatted and added -> https://coderrocketfuel.com/article/convert-a-unix-timestamp-to-a-date-in-vanilla-javascript
-->

<template>
  <div v-if="weather.forecast" class="card w-96 shadow-xl m-2">
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">
        Wetter {{ weather.current.name }}
      </h2>
      <div class="card card-side">
        <!-- <font-awesome-icon icon="fa-solid fa-cloud-hail-mixed" /> -->
        <figure>
          <img
            :src="`http://openweathermap.org/img/wn/${weather.current.icon}@2x.png`"
          />
        </figure>
        <div class="card-body">
          <h2 class="font-bold text-primary-focus">Montag, 21.05.2022</h2>
          <p class="mt-2 text-primary-focus text-2xl">
            {{ weather.current.tempMin }} / {{ weather.current.tempMax }}°C
          </p>
          <p class="mt-2 text-primary-focus">
            {{ weather.current.description }}
          </p>
        </div>
      </div>
      <!-- <div class="grid grid-cols-5 mt-5">
        <div class="col-span-2">
          <figure>
          <img src="http://openweathermap.org/img/wn/10d@2x.png" />
        </figure>
        </div>
        <div class="col-span-3">
          <h2 class="font-bold text-primary-focus">Montag, 21.05.2022</h2>
          <p class="mt-2 text-primary-focus text-2xl">3 / 6°C</p>
          <p class="mt-2 text-primary-focus">leichter Regen</p>
        </div>
      </div> -->
      <div class="grid grid-cols-3 mt-5">
        <weather-forecast :forecast="weather.forecast[0]"></weather-forecast>
        <weather-forecast :forecast="weather.forecast[1]"></weather-forecast>
        <weather-forecast :forecast="weather.forecast[2]"></weather-forecast>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
//####################################
//Test for weather / can be cleaned up
import type { Ref } from "vue";

import { storeToRefs } from "pinia";
import { weatherStore } from "../stores/weatherStore";
import type { Weather } from "../types/weather";

import WeatherForecast from "@/components/WeatherForecast.vue";

const weather: Ref<Weather> = storeToRefs(weatherStore()).getWeather;
//####################################
</script>
