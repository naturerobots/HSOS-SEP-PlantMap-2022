<template>
  <div class="map-container w-full h-full relative">
    <div id="map"></div>
  </div>
</template>

<script setup lang="ts">
import "leaflet/dist/leaflet.css";
import { onMounted, onUpdated } from "vue";
import L, { LatLng } from "leaflet";
import "./LeafletRotation.ts";
import type { GardenImage } from "@/types/gardenImage";

let leafletMap: L.Map;
let overlay: L.imageOverlay;
let gardenImage: GardenImage;

const props = withDefaults(
  defineProps<{
    maxZoom?: number;
    zoom?: number;
    zoomControl?: boolean;
    mapInteraction?: boolean;
  }>(),
  {
    maxZoom: 24,
    zoom: 13,
    //Disabled map interaction per default, can be fixed later but for now it reduces the number of tiles that need to be downloaded.
    mapInteraction: false,
  }
);

defineExpose({
  addTileLayer,
  addMarker,
  addPolygon,
  setView,
  addGardenImage,
});

onMounted(() => {
  leafletMap = L.map("map", {
    ...{
      zoomControl: false,
      attributionControl: false,
      zoomDelta: 0.25,
      zoomSnap: 0.25,
    },
    ...(props.mapInteraction
      ? {}
      : {
          dragging: false,
          touchZoom: false,
          doubleClickZoom: false,
          scrollWheelZoom: false,
          boxZoom: false,
          keyboard: false,
          tap: false,
        }),
  });

  //https://stackoverflow.com/a/55767702
  if (props.zoomControl) {
    L.control
      .zoom({
        position: "topright",
      })
      .addTo(leafletMap);
  }

  //TODO: refactor params
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHNpZWJlbHMiLCJhIjoiY2wxdno3d2E0Mnh4ZDNqcXJzbHlqeWZoMCJ9.KXbrKH7ESK2qu28olSw6sQ",
    {
      maxNativeZoom: 19,
      minZoom: 19,
      maxZoom: props.maxZoom,
    }
  ).addTo(leafletMap);

  setTimeout(function () {
    if (gardenImage) {
      var coordTopRight = gardenImage.coordinates.find(
        (coord) => coord.name === "topRight"
      );
      var coordBottomLeft = gardenImage.coordinates.find(
        (coord) => coord.name === "bottomLeft"
      );

      leafletMap.invalidateSize(true);
      const bounds = L.latLngBounds(
        new L.LatLng(coordTopRight!.latitude, coordTopRight!.longitude),
        new L.LatLng(coordBottomLeft!.latitude, coordBottomLeft!.longitude)
      );
      leafletMap.fitBounds(bounds, { animate: true });
    } else {
      leafletMap.invalidateSize(true);
      leafletMap.invalidateSize(false);
      leafletMap.setView(new L.LatLng(52.2719595, 8.047635), 19);
    }
  }, 100);
});

function addTileLayer(tileLayer: L.TileLayer) {
  tileLayer.addTo(leafletMap);
}

function addMarker(marker: L.Marker): void {
  marker.addTo(leafletMap);
}

function addPolygon(polygon: L.Polygon): void {
  polygon.addTo(leafletMap);
}

function setView(latlng: L.LatLng, zoom: number): void {
  leafletMap.setView(latlng, zoom);
}

function addGardenImage(updatedGardenImage: GardenImage): void {
  gardenImage = updatedGardenImage;

  if (overlay) {
    leafletMap.removeLayer(overlay);
  }

  var coordTopLeft = gardenImage.coordinates.find(
    (coord) => coord.name === "topLeft"
  );
  var coordTopRight = gardenImage.coordinates.find(
    (coord) => coord.name === "topRight"
  );
  var coordBottomLeft = gardenImage.coordinates.find(
    (coord) => coord.name === "bottomLeft"
  );

  overlay = L.imageOverlay.rotated(
    gardenImage.image,
    new L.LatLng(coordTopLeft!.latitude, coordTopLeft!.longitude),
    new L.LatLng(coordTopRight!.latitude, coordTopRight!.longitude),
    new L.LatLng(coordBottomLeft!.latitude, coordBottomLeft!.longitude),
    {
      opacity: 1,
    }
  );

  leafletMap.addLayer(overlay);

  leafletMap.invalidateSize(true);
  const bounds = L.latLngBounds(
    new L.LatLng(coordTopRight!.latitude, coordTopRight!.longitude),
    new L.LatLng(coordBottomLeft!.latitude, coordBottomLeft!.longitude)
  );
  leafletMap.fitBounds(bounds, { animate: true });
}
</script>
