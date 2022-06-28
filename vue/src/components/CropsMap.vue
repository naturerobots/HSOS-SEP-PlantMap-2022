<!--everything in this comp is for testing only-->
<template>
  <base-map
    ref="baseMapRef"
    :map-image="mapImage"
    :zoom="20.5"
    :zoom-control="true"
    :map-interaction="false"
    @polygon-enter="polygonEnter"
    @polygon-leave="polygonLeave"
  ></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/BaseMap.vue";
import type { Crop } from "@/types/crop";
import type { MapImage } from "@/types/mapImage";
import L, { LatLng, polygon, Polygon } from "leaflet";
import { ref, onMounted } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const polygonMap: Map<number, L.Polygon<any>> = new Map();

const props = defineProps<{
  crops: Crop[];
}>();

const emit = defineEmits<{
  (event: "polygonEnter", cropsId: number): void;
  (event: "polygonLeave", cropsId: number): void;
}>();

defineExpose({
  setPolygonActive,
  setPolygonInactive,
});

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_right: new LatLng(52.31724604719058, 7.630553394556046),
  top_left: new LatLng(52.3170773725588, 7.630054503679276),
  bottom_left: new LatLng(52.31686606722232, 7.630242593586445),
};

onMounted(() => {
  props.crops.forEach(function (crop) {
    addCropsPolygon(crop);
  });
});

let lat1 = 52.317039789516954;
let lon1 = 7.630354102703116;
let lat2 = 52.316941166226066;
let lon2 = 7.630439482077206;
let lat3 = 52.31693439650253;
let lon3 = 7.630420101787746;
let lat4 = 52.317031328642415;
let lon4 = 7.630334734025543;
let offsetLat = 0.00001;
let offsetLon = 0.00003;

function addCropsPolygon(crop: Crop): void {
  let latlng: L.LatLng[] = [];
  latlng.push(new LatLng(lat1, lon1));
  latlng.push(new LatLng(lat2, lon2));
  latlng.push(new LatLng(lat3, lon3));
  latlng.push(new LatLng(lat4, lon4));
  lat1 += offsetLat;
  lat2 += offsetLat;
  lat3 += offsetLat;
  lat4 += offsetLat;
  lon1 += offsetLon;
  lon2 += offsetLon;
  lon3 += offsetLon;
  lon4 += offsetLon;
  let polygon: L.Polygon<any>;
  polygon = L.polygon(latlng, { color: "green", fillOpacity: 0 });
  polygon.on("mouseover", function () {
    polygon.setStyle({
      fillOpacity: 0.7,
    });
  });
  polygon.on("mouseout", function () {
    polygon.setStyle({
      fillOpacity: 0,
    });
  });
  baseMapRef.value?.addPolygon(polygon);
  polygonMap.set(crop.id, polygon);
}

function setPolygonActive(cropsId: number): void {
  const crop = getCropById(cropsId);
  if (crop) {
    if (polygonMap.has(cropsId)) {
      const polygon = polygonMap.get(cropsId);
      polygon?.setStyle({
        fillOpacity: 0.7,
      });
    }
  }
}

function getCropById(cropsId: number): Crop | undefined {
  for (let i = 0; i < props.crops.length; i++) {
    if (props.crops[i].id == cropsId) {
      return props.crops[i];
    }
  }
  return undefined;
}

function setPolygonInactive(cropsId: number): void {
  const crop = getCropById(cropsId);
  if (crop) {
    if (polygonMap.has(cropsId)) {
      const polygon = polygonMap.get(cropsId);
      polygon?.setStyle({
        fillOpacity: 0.0,
      });
    }
  }
}

function getIdByPolygon(polygon: L.Polygon<any>): number {
  for (let [key, value] of polygonMap.entries()) {
    if (value === polygon) return key;
  }
  return -1;
}

function polygonEnter(polygon: L.Polygon<any>): void {
  const cropsId: number = getIdByPolygon(polygon);
  if (cropsId != -1) {
    emit("polygonEnter", cropsId);
  }
}

function polygonLeave(polygon: L.Polygon<any>): void {
  const cropsId: number = getIdByPolygon(polygon);
  if (cropsId != -1) {
    emit("polygonLeave", cropsId);
  }
}
</script>
