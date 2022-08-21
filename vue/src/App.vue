<template>
  <router-view></router-view>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { weatherDataStore } from "@/stores/weatherDataStore";
import { sensorStore } from "@/stores/sensorStore";
import { cropsStore } from "./stores/cropsStore";

onMounted(() => {
  sensorStore().loadDataFromApi();
});
</script>
