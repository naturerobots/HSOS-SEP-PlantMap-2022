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
    @polygon-click="polygonClick"
  ></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/map/BaseMap.vue";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
import type { Crop } from "@/types/crop";
import type { MapImage } from "@/types/mapImage";
import L, { LatLng, polygon, Polygon } from "leaflet";
import { ref, onMounted } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);
const polygonMap: Map<number, L.Polygon<any>> = new Map();

const props = defineProps<{
  beds: Beds;
}>();

const emit = defineEmits<{
  (event: "polygonEnter", cropsId: number): void;
  (event: "polygonLeave", cropsId: number): void;
  (event: "polygonClick", cropsId: number): void;
}>();

defineExpose({
  setPolygonActive,
  setPolygonInactive,
  setPolygonClicked,
});

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_right: new LatLng(52.31724604719058, 7.630553394556046),
  top_left: new LatLng(52.3170773725588, 7.630054503679276),
  bottom_left: new LatLng(52.31686606722232, 7.630242593586445),
};

onMounted(() => {
  props.beds.beds.forEach(function (crop) {
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
    if (polygon?.options.fillOpacity !== 1) {
      polygon.setStyle({
        fillOpacity: 0.7,
      });
    }
  });
  polygon.on("mouseout", function () {
    if (polygon?.options.fillOpacity !== 1) {
      polygon.setStyle({
        fillOpacity: 0.0,
      });
    }
  });
  // polygon.on("click", function () {
  //   polygon.setStyle({
  //     fillOpacity: 1,
  //   });
  // });
  baseMapRef.value?.addPolygon(polygon);
  polygonMap.set(crop.id, polygon);
}

function setPolygonActive(cropsId: number): void {
  removeActivePolygon();
  const crop = getCropById(cropsId);
  if (crop) {
    if (polygonMap.has(cropsId)) {
      const polygon = polygonMap.get(cropsId);
      if (polygon?.options.fillOpacity !== 1) {
        polygon?.setStyle({
          fillOpacity: 0.7,
        });
      }
    }
  }
}

function removeClickedPolygon(): void {
  console.log("removeClickedPolygon");
  polygonMap.forEach((polygon) => {
    if (polygon?.options.fillOpacity === 1) {
      polygon?.setStyle({
        fillOpacity: 0.0,
      });
    }
  });
}

function removeActivePolygon(): void {
  polygonMap.forEach((polygon) => {
    if (polygon?.options.fillOpacity === 0.7) {
      polygon?.setStyle({
        fillOpacity: 0.0,
      });
    }
  });
}

function setPolygonClicked(cropsId: number): void {
  console.log("setPolygonClicked");
  const crop = getCropById(cropsId);
  if (crop) {
    if (polygonMap.has(cropsId)) {
      const polygon = polygonMap.get(cropsId);
      if (polygon?.options.fillOpacity !== 1) {
        removeClickedPolygon();
        polygon?.setStyle({
          fillOpacity: 1.0,
        });
      } else {
        removeClickedPolygon();
        polygon?.setStyle({
          fillOpacity: 0.7,
        });
      }
    }
  }
}

function getCropById(cropsId: number): Bed | undefined {
  for (let i = 0; i < props.beds.beds.length; i++) {
    if (props.beds.beds[i].id == cropsId) {
      return props.beds.beds[i];
    }
  }
  return undefined;
}

function setPolygonInactive(cropsId: number): void {
  const crop = getCropById(cropsId);
  if (crop) {
    if (polygonMap.has(cropsId)) {
      const polygon = polygonMap.get(cropsId);
      if (polygon?.options.fillOpacity !== 1) {
        polygon?.setStyle({
          fillOpacity: 0.0,
        });
      }
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

function polygonClick(polygon: L.Polygon<any>): void {
  console.log("polygonClick");
  const cropsId: number = getIdByPolygon(polygon);
  if (cropsId != -1) {
    emit("polygonClick", cropsId);
  }
}
</script>
