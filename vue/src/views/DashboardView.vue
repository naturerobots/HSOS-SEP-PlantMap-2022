<template>
  <div class="flex-nowrap">
    <header-bar
      title="Dashboard"
      :widgetOptions="widgetOptionsDashboard"
      :storeOptions="storeOptions"
    ></header-bar>
    <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-6">
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
      <div v-if="storeOptions.indexOf('soil-parameter') > -1">
        <sensor-comp
          ref="sensorCompRef"
          :sensors="sensors"
          @row-enter="tableSensorEnter"
          @row-leave="tableSensorLeave"
        >
        </sensor-comp>
      </div>
    </div>
  </div>

  <!-- DEMO LAYOUTS -->
  <!-- <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <div>
      <div class="bg-gray-200 h-96 p-2">Weather</div>
    </div>
    <div class="col-span-3 row-span-2 order-last">
      <div class="bg-gray-200 h-96 p-2">Garden</div>
    </div>
    <div>
      <div class="bg-gray-200 h-full p-2">Sensor</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
  </div> -->

  <!-- <div class="grid grid-cols-3 gap-4 place-items-stretch h-fit p-3">
    <div>
      <div class="bg-gray-200 h-96 p-2">Weather</div>
    </div>
    <div>
      <div class="bg-gray-200 h-full p-2">Sensor</div>
    </div>
    <div class="col-span-1 row-span-2">
      <div class="bg-gray-200 h-full p-2">Garden</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
    <div>
      <div class="bg-gray-200 h-96 p-2">Custom</div>
    </div>
  </div> -->
</template>

<script setup lang="ts">
import { ref } from "vue";
import type { Ref } from "vue";
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
import SensorComp from "@/components/SensorCompQuasar.vue";
import GardenMap from "@/components/GardenMap.vue";
import HeaderBar from "@/components/header/HeaderBar.vue";

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
