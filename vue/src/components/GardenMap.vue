<!--image is for testing only-->
<template>
  <base-map
    :map-image="mapImage"
    :zoom="20.5"
    ref="baseMapRef"
    @marker-click="markerClick"
    @marker-enter="markerEnter"
    @marker-leave="markerLeave"
  ></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/BaseMap.vue";
import type { MapImage } from "@/types/mapImage";
import L, { LatLng } from "leaflet";
import { ref, onMounted } from "vue";
import type { Sensor } from "@/types/sensor";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const markerMap: Map<number, L.Marker> = new Map();

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

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_right: new LatLng(52.31724604719058, 7.630553394556046),
  top_left: new LatLng(52.3170773725588, 7.630054503679276),
  bottom_left: new LatLng(52.31686606722232, 7.630242593586445),
};

onMounted(() => {
  props.sensors.forEach(function (sensor) {
    addSensorMarker(sensor);
  });
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
