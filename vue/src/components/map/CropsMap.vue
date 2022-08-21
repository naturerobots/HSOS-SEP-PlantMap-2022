<!--everything in this comp is for testing only-->
<template>
  <base-map
    ref="baseMapRef"
    :zoom="20.5"
    :zoom-control="true"
    :map-interaction="true"
    @marker-click="markerClick"
    @marker-enter="markerEnter"
    @marker-leave="markerLeave"
  >
  </base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/map/BaseMap.vue";
import { gardenStore } from "@/stores/gardenStore";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
import type { Crop } from "@/types/crop";
import type { GardenImage } from "@/types/gardenImage";
import type { Crops } from "@/types/crops";
import L from "leaflet";
import { storeToRefs } from "pinia";
import { ref, onMounted, type Ref, watch } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const bedMarkerMap: Map<number, L.Marker> = new Map();
const cropMarkerMap: Map<string, L.Marker> = new Map();

const bedMarkers = L.layerGroup();
const cropMarkers = L.layerGroup();

const greenIcon: L.Icon = new L.Icon({
  iconUrl: "src/assets/marker/marker_green.svg",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

var gardenImage: Ref<{ image: GardenImage | undefined }> = storeToRefs(
  gardenStore()
).getGardenImage;

const props = defineProps<{
  beds: Beds;
  crops: Crops;
}>();

const emit = defineEmits<{
  (event: "bedClick", bedId: number): void;
  (event: "bedEnter", bedId: number): void;
  (event: "bedLeave", bedId: number): void;

  (event: "cropEnter", cropId: string): void;
  (event: "cropLeave", cropId: string): void;
}>();

let showCrops = false;

onMounted(() => {
  if (gardenImage.value.image) {
    baseMapRef.value?.addGardenImage(gardenImage.value.image);
  }

  if (props.beds.bedList.length > 0) {
    props.beds.bedList.forEach((bed) => {
      addBedMarker(bed);
    });
  }

  baseMapRef.value?.addLayerGroup(bedMarkers, undefined, undefined);
});

watch(props.beds, () => {
  if (props.beds.bedList.length === 0) return;

  const bed = props.beds.bedList[props.beds.bedList.length - 1];

  let marker = addBedMarker(bed);
  if (marker) baseMapRef.value?.addEventsToMarker(marker);
});

watch(props.crops, () => {
  if (props.crops.plants.length === 0) {
    baseMapRef.value?.removeLayerGroup(cropMarkers);
    baseMapRef.value?.addLayerGroup(bedMarkers, undefined, undefined);

    cropMarkers.clearLayers();
    cropMarkerMap.clear();

    showCrops = false;

    return;
  }

  baseMapRef.value?.removeLayerGroup(bedMarkers);

  props.crops.plants.forEach((crop: Crop) => {
    addCropMarker(crop);
  });

  showCrops = true;

  baseMapRef.value?.addLayerGroup(cropMarkers, undefined, undefined);
});

function addBedMarker(bed: Bed): L.Marker | undefined {
  if (bedMarkerMap.has(bed.id)) return undefined;

  const coords = new L.LatLng(bed.avg_plant_lat, bed.avg_plant_lon);
  const marker = L.marker(coords, {
    icon: greenIcon,
  });
  bedMarkerMap.set(bed.id, marker);
  bedMarkers.addLayer(marker);

  return marker;
}

function addCropMarker(crop: Crop): L.Marker | undefined {
  if (cropMarkerMap.has(crop.id)) return undefined;

  const coords = new L.LatLng(crop.plant_coords.lat, crop.plant_coords.lon);
  const marker = L.marker(coords, {
    icon: greenIcon,
  });

  cropMarkerMap.set(crop.id, marker);
  cropMarkers.addLayer(marker);

  return marker;
}

function markerClick(marker: L.Marker): void {
  const bedId: number | undefined = getBedIdByMarker(marker);
  if (bedId) {
    emit("bedClick", bedId);
  }
}

function markerEnter(marker: L.Marker): void {
  if (showCrops) {
    const id: string | undefined = getCropIdByMarker(marker);
    if (id) {
      emit("cropEnter", id);
    }
  } else {
    const id: number | undefined = getBedIdByMarker(marker);
    if (id) {
      emit("bedEnter", id);
    }
  }
}

function markerLeave(marker: L.Marker): void {
  if (showCrops) {
    const id: string | undefined = getCropIdByMarker(marker);
    if (id) {
      emit("cropLeave", id);
    }
  } else {
    const id: number | undefined = getBedIdByMarker(marker);
    if (id) {
      emit("bedLeave", id);
    }
  }
}

function getBedIdByMarker(marker: L.Marker): number | undefined {
  for (let [key, value] of bedMarkerMap.entries()) {
    if (value === marker) {
      console.log(key);
      return key;
    }
  }
  return undefined;
}

function getCropIdByMarker(marker: L.Marker): string | undefined {
  for (let [key, value] of cropMarkerMap.entries()) {
    if (value === marker) {
      console.log(key);
      return key;
    }
  }
  return undefined;
}
</script>
