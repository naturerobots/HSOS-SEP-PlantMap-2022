<!-- <template>
  <header-bar title="Crops"></header-bar>
  <div class="p-6"></div>
</template> -->

<template>
  <!-- <div class="px-3 py-5 text-h2 text-primary_hover">
    Crops
  </div> -->
  <header-bar
    title="Crops"
    :widgetOptions="widgetOptionsCrops"
    :storeOptions="storeOptions"
  ></header-bar>
  <div class="row p-6">
    <div v-if="storeOptions.indexOf('crops-table') > -1" class="col-8">
      <crops-table title="Overview" :visibleColumns="columns"></crops-table>
    </div>
    <div v-if="storeOptions.indexOf('crops-map') > -1" class="col-4 pl-2">
      <crops-map></crops-map>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, type Ref } from "vue";
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

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptionsCrops: WidgetOption[] = [
  widgetOptions.cropsTable,
  widgetOptions.cropsMap,
];

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
