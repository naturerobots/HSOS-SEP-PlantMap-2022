<template>
  <base-layout
    title="Crops"
    :widgetOptions="widgetOptionsCrops"
    :storeOptions="storeOptions"
  >
    <div class="row p-6">
      <div v-if="storeOptions.indexOf('crops-table') > -1" class="col-8">
        <crops-table
          ref="cropsTableRef"
          title="Beds"
          :beds="beds"
          :visibleColumnsBeds="visibleColsBedTable"
          :visibleColumnsCrops="visibleColsCropsTable"
          :columns="columns"
        ></crops-table>
      </div>
      <div
        v-if="beds.bedList && storeOptions.indexOf('crops-map') > -1"
        class="col-4 pl-2"
      >
        <crops-map
          ref="cropsMapRef"
          :beds="beds"
          :crops="crops"
          @bed-enter="mapBedEnter"
          @bed-leave="mapBedLeave"
          @crop-enter="mapCropEnter"
          @crop-leave="mapCropLeave"
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
import type { Crops } from "@/types/crops";
import type { QTableProps } from "quasar";

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptionsCrops: WidgetOption[] = [
  widgetOptions.cropsTable,
  widgetOptions.cropsMap,
];

let visibleColsBedTable: string[] = [
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

let visibleColsCropsTable: string[] = [
  "plant",
  "variety",
  "soil_humidity",
  "health",
  "status",
  "harvest",
  "yield",
  "3d",
];

const beds: Ref<Beds> = storeToRefs(bedStore()).getBeds;
const crops: Ref<Crops> = storeToRefs(cropsStore()).getCrops;

const cropsMapRef = ref<InstanceType<typeof CropsMap> | null>(null);
const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

// Table - Map interaction
function mapBedEnter(bedId: number): void {
  cropsTableRef.value?.setRowActiveBed(bedId);
}

function mapBedLeave(bedId: number): void {
  cropsTableRef.value?.setRowInactiveBed(bedId);
}

function mapCropEnter(cropId: string): void {
  cropsTableRef.value?.setRowActivePlant(cropId);
}

function mapCropLeave(cropId: string): void {
  cropsTableRef.value?.setRowInactivePlant(cropId);
}

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
  { name: "3d", align: "left", label: "3D", field: "3d", sortable: false },
];
</script>
