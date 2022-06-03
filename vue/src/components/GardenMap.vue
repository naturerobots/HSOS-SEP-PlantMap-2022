<!--everything in this comp is for testing only-->
<template>
  <base-map :map-image="mapImage" :zoom="20.5" ref="baseMapRef"></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/BaseMap.vue";
import type { MapImage } from "@/types/mapImage";
import L, { LatLng } from "leaflet";
import { ref, onMounted } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_left: new LatLng(52.31703002877383, 7.6307445019483575),
  top_right: new LatLng(52.316885520295315, 7.630280744986272),
  bottom_left: new LatLng(52.31721038577891, 7.630586922168733),
};

const sensorIcon: L.Icon = new L.Icon({
  iconUrl: "src/assets/marker/sensor_icon.svg",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});
onMounted(() => {
  addSensorMarker(new LatLng(52.31699002877383, 7.630380744986272));
  addSensorMarker(new LatLng(52.31700002877383, 7.630480744986272));
});

function addSensorMarker(latlng: L.LatLng) {
  let marker = L.marker(latlng, {
    icon: sensorIcon,
  });
  baseMapRef.value?.addMarker(marker);
}
</script>
