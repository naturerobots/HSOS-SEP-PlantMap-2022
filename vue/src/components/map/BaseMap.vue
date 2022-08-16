<template>
  <div class="card-map w-full h-full select-none base-map">
    <leaflet-comp
      :maxZoom="maxZoom"
      :zoom="zoom"
      :zoom-control="zoomControl"
      :map-interaction="mapInteraction"
      ref="leafletRef"
    >
    </leaflet-comp>
  </div>
</template>

<script setup lang="ts">
import LeafletComp from "@/components/leaflet/LeafletComp.vue";
import { ref } from "vue";
import type L from "leaflet";
import type { LeafletEvent } from "leaflet";
import type { GardenImage } from "@/types/gardenImage";
const leafletRef = ref<InstanceType<typeof LeafletComp> | null>(null);

defineProps<{
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
  addLayerGroup,
  removeLayerGroup,
  addEventsToMarker,
  addPolygon,
  addGardenImage,
});

function addMarker(marker: L.Marker): void {
  marker.on("click", emitMarkerClick);
  marker.on("mouseover", emitMarkerEnter);
  marker.on("mouseout", emitMarkerLeave);
  leafletRef.value?.addMarker(marker);
}

function addLayerGroup(
  markers: L.LayerGroup,
  topRight: L.LatLng | undefined,
  bottomLeft: L.LatLng | undefined
): void {
  markers.eachLayer(function (layer: any) {
    layer.on("click", emitMarkerClick);
    layer.on("mouseover", emitMarkerEnter);
    layer.on("mouseout", emitMarkerLeave);
  });

  leafletRef.value?.addLayerGroup(markers, topRight, bottomLeft);
}

function removeLayerGroup(markers: L.LayerGroup): void {
  leafletRef.value?.removeLayerGroup(markers);
}

function addEventsToMarker(marker: L.Marker): void {
  marker.on("click", emitMarkerClick);
  marker.on("mouseover", emitMarkerEnter);
  marker.on("mouseout", emitMarkerLeave);
}

function addPolygon(polygon: L.Polygon): void {
  polygon.on("click", emitPolygonClick);
  polygon.on("mouseover", emitPolygonEnter);
  polygon.on("mouseout", emitPolygonLeave);
  leafletRef.value?.addPolygon(polygon);
}

function addGardenImage(gardenImage: GardenImage | undefined): void {
  if (!gardenImage) throw new Error("Garden Image should not be undefined");

  leafletRef.value?.addGardenImage(gardenImage);
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
