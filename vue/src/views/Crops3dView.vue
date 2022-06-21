<template>
  <header-bar title="3D"></header-bar>
  <div class="row p-6">
    <div class="col-4">
      <crops-table title="Plants" :visibleColumns="columns"></crops-table>
    </div>
    <div class="col-8 pl-2">
      <crops-map></crops-map>
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderBar from "@/components/HeaderBar.vue";
import CropsTable from "../components/CropsTable.vue";
import CropsMap from "@/components/CropsMap.vue";
import { cropsStore } from "@/stores/cropsStore";
import { onMounted } from "vue";
onMounted(() => {
  cropsStore().loadDataFromApi();
});

let columns: string[] = ["id", "plant", "location"];
</script>
