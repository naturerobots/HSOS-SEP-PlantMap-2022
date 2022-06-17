<template>
  <header-bar
    title="3D"
    :widgetOptions="widgetOptions3D"
    :storeOptions="storeOptions"
  ></header-bar>
  <div class="row p-6">
    <div v-if="storeOptions.indexOf('3d-table') > -1" class="col-4">
      <crops-table title="Plants" :visibleColumns="columns"></crops-table>
    </div>
    <div v-if="storeOptions.indexOf('3d-map') > -1" class="col-8 pl-2">
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
import HeaderBar from "@/components/header/HeaderBar.vue";
import CropsTable from "../components/CropsTable.vue";
import CropsMap from "@/components/CropsMap.vue";

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptions3D: WidgetOption[] = [
  widgetOptions["3dTable"],
  widgetOptions["3dMap"],
];

onMounted(() => {
  cropsStore().loadDataFromApi();
});

let columns: string[] = ["id", "plant", "location"];
</script>
