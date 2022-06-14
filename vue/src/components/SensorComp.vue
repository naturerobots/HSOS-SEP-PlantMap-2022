<template>
  <div class="card h-full w-full drop-shadow bg-white">
    <div class="card-body p-5">
      <h2 class="text-base text-center text-primary-focus">Soil parameters</h2>
      <div class="grid grid-cols-3 gap-3">
        <div :key="sensor.id" v-for="sensor in sensors">
          <sensor-status :sensor="sensor"></sensor-status>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SensorStatus from "@/components/SensorStatus.vue";
import type { Sensor } from "@/types/sensor";

defineProps<{
  sensors: Sensor[];
}>();
</script>
