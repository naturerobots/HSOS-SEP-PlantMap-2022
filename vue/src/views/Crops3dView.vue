<template>
  <div class="flex-nowrap">
    <header-bar
      title="3D"
      :widgetOptions="widgetOptions3D"
      :storeOptions="storeOptions"
    ></header-bar>
    <div class="row p-6">
      <div v-if="storeOptions.indexOf('3d-table') > -1" class="col-4">
        <crops-table
          ref="cropsTableRef"
          title="Plants"
          :visibleColumns="columns"
          :crops="crops"
          @row-enter="tableCropsEnter"
          @row-leave="tableCropsLeave"
          @row-click="tableCropsClick"
        ></crops-table>
      </div>
      <div v-if="storeOptions.indexOf('3d-map') > -1" class="col-8 pl-2">
        <crops-map
          ref="cropsMapRef"
          :crops="crops"
          @polygon-enter="mapCropsEnter"
          @polygon-leave="mapCropsLeave"
          @polygon-click="mapCropsClick"
        ></crops-map>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { type Ref, ref } from "vue";
import { storeToRefs } from "pinia";
import { cropsStore } from "@/stores/cropsStore";
import { userStore } from "@/stores/userStore";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import HeaderBar from "@/components/header/HeaderBar.vue";
import CropsTable from "../components/CropsTable.vue";
import CropsMap from "@/components/CropsMap.vue";
import type { Bed } from "@/types/crop";

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptions3D: WidgetOption[] = [
  widgetOptions.crops3dTable,
  widgetOptions.crops3dMap,
];

let columns: string[] = ["id", "plant", "location"];

const crops: Ref<Bed[]> = storeToRefs(cropsStore()).getCrops;
const cropsMapRef = ref<InstanceType<typeof CropsMap> | null>(null);
const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

// Table - Map interaction
function mapCropsEnter(cropsId: number): void {
  cropsTableRef.value?.setRowActive(cropsId);
}

function mapCropsLeave(cropsId: number): void {
  cropsTableRef.value?.setRowInactive(cropsId);
}

function mapCropsClick(cropsId: number): void {
  cropsTableRef.value?.setRowClicked(cropsId);
}

function tableCropsEnter(cropsId: number): void {
  cropsMapRef.value?.setPolygonActive(cropsId);
}

function tableCropsLeave(cropsId: number): void {
  cropsMapRef.value?.setPolygonInactive(cropsId);
}

function tableCropsClick(cropsId: number): void {
  cropsMapRef.value?.setPolygonClicked(cropsId);
}
</script>
