<template>
  <div class="card w-full h-full bg-white shadow-xl">
    <div class="card-body p-0">
      <leaflet-comp
        :maxZoom="maxZoom"
        :zoom="zoom"
        :map-image="mapImage"
        ref="leafletRef"
      ></leaflet-comp>
    </div>
  </div>
</template>

<script setup lang="ts">
import LeafletComp from "@/components/Leaflet/LeafletComp.vue";
import type { MapImage } from "@/types/mapImage";
import { ref } from "vue";
import type L from "leaflet";

const leafletRef = ref<InstanceType<typeof LeafletComp> | null>(null);

defineProps<{
  maxZoom?: number;
  zoom?: number;
  mapImage: MapImage;
}>();

defineExpose({
  addMarker,
});

function addMarker(marker: L.Marker): void {
  leafletRef.value?.addMarker(marker);
}
</script>
