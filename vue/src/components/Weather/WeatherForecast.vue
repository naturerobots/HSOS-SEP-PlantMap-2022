<template>
  <div class="text-center">
    <h2 class="font-bold text-primary-focus">
      <!--TODO: Maybe move language and date options to settings?-->
      {{ new Date(forecast.dt * 1000).toLocaleString("de-DE", dateOptions) }}
    </h2>
    <figure>
      <img
        :src="`http://openweathermap.org/img/wn/${forecast.weather[0].icon}@2x.png`"
      />
    </figure>
    <p class="weather-forecasts">
      {{ forecast.temp.min.toFixed(1) }} / {{ forecast.temp.max.toFixed(1) }}°C
    </p>
    <p class="weather-forecasts">{{ forecast.weather[0].description }}</p>
  </div>
</template>

<script setup lang="ts">
import type { Daily } from "@/types/weatherData";

//type-based declaration
defineProps<{
  forecast: Daily;
}>();

//https://stackoverflow.com/questions/66590691/typescript-type-string-is-not-assignable-to-type-numeric-2-digit-in-d
const dateOptions: Intl.DateTimeFormatOptions = {
  weekday: "short",
  day: "2-digit",
  month: "2-digit",
};
</script>

<!--
//runtime declaration of props
//https://vuejs.org/guide/typescript/composition-api.html#typing-component-props
//https://frontendsociety.com/using-a-typescript-interfaces-and-types-as-a-prop-type-in-vuejs-508ab3f83480
//https://github.com/vuejs/vue/pull/6856
defineProps({
  forecast: {
    type: Object as PropType<WeatherForecast>,
    required: true,
  }
});
-->
