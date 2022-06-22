<template>
  <header-bar
    title="Crops"
    :widgetOptions="widgetOptionsCrops"
    :storeOptions="storeOptions"
  ></header-bar>
  <div class="row p-6">
    <div v-if="storeOptions.indexOf('crops-table') > -1" class="col-8">
      <crops-table
        ref="cropsTableRef"
        title="Overview"
        :crops="crops"
        :visibleColumns="columns"
        @row-enter="tableCropsEnter"
        @row-leave="tableCropsLeave"
      ></crops-table>
    </div>
    <div v-if="storeOptions.indexOf('crops-map') > -1" class="col-4 pl-2">
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
import { onMounted, type Ref, ref } from "vue";
import { storeToRefs } from "pinia";
import { cropsStore } from "@/stores/cropsStore";
import { userStore } from "@/stores/userStore";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import CropsTable from "@/components/CropsTable.vue";
import HeaderBar from "@/components/header/HeaderBar.vue";
import CropsMap from "@/components/CropsMap.vue";
import type { Crop } from "@/types/crop";
const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptionsCrops: WidgetOption[] = [
  widgetOptions.cropsTable,
  widgetOptions.cropsMap,
];

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
