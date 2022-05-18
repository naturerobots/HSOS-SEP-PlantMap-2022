<!---
TODO: hover effect
FIXME: fix template string for img src -> "@/" doesnt worked in first attempt
--->
<template>
  <h2 class="text-center text-primary-focus">
    {{ sensor.name }}
  </h2>

  <div class="text-sm">
    <div class="flex items-center">
      <div class="flex-none w-16">Moisture</div>
      <div class="flex-none w-8 text-right ml-1">
        {{ sensor.moisture_value }}%
      </div>
      <div class="flex-none ml-1">
        <img
          :src="`src/assets/icons/triangle_small_${sensor.moisture_trend}.svg`"
        />
      </div>
    </div>

    <div class="flex items-center">
      <div class="flex-none w-12">Temp</div>
      <div class="flex-none w-12 text-right ml-1">
        {{ sensor.temp_value }}°C
      </div>
      <div class="flex-none ml-1">
        <img
          :src="`src/assets/icons/triangle_small_${sensor.temp_trend}.svg`"
        />
      </div>
    </div>

    <div class="flex items-center">
      <div class="flex-none w-12">EC</div>
      <div class="flex-none w-12 text-right ml-1">{{ sensor.ec_value }}mS</div>
      <div class="flex-none ml-1">
        <img :src="`src/assets/icons/triangle_small_${sensor.ec_trend}.svg`" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Sensor } from "@/types/sensor";

defineProps<{
  sensor: Sensor;
}>();
</script>
