<template>
  <base-layout
    title="3D"
    :widgetOptions="widgetOptions3D"
    :storeOptions="storeOptions"
  >
    <div class="row p-6">
      <div v-if="storeOptions.indexOf('3d-table') > -1" class="col-4">
        <crops-table
          ref="cropsTableRef"
          title="Plants"
          :visibleColumnsBeds="visibleColsBedsTable"
          :visibleColumnsCrops="visibleColsCropsTable"
          :columns="columns"
          :beds="beds"
        ></crops-table>
      </div>
      <div
        v-if="beds.beds && storeOptions.indexOf('3d-map') > -1"
        class="col-8 pl-2"
      >
        <crops-map
          ref="cropsMapRef"
          :beds="beds"
          :plants="plants"
          @bed-click="mapBedClick"
          @bed-enter="mapBedEnter"
          @bed-leave="mapBedLeave"
          @plant-enter="mapPlantEnter"
          @plant-leave="mapPlantLeave"
        ></crops-map>
      </div>
    </div>
    <div class="row p-6">
      <crop-scene></crop-scene>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
import CropScene from "@/components/three-scenes/CropScene.vue";
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
import type { QTableProps } from "quasar";
import type { Plants } from "@/types/plants";
import { cropsStore } from "@/stores/cropsStore";

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptions3D: WidgetOption[] = [
  widgetOptions.crops3dTable,
  widgetOptions.crops3dMap,
];

let visibleColsBedsTable: string[] = ["health", "plant", "location"];
let visibleColsCropsTable: string[] = ["health", "plant"];

const beds: Ref<Beds> = storeToRefs(bedStore()).getBeds;
const plants: Ref<Plants> = storeToRefs(cropsStore()).getCrops;
const cropsMapRef = ref<InstanceType<typeof CropsMap> | null>(null);
const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

// Table - Map interaction
function mapBedEnter(bedId: number): void {
  cropsTableRef.value?.setRowActiveBed(bedId);
}

function mapBedLeave(bedId: number): void {
  cropsTableRef.value?.setRowInactiveBed(bedId);
}

function mapBedClick(bedId: number): void {
  cropsTableRef.value?.setRowClicked(bedId);
}

function mapPlantEnter(plantId: string): void {
  cropsTableRef.value?.setRowActivePlant(plantId);
}

function mapPlantLeave(plantId: string): void {
  cropsTableRef.value?.setRowInactivePlant(plantId);
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

const columns: QTableProps["columns"] = [
  {
    name: "location",
    align: "left",
    label: "Location",
    field: "id",
    sortable: true,
  },
  {
    name: "plant",
    align: "left",
    label: "Plant",
    field: "plant",
    sortable: true,
  },
  {
    name: "variety",
    align: "left",
    label: "Variety",
    field: "variety",
    sortable: true,
  },
  {
    name: "soil_humidity",
    align: "left",
    label: "Humidity",
    field: "soil_humidity",
    sortable: true,
  },
  {
    name: "health",
    align: "left",
    label: "Health",
    field: "health",
    sortable: false,
  },
  {
    name: "harvest",
    align: "left",
    label: "Harvest",
    field: "harvest",
    sortable: true,
    sort: (a: any, b: any) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "yield",
    align: "left",
    label: "Yield",
    field: "yield",
    sortable: true,
  },
];
</script>
