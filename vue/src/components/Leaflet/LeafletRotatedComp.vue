<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
  <button class="btn btn-primary mt-3" @click="saveImage">Save</button>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "./Leaflet.ImageOverlay.Rotated.js";

const router = useRouter();
let leafletMap = {} as L.Map;
let markers: L.Marker[] = [];
let counter = 0;
let overlay = {} as L.Overlay;

const greenIcon: L.Icon = new L.Icon({
  iconUrl: "src/assets/marker/marker_green.svg",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
});

onMounted(() => {
  leafletMap = L.map("map", { zoomControl: false }).setView(
    new L.LatLng(52.27264, 8.0498),
    13
  );
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxNativeZoom: 18,
    maxZoom: 24,
  }).addTo(leafletMap);

  leafletMap.on("click", setMarker);
});

function repositionImage() {
  if (markers.length == 3) {
    overlay.reposition(
      markers[0].getLatLng(),
      markers[1].getLatLng(),
      markers[2].getLatLng()
    );
  }
}

function setMarker(e): void {
  if (counter < 3) {
    let point = L.latLng(e.latlng.lat, e.latlng.lng);
    let marker: L.Marker = L.marker(point, {
      draggable: true,
      icon: greenIcon,
    }).addTo(leafletMap);
    markers.push(marker);
    marker.on("drag dragend", repositionImage);
    counter += 1;
    if (counter == 3) {
      setImage();
    }
  }
}

function setImage(): void {
  overlay = L.imageOverlay.rotated(
    "https://cloud.naturerobots.de/apps/files_sharing/publicpreview/xZj9ytRt8WKr5cw?file=/goeoentueuegs_ibbenbueren_new2.jpg&fileId=28565&x=2736&y=1824&a=true",
    markers[0].getLatLng(),
    markers[1].getLatLng(),
    markers[2].getLatLng(),
    {
      opacity: 1,
      interactive: true,
    }
  );
  leafletMap.addLayer(overlay);
  //var	bounds = new L.LatLngBounds(markers[0].getLatLng(), markers[1].getLatLng()).extend(markers[2].getLatLng());
  //leafletMap.fitBounds(bounds);
}

function saveImage(): void {
  //ToDo: Router to dashBoard, send to Server pos + img
  router.push({ path: "/dashboard" });
}
</script>

<style>
.map-container {
  width: 100%;
}
#map {
  height: 600px;
  width: 100%;
}
</style>
