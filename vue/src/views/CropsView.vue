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
      <crops-table
        ref="cropsTableRef"
        title="Overview"
        :crops="crops"
        :visibleColumns="columns"
        @row-enter="tableCropsEnter"
        @row-leave="tableCropsLeave"
      ></crops-table>
    </div>
    <div class="col-4 pl-2">
      <crops-map
        ref="cropsMapRef"
        :crops="crops"
        @polygon-enter="mapCropsEnter"
        @polygon-leave="mapCropsLeave"
      ></crops-map>
    </div>
  </div>
</template>

<script setup lang="ts">
import CropsTable from "../components/CropsTable.vue";
import { ref, type Ref } from "vue";
import { cropsStore } from "@/stores/cropsStore";
import HeaderBar from "@/components/HeaderBar.vue";
import CropsMap from "@/components/CropsMap.vue";
import type { Crop } from "@/types/crop";
import { storeToRefs } from "pinia";

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

const crops: Ref<Crop[]> = storeToRefs(cropsStore()).getCrops;
const cropsMapRef = ref<InstanceType<typeof CropsMap> | null>(null);
const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

// Table - Map interaction
function mapCropsEnter(cropsId: number): void {
  cropsTableRef.value?.setRowActive(cropsId);
}

function mapCropsLeave(cropsId: number): void {
  cropsTableRef.value?.setRowInactive(cropsId);
}

function tableCropsEnter(cropsId: number): void {
  cropsMapRef.value?.setPolygonActive(cropsId);
}

function tableCropsLeave(cropsId: number): void {
  cropsMapRef.value?.setPolygonInactive(cropsId);
}
</script>
