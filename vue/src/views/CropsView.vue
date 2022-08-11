<template>
  <base-layout
    title="Crops"
    :widgetOptions="widgetOptionsCrops"
    :storeOptions="storeOptions"
  >
    <div class="row p-6">
      <!-- <div
        v-if="beds.beds && storeOptions.indexOf('crops-table') > -1"
        class="col-8"
      > -->
      <div v-if="storeOptions.indexOf('crops-table') > -1" class="col-8">
        <crops-table
          ref="cropsTableRef"
          title="Beds"
          :beds="beds"
          :visibleColumnsBeds="colsBedTable"
          :visibleColumnsCrops="colsCropsTable"
          @row-enter="tableCropsEnter"
          @row-leave="tableCropsLeave"
          @row-click="tableCropsClick"
        ></crops-table>
      </div>
      <div
        v-if="beds.beds && storeOptions.indexOf('crops-map') > -1"
        class="col-4 pl-2"
      >
        <crops-map ref="cropsMapRef" :beds="beds"></crops-map>
      </div>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import { type Ref, ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { cropsStore } from "@/stores/cropsStore";
import { userStore } from "@/stores/userStore";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import CropsTable from "@/components/table/CropsTable.vue";
import CropsMap from "@/components/map/CropsMap.vue";
import BaseLayout from "@/components/layout/BaseLayout.vue";
import type { Crop } from "@/types/crop";
import type { Plants } from "@/types/plants";
import { bedStore } from "@/stores/bedStore";
import type { Bed } from "@/types/bed";
import type { Beds } from "@/types/beds";
const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptionsCrops: WidgetOption[] = [
  widgetOptions.cropsTable,
  widgetOptions.cropsMap,
];

// onMounted(() => {
//   bedStore().loadDataFromApi();
// });

onMounted(() => {
  console.log("onMounted");
  bedStore().loadDataFromApi();
});

let colsBedTable: string[] = [
  // "id",
  "plant",
  "location",
  "variety",
  "soil_humidity",
  "health",
  "status",
  "harvest",
  "yield",
  "3d",
];

let colsCropsTable: string[] = [
  // "id",
  "plant",
  // "location",
  "variety",
  "soil_humidity",
  "health",
  "status",
  "harvest",
  "yield",
  // "3d",
];

const beds: Ref<Beds> = storeToRefs(bedStore()).getBeds;
const plants: Ref<Plants> = storeToRefs(cropsStore()).getCrops;

const cropsMapRef = ref<InstanceType<typeof CropsMap> | null>(null);
const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

// Table - Map interaction
// function mapCropsEnter(cropsId: number): void {
//   cropsTableRef.value?.setRowActive(cropsId);
// }

// function mapCropsLeave(cropsId: number): void {
//   cropsTableRef.value?.setRowInactive(cropsId);
// }

// function mapCropsClick(cropsId: number): void {
//   cropsTableRef.value?.setRowClicked(cropsId);
// }

// function tableCropsEnter(cropsId: number): void {
//   cropsMapRef.value?.setPolygonActive(cropsId);
// }

// function tableCropsLeave(cropsId: number): void {
//   cropsMapRef.value?.setPolygonInactive(cropsId);
// }

// function tableCropsClick(cropsId: number): void {
//   cropsMapRef.value?.setPolygonClicked(cropsId);
// }
</script>
