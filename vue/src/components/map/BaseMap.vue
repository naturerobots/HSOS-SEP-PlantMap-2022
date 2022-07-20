<template>
  <div class="card-map w-full h-full select-none base-map">
    <leaflet-comp
      :maxZoom="maxZoom"
      :zoom="zoom"
      :map-image="mapImage"
      :zoom-control="zoomControl"
      :map-interaction="mapInteraction"
      ref="leafletRef"
    >
    </leaflet-comp>
  </div>
</template>

<script setup lang="ts">
import LeafletComp from "@/components/leaflet/LeafletComp.vue";
import type { MapImage } from "@/types/mapImage";
import { ref } from "vue";
import type L from "leaflet";
import type { LeafletEvent } from "leaflet";

const leafletRef = ref<InstanceType<typeof LeafletComp> | null>(null);

defineProps<{
  mapImage: MapImage;
  maxZoom?: number;
  zoom?: number;
  zoomControl?: boolean;
  mapInteraction?: boolean;
}>();

const emit = defineEmits<{
  (event: "markerClick", marker: L.Marker): void;
  (event: "markerEnter", marker: L.Marker): void;
  (event: "markerLeave", marker: L.Marker): void;
  (event: "polygonClick", polygon: L.Polygon): void;
  (event: "polygonEnter", polygon: L.Polygon): void;
  (event: "polygonLeave", polygon: L.Polygon): void;
}>();

defineExpose({
  addMarker,
  addPolygon,
});

function addMarker(marker: L.Marker): void {
  marker.on("click", emitMarkerClick);
  marker.on("mouseover", emitMarkerEnter);
  marker.on("mouseout", emitMarkerLeave);
  leafletRef.value?.addMarker(marker);
}

function addPolygon(polygon: L.Polygon): void {
  polygon.on("click", emitPolygonClick);
  polygon.on("mouseover", emitPolygonEnter);
  polygon.on("mouseout", emitPolygonLeave);
  leafletRef.value?.addPolygon(polygon);
}

function emitMarkerClick(event: LeafletEvent): void {
  const marker: L.Marker = event.target;
  emit("markerClick", marker);
}

function emitMarkerEnter(event: LeafletEvent): void {
  const marker: L.Marker = event.target;
  emit("markerEnter", marker);
}

function emitMarkerLeave(event: LeafletEvent): void {
  const marker: L.Marker = event.target;
  emit("markerLeave", marker);
}

function emitPolygonClick(event: LeafletEvent): void {
  const polygon: L.Polygon = event.target;
  emit("polygonClick", polygon);
}

function emitPolygonEnter(event: LeafletEvent): void {
  const polygon: L.Polygon = event.target;
  emit("polygonEnter", polygon);
}

function emitPolygonLeave(event: LeafletEvent): void {
  const polygon: L.Polygon = event.target;
  emit("polygonLeave", polygon);
}
</script>

<style>
.base-map {
  min-height: 600px; /* TODO: change css */
}
</style>