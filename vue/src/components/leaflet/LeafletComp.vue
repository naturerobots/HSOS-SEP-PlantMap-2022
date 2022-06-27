<template>
  <div class="map-container w-full h-full relative">
    <div id="map"></div>
  </div>
</template>

<script setup lang="ts">
import "leaflet/dist/leaflet.css";
import { onMounted } from "vue";
import L from "leaflet";
import "./LeafletRotation.ts";
import type { MapImage } from "@/types/mapImage";

let leafletMap: L.Map;

const props = withDefaults(
  defineProps<{
    mapImage: MapImage;
    maxZoom?: number;
    zoom?: number;
    zoomControl?: boolean;
  }>(),
  {
    maxZoom: 24,
    zoom: 13,
    zoomControl: true,
  }
);

defineExpose({
  addTileLayer,
  addMarker,
  addPolygon,
  setView,
});

onMounted(() => {
  leafletMap = L.map("map", {
    zoomControl: false,
    attributionControl: false,
    zoomDelta: 0.25,
    zoomSnap: 0.25,
  });

  //https://stackoverflow.com/a/55767702
  if (props.zoomControl) {
    L.control
      .zoom({
        position: "bottomright",
      })
      .addTo(leafletMap);
  }

  //Disable map interaction, can be removed later but for now it reduces the number of tiles that need to be downloaded.
  leafletMap.dragging.disable();
  leafletMap.touchZoom.disable();
  leafletMap.doubleClickZoom.disable();
  leafletMap.scrollWheelZoom.disable();
  leafletMap.boxZoom.disable();
  leafletMap.keyboard.disable();
  if (leafletMap.tap) leafletMap.tap.disable();

  //TODO: refactor params
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibHNpZWJlbHMiLCJhIjoiY2wxdno3d2E0Mnh4ZDNqcXJzbHlqeWZoMCJ9.KXbrKH7ESK2qu28olSw6sQ",
    {
      maxNativeZoom: 19,
      minZoom: 19,
      maxZoom: props.maxZoom,
    }
  ).addTo(leafletMap);

  if (props.mapImage) {
    let overlay = L.imageOverlay.rotated(
      props.mapImage.src,
      props.mapImage.top_left,
      props.mapImage.top_right,
      props.mapImage.bottom_left,
      {
        opacity: 1,
      }
    );

    leafletMap.addLayer(overlay);

    //TODO not the best solution, map doens't appear right on first load with 100% height. For now it worked with setTimeout and invalidateSize.
    setTimeout(function () {
      leafletMap.invalidateSize(true);
      const bounds = L.latLngBounds(
        props.mapImage.bottom_left,
        props.mapImage.top_right
      );
      leafletMap.fitBounds(bounds, { animate: true });
    }, 100);
  }
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
</script>
