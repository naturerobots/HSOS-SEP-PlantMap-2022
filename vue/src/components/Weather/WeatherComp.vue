<!---
TODO: If no weather information is available because the API is not accessible or the location cannot be found,
the component should be extended to include a message indicating that no weather data is available.
-->

<template>
  <div
    v-if="Object.keys(current).length > 0 && Object.keys(forecast).length > 0"
    class="card h-full w-full shadow-sm bg-[#fdfff9]"
  >
    <div class="card-body p-5">
      <h2 class="text-xl text-center text-primary-focus">
        Wetter {{ current.name }}
      </h2>
      <div class="card card-side">
        <figure>
          <img
            :src="`http://openweathermap.org/img/wn/${current.weather[0].icon}@2x.png`"
          />
        </figure>
        <div class="card-body">
          <h2 class="font-bold text-primary-focus">
            <!--TODO: Maybe move language and date options to settings?-->
            {{
              new Date(current.dt * 1000).toLocaleString("de-DE", dateOptions)
            }}
          </h2>
          <p class="mt-2 text-primary-focus text-2xl">
            {{ forecast.daily[0].temp.min.toFixed(1) }} /
            {{ forecast.daily[0].temp.max.toFixed(1) }}°C
          </p>
          <p class="mt-2 text-primary-focus">
            {{ current.weather[0].description }}
          </p>
        </div>
      </div>
      <div class="grid grid-cols-3 mt-5">
        <!-- TODO: slice parameters could be added to later settings -->
        <div
          :key="forecastDaily.dt"
          v-for="forecastDaily in forecast.daily.slice(1, 4)"
        >
          <weather-forecast :forecast="forecastDaily"></weather-forecast>
        </div>
      </div>
    </div>
    <!-- <test-line-chart></test-line-chart> -->
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { weatherDataStore } from "@/stores/weatherDataStore";
import WeatherForecast from "@/components/Weather/WeatherForecast.vue";

//const weather: Ref<Weather> = storeToRefs(weatherStore()).getWeather;
const { initialised, current, forecast } = storeToRefs(weatherDataStore());

const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "long",
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
};
</script>
