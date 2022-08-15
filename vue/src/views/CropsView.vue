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
        ></crops-table>
      </div>
      <div
        v-if="beds.beds && storeOptions.indexOf('crops-map') > -1"
        class="col-4 pl-2"
      >
        <crops-map
          ref="cropsMapRef"
          :beds="beds"
          :plants="plants"
          @bed-click="mapCropsClick"
          @bed-enter="mapCropsEnter"
          @bed-leave="mapCropsLeave"
        >
        </crops-map>
      </div>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import { type Ref, ref } from "vue";
import { storeToRefs } from "pinia";
import { userStore } from "@/stores/userStore";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import CropsTable from "@/components/table/CropsTable.vue";
import CropsMap from "@/components/map/CropsMap.vue";
import BaseLayout from "@/components/layout/BaseLayout.vue";
import { bedStore } from "@/stores/bedStore";
import type { Beds } from "@/types/beds";
import { cropsStore } from "@/stores/cropsStore";
import type { Plants } from "@/types/plants";
const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptionsCrops: WidgetOption[] = [
  widgetOptions.cropsTable,
  widgetOptions.cropsMap,
];

let colsBedTable: string[] = [
  //"id",
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
  //"id",
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
function mapCropsEnter(bedId: number): void {
  cropsTableRef.value?.setRowActive(bedId);
}

function mapCropsLeave(bedId: number): void {
  cropsTableRef.value?.setRowInactive(bedId);
}

function mapCropsClick(bedId: number): void {
  //cropsStore().loadDataFromApi(bedId);
  cropsTableRef.value?.setRowClicked(bedId);
}

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
