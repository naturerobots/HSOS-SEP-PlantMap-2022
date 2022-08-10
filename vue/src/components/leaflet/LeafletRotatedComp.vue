<template>
  <div class="flex flex-col h-full" style="flex-wrap: nowrap">
    <div class="px-4 pt-4">
      <q-btn
        class="mr-2 bg-primary text-white"
        v-if="markers.length == 3"
        rounded
        label="Save Image"
        @click="saveImage"
      ></q-btn>
      <q-btn
        class="mr-1 bg-secondary text-white"
        v-if="markers.length == 3 && parseFloat(opacity.toFixed(1)) >= 0.1"
        rounded
        fab-mini
        label="-"
        @click="updateOpacity(-0.1)"
      ></q-btn>
      <q-btn
        class="mr-1 bg-secondary text-white"
        v-if="markers.length == 3 && parseFloat(opacity.toFixed(1)) <= 0.9"
        rounded
        fab-mini
        label="+"
        @click="updateOpacity(0.1)"
      ></q-btn>
    </div>
    <div class="grow p-4">
      <div class="card-map h-full">
        <div class="map-container w-full">
          <div id="map"></div>
        </div>
      </div>
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
import { companyStore } from "@/stores/companyStore";
import { gardenStore } from "@/stores/gardenStore";
import type { Coordinate, GardenImage } from "@/types/gardenImage";

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
  leafletMap = L.map("map", {
    zoomControl: false,
    attributionControl: false,
  }).setView(new L.LatLng(52.317033021766406, 7.630251717595675), 13);

  //TODO: refactor params
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHNpZWJlbHMiLCJhIjoiY2wxdno3d2E0Mnh4ZDNqcXJzbHlqeWZoMCJ9.KXbrKH7ESK2qu28olSw6sQ",
    {
      maxNativeZoom: 18,
      minZoom: 18,
      maxZoom: 22,
    }
  ).addTo(leafletMap);

  if (route.params.coordinates) {
    const parsedCoordinates = JSON.parse(
      route.params.coordinates as string
    ) as Coordinate[];
    setMarkerAndPlaceImage(parsedCoordinates);
  } else {
    leafletMap.on("click", setMarker);
  }
});

function repositionImage() {
  if (markers.value.length == 3) {
    overlay.reposition(
      markers.value[0].getLatLng(),
      markers.value[1].getLatLng(),
      markers.value[2].getLatLng()
    );
  }
}

function updateOpacity(opacityFactor: number) {
  opacity.value += opacityFactor;
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

function setMarkerAndPlaceImage(coordinates: Coordinate[]): void {
  const topLeft = coordinates.find((coord) => coord.name === "top_left");
  const topRight = coordinates.find((coord) => coord.name === "top_right");
  const bottomLeft = coordinates.find((coord) => coord.name === "bottom_left");

  setMarkerFromCoordinate(topLeft);
  setMarkerFromCoordinate(topRight);
  setMarkerFromCoordinate(bottomLeft);

  const bounds = L.latLngBounds(
    new L.LatLng(topRight!.latitude, topRight!.longitude),
    new L.LatLng(bottomLeft!.latitude, bottomLeft!.longitude)
  );
  leafletMap.fitBounds(bounds, { animate: true });

  setImage();
}

function setMarkerFromCoordinate(coordinate: Coordinate | undefined): void {
  if (coordinate) {
    let point = L.latLng(coordinate.latitude, coordinate.longitude);
    let marker: L.Marker = L.marker(point, {
      draggable: true,
      icon: greenIcon,
    }).addTo(leafletMap);

    markers.value.push(marker);
    marker.on("drag dragend", repositionImage);
  }
}

function saveImage(): void {
  if (markers.value.length < 3) {
    $q.notify({
      type: "negative",
      message: "At least 3 markers has to be placed!",
    });
    return;
  }

  const gardenImage: GardenImage = {
    image: route.params.src as string,
    coordinates: [
      {
        name: "top_left",
        longitude: markers.value[0].getLatLng().lng,
        latitude: markers.value[0].getLatLng().lat,
      },
      {
        name: "top_right",
        longitude: markers.value[1].getLatLng().lng,
        latitude: markers.value[1].getLatLng().lat,
      },
      {
        name: "bottom_left",
        longitude: markers.value[2].getLatLng().lng,
        latitude: markers.value[2].getLatLng().lat,
      },
    ],
  };

  gardenStore().setSelectedGardenImg(
    companyStore().getCompanies[0]?.id,
    gardenImage
  );

  router.push({ path: "/dashboard" });
}
</script>
