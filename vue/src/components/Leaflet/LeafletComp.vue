<template>
  <div class="map-container w-full h-full absolute">
    <div id="map"></div>
  </div>
</template>

<script setup lang="ts">
import "leaflet/dist/leaflet.css";
import { onMounted, type PropType } from "vue";
import L from "leaflet";
import "./LeafletRotation.ts";
import type { MapImage } from "@/types/mapImage";

let leafletMap = {} as L.Map;

const props = defineProps({
  maxZoom: {
    type: Number,
    default: 24,
  },
  zoom: {
    type: Number,
    default: 13,
  },
  mapImage: {
    type: Object as PropType<MapImage>,
  },
});

onMounted(() => {
  leafletMap = L.map("map", {
    zoomControl: false,
    attributionControl: false,
    zoomDelta: 0.25,
    zoomSnap: 0.25,
  });

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxNativeZoom: 18,
    maxZoom: props.maxZoom,
  }).addTo(leafletMap);

  if (props.mapImage) {
    let overlay = L.imageOverlay.rotated(
      props.mapImage.src,
      props.mapImage.top_left,
      props.mapImage.top_right,
      props.mapImage.bottom_left,
      {
        opacity: 1,
      }
    );

    leafletMap.addLayer(overlay);
    const bounds = L.latLngBounds(
      props.mapImage.bottom_left,
      props.mapImage.top_right
    );

    var point = L.point(0, 0);
    leafletMap.fitBounds(bounds, { animate: false, padding: point });
  }
});
</script>

<style>
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100% !important;
  height: 100% !important;
}
</style>
