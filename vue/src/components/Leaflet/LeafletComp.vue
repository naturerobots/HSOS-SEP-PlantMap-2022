<template>
  <div style="height: 539px; width: 200px">
    <l-map
      v-model="zoom"
      v-model:zoom="zoom"
      :center="center"
      :options="{ zoomControl: false }"
    >
      <!-- [52.317628, 7.63112] -->
      <l-image-overlay
        url="src/assets/img/demo_image.png"
        :bounds="bounds"
      ></l-image-overlay>
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="satellite"
        name="OpenStreetMap"
      ></l-tile-layer>

      <l-marker :lat-lng="[52.317206461376706, 7.630606037986071]"> </l-marker>
      <!-- Oben Links -->
      <l-marker :lat-lng="[52.31704187031269, 7.6307588913140405]"> </l-marker>
      <!-- Oben Rechts -->
      <l-marker :lat-lng="[52.31705535218097, 7.630129751278906]"> </l-marker>
      <!-- Unten Links -->
      <l-marker :lat-lng="[52.31688241444382, 7.630275079858925]"> </l-marker>
      <!-- Unten Rechts -->
    </l-map>
  </div>
</template>
<script setup lang="ts">
import {
  LMap,
  LTileLayer,
  LMarker,
  LImageOverlay,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";

const bounds = [
  [52.31705535218097, 7.630129751278906],
  [52.317206461376706, 7.630606037986071],
  [52.31704187031269, 7.6307588913140405],
  [
    52.31688241444382, 7.630275079858925,
  ] /* [52.317118, 7.630613],[52.318119, 7.631614] */,
];
const center = [
  (bounds[0][0] + bounds[1][0]) / 2,
  (bounds[0][1] + bounds[1][1]) / 2,
];

const zoom = 20;
</script>
