<!-- <template>
  <header-bar title="Crops"></header-bar>
  <div class="p-6"></div>
</template> -->

<template>
  <!-- <div class="px-3 py-5 text-h2 text-primary_hover">
    Crops
  </div> -->
  <header-bar title="Crops"></header-bar>
  <div class="row p-6">
    <div class="col-8">
      <CropsTable />
    </div>
    <div class="col-4 pl-2">
      <q-card class="shadow-1">
        <img src="../assets/img/gardenDummy.png" alt="" />
      </q-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import CropsTable from "../components/CropsTable.vue";
import { onMounted } from "vue";
import { cropsStore } from "@/stores/cropsStore";
import HeaderBar from "@/components/HeaderBar.vue";

onMounted(() => {
  cropsStore().loadDataFromApi();
});
</script>
