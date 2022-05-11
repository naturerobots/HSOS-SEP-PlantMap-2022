<!---
TODO: hover effect
--->
<template>
  <div>
    <h2 class="text-center text-primary-focus">
      {{ sensorName }}
    </h2>

    <div class="text-sm">
      <div class="flex items-center">
        <div class="flex-none w-16">Moisture</div>
        <div class="flex-none w-8 text-right ml-1">{{ moisture }}%</div>
        <div class="flex-none ml-1">
          {{ icons }}
          <img src="@/assets/icons/triangle_small_up_green.svg" />
        </div>
      </div>

      <div class="flex items-center">
        <div class="flex-none w-12">Temp</div>
        <div class="flex-none w-12 text-right ml-1">{{ temp }}°C</div>
        <div class="flex-none ml-1">
          <img class="" src="@/assets/icons/triangle_small_down_red.svg" />
        </div>
      </div>

      <div class="flex items-center">
        <div class="flex-none w-12">EC</div>
        <div class="flex-none w-12 text-right ml-1">{{ ec }}mS</div>
        <div class="flex-none ml-1">
          <img class="" src="@/assets/icons/triangle_small_down_green.svg" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
//Props for testing
defineProps<{
  sensorName: string;
  moisture: string;
  temp: string;
  ec: string;
  icons: string[];
}>();
</script>
