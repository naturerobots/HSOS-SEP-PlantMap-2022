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
import type { PropType } from "vue";

defineProps({
  maxZoom: {
    type: Number,
  },
  zoom: {
    type: Number,
  },
  mapImage: {
    type: Object as PropType<MapImage>,
    required: true,
  },
});
</script>
