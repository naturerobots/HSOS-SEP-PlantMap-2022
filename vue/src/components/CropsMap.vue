<!--everything in this comp is for testing only-->
<template>
  <base-map :map-image="mapImage" :zoom="20.5" ref="baseMapRef"></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/BaseMap.vue";
import type { MapImage } from "@/types/mapImage";
import L, { LatLng } from "leaflet";
import { ref, onMounted } from "vue";

const baseMapRef = ref<InstanceType<typeof BaseMap> | null>(null);

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_right: new LatLng(52.31724604719058, 7.630553394556046),
  top_left: new LatLng(52.3170773725588, 7.630054503679276),
  bottom_left: new LatLng(52.31686606722232, 7.630242593586445),
};

onMounted(() => {
  let latlng: L.LatLng[] = [];
  latlng.push(new LatLng(52.317039789516954, 7.630354102703116));
  latlng.push(new LatLng(52.316941166226066, 7.630439482077206));
  latlng.push(new LatLng(52.31693439650253, 7.630420101787746));
  latlng.push(new LatLng(52.317031328642415, 7.630334734025543));
  addBedBorder(latlng);
});

function addBedBorder(latlng: L.LatLng[]) {
  let polygon = L.polygon(latlng, { color: "green", fillOpacity: 0 });
  polygon.on("mouseover", function () {
    polygon.setStyle({
      fillOpacity: 0.2,
    });
  });
  polygon.on("mouseout", function () {
    polygon.setStyle({
      fillOpacity: 0,
    });
  });
  baseMapRef.value?.addPolygon(polygon);
}
</script>
