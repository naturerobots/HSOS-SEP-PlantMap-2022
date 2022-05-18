<!---
TODO: Create the date in the store or service. Must then also be changed in WeatherComp.
-->
<template>
  <div class="text-center">
    <h2 class="font-bold text-primary-focus">
      {{ forecast.dt.toLocaleString("de-DE", dateOptions) }}
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

//runtime declaration
//https://vuejs.org/guide/typescript/composition-api.html#typing-component-props
//https://frontendsociety.com/using-a-typescript-interfaces-and-types-as-a-prop-type-in-vuejs-508ab3f83480
//https://github.com/vuejs/vue/pull/6856
/*defineProps({
  forecast: {
    type: Object as PropType<WeatherForecast>,
    required: true,
  }
});*/

//type-based declaration
defineProps<{
  forecast: WeatherForecast;
}>();
</script>
