<!--everything in this comp is for testing only-->
<template>
  <base-map
    ref="baseMapRef"
    :zoom="20.5"
    :zoom-control="true"
    :map-interaction="true"
  ></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/map/BaseMap.vue";
import { gardenStore } from "@/stores/gardenStore";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
import type { Crop } from "@/types/crop";
import type { GardenImage } from "@/types/gardenImage";
import type { MapImage } from "@/types/mapImage";
import type { Plants } from "@/types/plants";
import L, { LatLng, polygon, Polygon } from "leaflet";
import { storeToRefs } from "pinia";
import { ref, onMounted, type Ref, watch } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const markerMap: Map<number, L.Marker> = new Map();

var gardenImage: Ref<{ image: GardenImage | undefined }> = storeToRefs(
  gardenStore()
).getGardenImage;

const props = defineProps<{
  beds: Beds;
}>();

// const emit = defineEmits<{
//   (event: "sensorClick", sensorId: number): void;
//   (event: "sensorEnter", sensorId: number): void;
//   (event: "sensorLeave", sensorId: number): void;
// }>();

// defineExpose({
//   setPolygonActive,
//   setPolygonInactive,
//   setPolygonClicked,
// });

onMounted(() => {
  if (gardenImage.value.image) {
    baseMapRef.value?.addGardenImage(gardenImage.value.image);
  }

  if (props.beds.beds.length > 0) {
    props.beds.beds[props.beds.beds.length - 1].plant_coords.forEach(
      (value) => {
        addPlantMarker(value);
      }
    );
  }
});

watch(props.beds, () => {
  console.log("WATCHER");

  if (props.beds.beds.length > 0) {
    props.beds.beds[props.beds.beds.length - 1].plant_coords.forEach(
      (value) => {
        addPlantMarker(value);
      }
    );
  }
});

function addPlantMarker(latLng: L.LatLng): void {
  let marker = L.marker(latLng, {
    // icon: L.divIcon({
    // }),
  });
  //markerMap.set(crop.id, marker);
  baseMapRef.value?.addMarker(marker);
}

// function setMarkerActive(sensorId: number): void {
//   const sensor = getSensorById(sensorId);
//   if (sensor) {
//     if (markerMap.has(sensorId)) {
//       const marker = markerMap.get(sensorId);
//       marker?.setIcon(
//         L.divIcon({
//           html:
//             '<div class="sensor-icon sensor-icon-active shadow-xl">' +
//             sensor.name +
//             "</div>",
//         })
//       );
//     }
//   }
// }

// function setMarkerInactive(sensorId: number): void {
//   const sensor = getSensorById(sensorId);
//   if (sensor) {
//     if (markerMap.has(sensorId)) {
//       const marker = markerMap.get(sensorId);
//       marker?.setIcon(
//         L.divIcon({
//           html:
//             '<div class="sensor-icon hover:sensor-icon-active shadow-xl">' +
//             sensor.name +
//             "</div>",
//         })
//       );
//     }
//   }
// }

// function getSensorById(sensorId: number): Sensor | undefined {
//   for (let i = 0; i < props.sensors.length; i++) {
//     if (props.sensors[i].id == sensorId) {
//       return props.sensors[i];
//     }
//   }
//   return undefined;
// }

// function getIdByMarker(marker: L.Marker): number {
//   for (let [key, value] of markerMap.entries()) {
//     if (value === marker) return key;
//   }
//   return -1;
// }

// function markerClick(marker: L.Marker): void {
//   const sensorId: number = getIdByMarker(marker);
//   if (sensorId != -1) {
//     emit("sensorClick", sensorId);
//   }
// }

// function markerEnter(marker: L.Marker): void {
//   const sensorId: number = getIdByMarker(marker);
//   if (sensorId != -1) {
//     emit("sensorEnter", sensorId);
//   }
// }

// function markerLeave(marker: L.Marker): void {
//   const sensorId: number = getIdByMarker(marker);
//   if (sensorId != -1) {
//     emit("sensorLeave", sensorId);
//   }
//}

// let lat1 = 52.317039789516954;
// let lon1 = 7.630354102703116;
// let lat2 = 52.316941166226066;
// let lon2 = 7.630439482077206;
// let lat3 = 52.31693439650253;
// let lon3 = 7.630420101787746;
// let lat4 = 52.317031328642415;
// let lon4 = 7.630334734025543;
// let offsetLat = 0.00001;
// let offsetLon = 0.00003;

