<template>
  <header-bar title="3D"></header-bar>
  <div class="row p-6">
    <div class="col-4">
      <crops-table
        ref="cropsTableRef"
        title="Plants"
        :visibleColumns="columns"
        :crops="crops"
        @row-enter="tableCropsEnter"
        @row-leave="tableCropsLeave"
      ></crops-table>
    </div>
    <div class="col-8 pl-2">
      <crops-map
        ref="cropsMapRef"
        :crops="crops"
        @crops-enter="mapCropsEnter"
        @crops-leave="mapCropsLeave"
      ></crops-map>
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderBar from "@/components/HeaderBar.vue";
import CropsTable from "../components/CropsTable.vue";
import CropsMap from "@/components/CropsMap.vue";
import { cropsStore } from "@/stores/cropsStore";
import type { Crop } from "@/types/crop";
import { storeToRefs } from "pinia";
import { ref, type Ref } from "vue";

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
