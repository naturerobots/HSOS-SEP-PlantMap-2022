<!--everything in this comp is for testing only-->
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

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_left: new LatLng(52.31703002877383, 7.6307445019483575),
  top_right: new LatLng(52.316885520295315, 7.630280744986272),
  bottom_left: new LatLng(52.31721038577891, 7.630586922168733),
};

onMounted(() => {
  props.sensors.forEach(function (sensor) {
    addSensorMarker(sensor);
  });
});

function addSensorMarker(sensor: Sensor): void {
  let marker = L.marker(new LatLng(sensor.lat, sensor.lng), {
    icon: L.divIcon({
      html: '<div class="sensor-icon shadow-xl">' + sensor.name + "</div>",
    }),
  });
  markerMap.set(sensor.id, marker);
  baseMapRef.value?.addMarker(marker);
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

<style>
/*TODO: move to base.css */
.sensor-icon {
  width: 25px;
  height: 25px;
  line-height: 25px;
  border-radius: 50%;
  font-size: 10px;
  color: #000;
  text-align: center;
  background: #fff;
  margin-left: -12.5px;
  margin-top: -12.5px;
}

.sensor-icon:hover {
  background: #addb73;
}
</style>
