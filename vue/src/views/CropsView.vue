<!-- <template>
  <header-bar title="Crops"></header-bar>
  <div class="p-6"></div>
</template> -->

<template>
  <!-- <div class="px-3 py-5 text-h2 text-primary_hover">
    Crops
  </div> -->
  <header-bar title="Crops"></header-bar>
  <div class="row p-6">
    <div class="col-8">
      <crops-table title="Overview" :visibleColumns="columns"></crops-table>
    </div>
    <div class="col-4 pl-2">
      <crops-map></crops-map>
    </div>
  </div>
</template>

<script setup lang="ts">
import CropsTable from "../components/CropsTable.vue";
import { onMounted } from "vue";
import { cropsStore } from "@/stores/cropsStore";
import HeaderBar from "@/components/header/HeaderBar.vue";
import CropsMap from "@/components/CropsMap.vue";
onMounted(() => {
  cropsStore().loadDataFromApi();
});

let columns: string[] = [
  "id",
  "plant",
  "location",
  "variety",
  "soilHumidity",
  "health",
  "status",
  "harvest",
  "yield",
  "3d",
];
</script>
