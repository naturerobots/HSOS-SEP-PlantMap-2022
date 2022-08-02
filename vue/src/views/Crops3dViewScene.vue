<template>
  <base-layout
    title="3D"
    :widgetOptions="widgetOptions3D"
    :storeOptions="storeOptions"
  >
    <div class="row p-6">
      <crop-scene-potree></crop-scene-potree>
    </div>
  </base-layout>
</template>

<script setup lang="ts">
//import CropScene from "@/components/three-scenes/CropScene.vue";
import CropScenePotree from "@/components/three-scenes/CropScenePotree.vue";
import { type Ref, ref } from "vue";
import { storeToRefs } from "pinia";
import { cropsStore } from "@/stores/cropsStore";
import { userStore } from "@/stores/userStore";
import {
  widgetOptions,
  type StoreOption,
  type WidgetOption,
} from "@/types/widgetOption";
import BaseLayout from "@/components/layout/BaseLayout.vue";
import type { Crop } from "@/types/crop";

const storeOptions: Ref<StoreOption[]> = storeToRefs(userStore()).getOptions;
const widgetOptions3D: WidgetOption[] = [
  widgetOptions.crops3dTable,
  widgetOptions.crops3dMap,
];

let columns: string[] = ["id", "plant", "location"];

const crops: Ref<Crop[]> = storeToRefs(cropsStore()).getCrops;
</script>
