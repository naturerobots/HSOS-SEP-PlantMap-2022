<template>
  <base-layout
    title="Dashboard"
    :widgetOptions="widgetOptionsDashboard"
    :storeOptions="storeOptions"
  >
    <div
      v-if="storeToRefs(gardenStore()).getGardens.value.length > 0"
      class="grow grid grid-cols-3 gap-4 place-items-stretch p-6 w-full h-fit"
    >
      <div v-if="storeOptions.indexOf('weather') > -1">
        <weather-comp></weather-comp>
      </div>
      <div
        v-if="storeOptions.indexOf('garden-map') > -1"
        class="col-span-2 row-span-2"
      >
        <div class="h-full">
          <garden-map
            ref="gardenMapRef"
            :sensors="sensors"
            @sensor-enter="mapSensorEnter"
            @sensor-leave="mapSensorLeave"
          ></garden-map>
        </div>
      </div>
      <div
        v-if="sensors.length > 0 && storeOptions.indexOf('soil-parameter') > -1"
      >
        <sensor-comp
          ref="sensorCompRef"
          :sensors="sensors"
          @row-enter="tableSensorEnter"
          @row-leave="tableSensorLeave"
        >
        </sensor-comp>
      </div>
    </div>
    <div v-else>
      <h6>You don't have any gardens.</h6>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import { storeToRefs } from "pinia";
import { sensorStore } from "@/stores/sensorStore";
import { userStore } from "@/stores/userStore";
import { gardenStore } from "@/stores/gardenStore";
import type { Sensor } from "@/types/sensor";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import WeatherComp from "@/components/weather/WeatherComp.vue";
import SensorComp from "@/components/sensor/SensorComp.vue";
import GardenMap from "@/components/map/GardenMap.vue";
import BaseLayout from "@/components/layout/BaseLayout.vue";

const sensors: Ref<Sensor[]> = storeToRefs(sensorStore()).getSensors;
const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const gardenMapRef = ref<InstanceType<typeof GardenMap> | null>(null);
const sensorCompRef = ref<InstanceType<typeof SensorComp> | null>(null);
const widgetOptionsDashboard: WidgetOption[] = [
  widgetOptions.weather,
  widgetOptions.soilParameter,
  widgetOptions.gardenMap,
  widgetOptions.notification,
];

// Sensor - Map interaction
function mapSensorEnter(sensorId: number): void {
  sensorCompRef.value?.setRowActive(sensorId);
}

function mapSensorLeave(sensorId: number): void {
  sensorCompRef.value?.setRowInactive(sensorId);
}

function tableSensorEnter(sensorId: number): void {
  gardenMapRef.value?.setMarkerActive(sensorId);
}

function tableSensorLeave(sensorId: number): void {
  gardenMapRef.value?.setMarkerInactive(sensorId);
}
</script>