// function addCropsPolygon(crop: Crop): void {
//   let latlng: L.LatLng[] = [];
//   latlng.push(new LatLng(lat1, lon1));
//   latlng.push(new LatLng(lat2, lon2));
//   latlng.push(new LatLng(lat3, lon3));
//   latlng.push(new LatLng(lat4, lon4));
//   lat1 += offsetLat;
//   lat2 += offsetLat;
//   lat3 += offsetLat;
//   lat4 += offsetLat;
//   lon1 += offsetLon;
//   lon2 += offsetLon;
//   lon3 += offsetLon;
//   lon4 += offsetLon;

//   let polygon: L.Polygon<any>;
//   polygon = L.polygon(latlng, { color: "green", fillOpacity: 0 });
//   polygon.on("mouseover", function () {
//     if (polygon?.options.fillOpacity !== 1) {
//       polygon.setStyle({
//         fillOpacity: 0.7,
//       });
//     }
//   });
//   polygon.on("mouseout", function () {
//     if (polygon?.options.fillOpacity !== 1) {
//       polygon.setStyle({
//         fillOpacity: 0.0,
//       });
//     }
//   });
//   // polygon.on("click", function () {
//   //   polygon.setStyle({
//   //     fillOpacity: 1,
//   //   });
//   // });
//   baseMapRef.value?.addPolygon(polygon);
//   polygonMap.set(crop.id, polygon);
// }

// function setPolygonActive(cropsId: number): void {
//   removeActivePolygon();
//   const crop = getCropById(cropsId);
//   if (crop) {
//     if (polygonMap.has(cropsId)) {
//       const polygon = polygonMap.get(cropsId);
//       if (polygon?.options.fillOpacity !== 1) {
//         polygon?.setStyle({
//           fillOpacity: 0.7,
//         });
//       }
//     }
//   }
// }

// function removeClickedPolygon(): void {
//   console.log("removeClickedPolygon");
//   polygonMap.forEach((polygon) => {
//     if (polygon?.options.fillOpacity === 1) {
//       polygon?.setStyle({
//         fillOpacity: 0.0,
//       });
//     }
//   });
// }

// function removeActivePolygon(): void {
//   polygonMap.forEach((polygon) => {
//     if (polygon?.options.fillOpacity === 0.7) {
//       polygon?.setStyle({
//         fillOpacity: 0.0,
//       });
//     }
//   });
// }

// function setPolygonClicked(cropsId: number): void {
//   console.log("setPolygonClicked");
//   const crop = getCropById(cropsId);
//   if (crop) {
//     if (polygonMap.has(cropsId)) {
//       const polygon = polygonMap.get(cropsId);
//       if (polygon?.options.fillOpacity !== 1) {
//         removeClickedPolygon();
//         polygon?.setStyle({
//           fillOpacity: 1.0,
//         });
//       } else {
//         removeClickedPolygon();
//         polygon?.setStyle({
//           fillOpacity: 0.7,
//         });
//       }
//     }
//   }
// }

// function getCropById(cropsId: number): Bed | undefined {
//   for (let i = 0; i < props.beds.beds.length; i++) {
//     if (props.beds.beds[i].id == cropsId) {
//       return props.beds.beds[i];
//     }
//   }
//   return undefined;
// }

// function setPolygonInactive(cropsId: number): void {
//   const crop = getCropById(cropsId);
//   if (crop) {
//     if (polygonMap.has(cropsId)) {
//       const polygon = polygonMap.get(cropsId);
//       if (polygon?.options.fillOpacity !== 1) {
//         polygon?.setStyle({
//           fillOpacity: 0.0,
//         });
//       }
//     }
//   }
// }

// function getIdByPolygon(polygon: L.Polygon<any>): number {
//   for (let [key, value] of polygonMap.entries()) {
//     if (value === polygon) return key;
//   }
//   return -1;
// }

// function polygonEnter(polygon: L.Polygon<any>): void {
//   const cropsId: number = getIdByPolygon(polygon);
//   if (cropsId != -1) {
//     emit("polygonEnter", cropsId);
//   }
// }

// function polygonLeave(polygon: L.Polygon<any>): void {
//   const cropsId: number = getIdByPolygon(polygon);
//   if (cropsId != -1) {
//     emit("polygonLeave", cropsId);
//   }
// }

// function polygonClick(polygon: L.Polygon<any>): void {
//   console.log("polygonClick");
//   const cropsId: number = getIdByPolygon(polygon);
//   if (cropsId != -1) {
//     emit("polygonClick", cropsId);
//   }
// }
</script>
