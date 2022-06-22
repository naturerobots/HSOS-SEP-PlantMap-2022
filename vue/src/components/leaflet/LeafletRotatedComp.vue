<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
  <button class="btn btn-primary mt-3" @click="saveImage">Save</button>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import L, { type LeafletMouseEvent } from "leaflet";
import "leaflet/dist/leaflet.css";
import "./LeafletRotation.ts";

const router = useRouter();
const route = useRoute();
const markers: L.Marker[] = [];

let leafletMap: L.Map;
let overlay: L.ImageOverlay.Rotated;
let counter = 0;

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

function setMarker(e: LeafletMouseEvent): void {
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
    route.params.src,
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
  //TODO: Router to dashBoard, send to Server pos + img
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