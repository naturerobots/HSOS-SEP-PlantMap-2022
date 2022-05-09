<template>
  <h1>Dashboard</h1>

  <!--Test for weather / can be removed-->
  {{ weather }}
</template>

<script setup lang="ts">
//####################################
//Test for weather / can be cleaned up
import { Ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { weatherStore } from "../stores/weatherStore";
import type { Weather } from "../types/weather";

const weather: Ref<Weather> = storeToRefs(weatherStore()).getWeather;

onMounted(() => {
  weatherStore().loadDataFromApi();
});
//####################################
</script>
