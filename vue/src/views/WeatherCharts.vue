<template>
  <h1>Weather Charts</h1>
  <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <chart-rain-pop></chart-rain-pop>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { weatherStore } from "../stores/weatherStore";

import ChartRainPop from "@/components/Weather/ChartRainPop.vue";

onMounted(() => {
  weatherStore().loadDataFromApi();
});
</script>
