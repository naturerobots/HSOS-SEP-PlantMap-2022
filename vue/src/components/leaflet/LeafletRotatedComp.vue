<template>
  <div class="inline-flex space-x-3 pl-2 items-center q-pa-md">
    <q-btn rounded color="primary" label="Save Image" @click="saveImage" />
    <q-btn
      v-if="markers.length == 3 && parseFloat(opacity.toFixed(1)) >= 0.1"
      rounded
      color="black font-bold"
      fab-mini
      label="-"
      @click="updateOpacity(-0.1)"
    />
    <q-btn
      v-if="markers.length == 3 && parseFloat(opacity.toFixed(1)) <= 0.9"
      rounded
      color="black font-bold"
      fab-mini
      label="+"
      @click="updateOpacity(0.1)"
    />
  </div>

  <div class="card-map h-full m-4 flex-1">
    <div class="map-container w-full h-full">
      <div id="map"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import L from "leaflet";
import type { LeafletMouseEvent } from "leaflet";
import { useQuasar } from "quasar";
import type { QVueGlobals } from "quasar";
import "leaflet/dist/leaflet.css";
import "./LeafletRotation.ts";

const router = useRouter();
const route = useRoute();
const markers = ref<L.Marker[]>([]);

const $q: QVueGlobals = useQuasar();

let leafletMap: L.Map;
let overlay: L.ImageOverlay.Rotated;
let counter = 0;
let opacity = ref<number>(0.5);

const greenIcon: L.Icon = new L.Icon({
  iconUrl: "src/assets/marker/marker_green.svg",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
});

onMounted(() => {
  if (!route.params.src) {
    $q.notify({
      type: "negative",
      message: "No image selected!",
    });
    router.push({ path: "/cropimage" });
  }

  //TODO: Get coords from stored location
  leafletMap = L.map("map", { zoomControl: false }).setView(
    new L.LatLng(52.317033021766406, 7.630251717595675),
    13
  );

  //TODO: refactor params
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHNpZWJlbHMiLCJhIjoiY2wxdno3d2E0Mnh4ZDNqcXJzbHlqeWZoMCJ9.KXbrKH7ESK2qu28olSw6sQ",
    {
      maxNativeZoom: 18,
      minZoom: 18,
      maxZoom: 22,
    }
  ).addTo(leafletMap);

  leafletMap.on("click", setMarker);
});

function repositionImage() {
  if (markers.value.length == 3) {
    overlay.reposition(
      markers.value[0].getLatLng(),
      markers.value[1].getLatLng(),
      markers.value[2].getLatLng()
    );
  }

  console.log(markers.value.map((value) => value?.getLatLng()));
}

function updateOpacity(opacityFactor: number) {
  opacity.value += opacityFactor;
  console.log(opacity.value.toFixed(1));
  if (
    markers.value.length == 3 &&
    parseFloat(opacity.value.toFixed(1)) >= 0.0 &&
    parseFloat(opacity.value.toFixed(1)) <= 1.0
  ) {
    overlay.updateOpacity(opacity.value);
  }
}

function setMarker(e: LeafletMouseEvent): void {
  if (counter < 3) {
    let point = L.latLng(e.latlng.lat, e.latlng.lng);
    let marker: L.Marker = L.marker(point, {
      draggable: true,
      icon: greenIcon,
    }).addTo(leafletMap);

    markers.value.push(marker);
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
    markers.value[0].getLatLng(),
    markers.value[1].getLatLng(),
    markers.value[2].getLatLng(),
    {
      opacity: opacity.value,
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
