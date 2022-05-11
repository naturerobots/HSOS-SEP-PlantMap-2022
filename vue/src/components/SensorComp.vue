<template>
  <div class="card w-96 bg-light shadow-xl m-2">
    <div class="card-body px-2 py-3">
      <h2 class="text-base text-center text-primary-focus">Soil parameters</h2>
      <div class="grid grid-cols-3 gap-3">
        <sensor-status
          sensorName="Sensor A"
          moisture="100"
          temp="20"
          ec="400"
          :icons="[upGreen, downGreen, upRed]"
        ></sensor-status>
        <sensor-status
          sensorName="Sensor B"
          moisture="15"
          temp="5"
          ec="99"
          :icons="[downGreen, downGreen, upRed]"
        ></sensor-status>
        <sensor-status
          sensorName="Sensor C"
          moisture="34"
          temp="-3"
          ec="3"
          :icons="[upRed, upRed, upGreen]"
        ></sensor-status>
        <sensor-status
          sensorName="Sensor D"
          moisture="5"
          temp="100"
          ec="122"
          :icons="[upRed, upGreen, downGreen]"
        ></sensor-status>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SensorStatus from "@/components/SensorStatus.vue";

//icons for testing
const upGreen = "up_green";
const downGreen = "down_green";
const upRed = "up_red";
const downRed = "down_red";
</script>
