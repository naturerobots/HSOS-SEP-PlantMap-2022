<template>
  <base-map :map-image="mapImage" :zoom="20.5"></base-map>
</template>

<script setup lang="ts">
import BaseMap from "@/components/BaseMap.vue";
import type { MapImage } from "@/types/mapImage";
import { LatLng } from "leaflet";

const mapImage: MapImage = {
  src: "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=1920&y=1080&a=true",
  top_left: new LatLng(52.31703002877383, 7.6307445019483575),
  top_right: new LatLng(52.316885520295315, 7.630280744986272),
  bottom_left: new LatLng(52.31721038577891, 7.630586922168733),
};
</script>
