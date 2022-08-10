<template>
  <q-tooltip
    class="w-60 bg-white card"
    style="border-radius: 1rem"
    :delay="500"
  >
    <!-- fit -->
    <div class="p-2">
      <div class="font-bold text-[#707070] text-sm mb-2">Health:</div>
      <!-- <p> -->
      <q-badge
        text-color="black"
        :class="{
          'bg-n/a': health.loglevel === 0,
          'bg-ok': health.loglevel === 1,
          'bg-warning-custom': health.loglevel === 2,
          'bg-danger': health.loglevel === 3,
        }"
      >
        <div class="font-bold">
          {{ health.type[0].toUpperCase() + health.type.slice(1) }}
        </div>
      </q-badge>
      <div>
        <div
          class="font-bold text-sm mt-2"
          :class="{
            'text-n/a-text': health.loglevel === 0,
            'text-ok-text': health.loglevel === 1,
            'text-warning-custom-text': health.loglevel === 2,
            'text-danger': health.loglevel === 3,
          }"
        >
          {{ health.loglevel }}: {{ infoLoglevel[health.loglevel] }}
        </div>
        <div class="font-bold text-black text-sm">
          <div v-if="health.type === 'water'">
            {{ infoWatering[health.loglevel] }} {{ plant }}.
          </div>
          <div v-else-if="health.type === 'nutrients'">
            {{ infoNutrient[health.loglevel] }} {{ plant }}.
          </div>
          <div v-else-if="health.type === 'diseases'">
            {{ infoDisease[health.loglevel] }} {{ plant }}.
          </div>
        </div>
      </div>
      <!-- </p> -->
    </div>
  </q-tooltip>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type CropsTable from "@/components/table/CropsTable.vue";
import type { Health } from "@/types/health";

const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

const props = defineProps<{
  health: Health;
  plant: string;
}>();

defineEmits<{
  (event: "removeClicked"): void;
}>();

const infoLoglevel: string[] = ["N/A", "OK", "Warning", "Attention"];
const infoNotAvailable =
  "The health state is not available at the moment for your";

const infoNutrient: string[] = [
  infoNotAvailable,
  "No nutrient deficiency has been detected in your",
  "A nutrient deficiency has been detected in your",
  "Action required, a nutrient deficiency has been detected in your",
];

const infoDisease: string[] = [
  infoNotAvailable,
  "No disease has been detected in your",
  "A disease has been detected in your",
  "Action required, a disease has been detected in your",
];

const infoWatering: string[] = [
  infoNotAvailable,
  "No lack of water has been detected in your",
  "A lack of water has been detected in your",
  "Action required, a lack of water has been detected in your",
];
</script>

<style></style>
