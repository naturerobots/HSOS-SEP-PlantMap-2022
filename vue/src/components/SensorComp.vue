<template>
  <div class="card h-full w-full drop-shadow bg-white">
    <div class="card-body p-5">
      <h2 class="text-base text-center text-primary_hover">Soil parameters</h2>
      <div class="grid grid-cols-3 gap-3">
        <div :key="sensor.id" v-for="sensor in sensors">
          <sensor-status :sensor="sensor"></sensor-status>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { sensorStore } from "@/stores/sensorStore";
import SensorStatus from "@/components/SensorStatus.vue";

import type { Ref } from "vue";
import type { Sensor } from "@/types/sensor";

const sensors: Ref<Sensor[]> = storeToRefs(sensorStore()).getSensors;
</script>
