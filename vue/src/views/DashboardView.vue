<template>
  <base-layout
    title="Dashboard"
    :widgetOptions="widgetOptionsDashboard"
    :storeOptions="storeOptions"
  >
    <div
      class="p-6 dashboard-grid"
      :class="{ 'grid-flow-row': !gardenMapComputed }"
    >
      <div v-if="weatherComputed">
        <weather-comp></weather-comp>
      </div>
      <div v-if="soilParameterComputed">
        <sensor-comp
          ref="sensorCompRef"
          :sensors="sensors"
          @row-enter="tableSensorEnter"
          @row-leave="tableSensorLeave"
        >
        </sensor-comp>
      </div>
      <div v-if="gardenMapComputed" class="row-span-2 col-span-2">
        <garden-map
          ref="gardenMapRef"
          :sensors="sensors"
          @sensor-enter="mapSensorEnter"
          @sensor-leave="mapSensorLeave"
        >
        </garden-map>
      </div>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import { ref, computed, type Ref } from "vue";
import { storeToRefs } from "pinia";
import { sensorStore } from "@/stores/sensorStore";
import { userStore } from "@/stores/userStore";
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

const weatherComputed = computed(
  () => storeOptions.value.indexOf("weather") > -1
);
const soilParameterComputed = computed(
  () => storeOptions.value.indexOf("soil-parameter") > -1
);
const gardenMapComputed = computed(
  () => storeOptions.value.indexOf("garden-map") > -1
);

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

<style>
.dashboard-grid {
  display: grid;
  gap: 1.5rem;

  grid-template-columns: repeat(
    auto-fill,
    minmax(calc(100% / 2 - 1.5rem), 1fr)
  );
  grid-template-rows: repeat(auto-fill, minmax(calc(100% / 2 - 1.5rem), 1fr));

  grid-auto-flow: row;

  height: 100%;
}

@media screen and (min-width: 1350px) {
  .dashboard-grid {
    grid-auto-flow: column;
    grid-template-columns: repeat(
      auto-fill,
      minmax(calc(100% / 3 - 1.5rem), 1fr)
    );
    grid-template-rows: repeat(auto-fill, minmax(calc(100% / 2 - 1.5rem), 1fr));
  }
}
</style>
