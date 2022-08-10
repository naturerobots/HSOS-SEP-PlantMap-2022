<template>
  <base-map
    ref="baseMapRef"
    :zoom="20.5"
    :zoom-control="true"
    :map-interaction="false"
    @marker-click="markerClick"
    @marker-enter="markerEnter"
    @marker-leave="markerLeave"
  ></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/map/BaseMap.vue";
import L, { LatLng } from "leaflet";
import { ref, onMounted, type Ref, watch } from "vue";
import type { Sensor } from "@/types/sensor";
import { gardenStore } from "@/stores/gardenStore";
import type { GardenImage } from "@/types/gardenImage";
import { storeToRefs } from "pinia";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const markerMap: Map<number, L.Marker> = new Map();

var gardenImage: Ref<{ image: GardenImage | undefined }> = storeToRefs(
  gardenStore()
).getGardenImage;

const props = defineProps<{
  sensors: Sensor[];
}>();

const emit = defineEmits<{
  (event: "sensorClick", sensorId: number): void;
  (event: "sensorEnter", sensorId: number): void;
  (event: "sensorLeave", sensorId: number): void;
}>();

defineExpose({
  setMarkerActive,
  setMarkerInactive,
});

onMounted(() => {
  props.sensors.forEach(function (sensor) {
    addSensorMarker(sensor);
  });

  if (gardenImage.value.image) {
    baseMapRef.value?.addGardenImage(gardenImage.value.image);
  }
});

watch(gardenImage.value, (updatedGardenImage) => {
  baseMapRef.value?.addGardenImage(gardenImage.value.image);
});

function addSensorMarker(sensor: Sensor): void {
  let marker = L.marker(new LatLng(sensor.lat, sensor.lng), {
    icon: L.divIcon({
      html:
        '<div class="sensor-icon hover:sensor-icon-active shadow-xl">' +
        sensor.name +
        "</div>",
    }),
  });
  markerMap.set(sensor.id, marker);
  baseMapRef.value?.addMarker(marker);
}

function setMarkerActive(sensorId: number): void {
  const sensor = getSensorById(sensorId);
  if (sensor) {
    if (markerMap.has(sensorId)) {
      const marker = markerMap.get(sensorId);
      marker?.setIcon(
        L.divIcon({
          html:
            '<div class="sensor-icon sensor-icon-active shadow-xl">' +
            sensor.name +
            "</div>",
        })
      );
    }
  }
}

function setMarkerInactive(sensorId: number): void {
  const sensor = getSensorById(sensorId);
  if (sensor) {
    if (markerMap.has(sensorId)) {
      const marker = markerMap.get(sensorId);
      marker?.setIcon(
        L.divIcon({
          html:
            '<div class="sensor-icon hover:sensor-icon-active shadow-xl">' +
            sensor.name +
            "</div>",
        })
      );
    }
  }
}

function getSensorById(sensorId: number): Sensor | undefined {
  for (let i = 0; i < props.sensors.length; i++) {
    if (props.sensors[i].id == sensorId) {
      return props.sensors[i];
    }
  }
  return undefined;
}

function getIdByMarker(marker: L.Marker): number {
  for (let [key, value] of markerMap.entries()) {
    if (value === marker) return key;
  }
  return -1;
}

function markerClick(marker: L.Marker): void {
  const sensorId: number = getIdByMarker(marker);
  if (sensorId != -1) {
    emit("sensorClick", sensorId);
  }
}

function markerEnter(marker: L.Marker): void {
  const sensorId: number = getIdByMarker(marker);
  if (sensorId != -1) {
    emit("sensorEnter", sensorId);
  }
}

function markerLeave(marker: L.Marker): void {
  const sensorId: number = getIdByMarker(marker);
  if (sensorId != -1) {
    emit("sensorLeave", sensorId);
  }
}
</script>
