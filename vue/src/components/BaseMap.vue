<template>
  <div class="card w-full h-full bg-white shadow-xl">
    <div class="card-body p-0">
      <leaflet-comp
        :maxZoom="maxZoom"
        :zoom="zoom"
        :map-image="mapImage"
      ></leaflet-comp>
    </div>
  </div>
</template>

<script setup lang="ts">
import LeafletComp from "@/components/Leaflet/LeafletComp.vue";
import type { MapImage } from "@/types/mapImage";

defineProps<{
  maxZoom?: number
  zoom?: number
  mapImage: MapImage
}>();
</script>
