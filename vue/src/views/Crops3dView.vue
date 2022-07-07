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
          :visibleColumns="columns"
          :crops="crops"
          @row-enter="tableCropsEnter"
          @row-leave="tableCropsLeave"
        ></crops-table>
      </div>
      <div v-if="storeOptions.indexOf('3d-map') > -1" class="col-8 pl-2">
        <crops-map
          ref="cropsMapRef"
          :crops="crops"
          @polygon-enter="mapCropsEnter"
          @polygon-leave="mapCropsLeave"
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

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptions3D: WidgetOption[] = [
  widgetOptions.crops3dTable,
  widgetOptions.crops3dMap,
];

let columns: string[] = ["id", "plant", "location"];

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
