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
          'bg-blue': health.loglevel === 0,
          'bg-green': health.loglevel === 1,
          'bg-warning': health.loglevel === 2,
          'bg-red': health.loglevel === 3,
        }"
      >
        <div class="font-bold">{{ health.type }}</div>
      </q-badge>
      <div>
        <div
          class="font-bold text-sm mt-2"
          :class="{
            'text-blue': health.loglevel === 0,
            'text-green': health.loglevel === 1,
            'text-warning': health.loglevel === 2,
            'text-red': health.loglevel === 3,
          }"
        >
          {{ health.loglevel }}: {{ infoLoglevel[health.loglevel] }}
        </div>
        <div class="font-bold text-black text-sm">
          <div v-if="health.shortcut === 'W'">
            {{ infoWatering[health.loglevel] }} {{ plant }}.
          </div>
          <div v-else-if="health.shortcut === 'N'">
            {{ infoNutrient[health.loglevel] }} {{ plant }}.
          </div>
          <div v-else-if="health.shortcut === 'D'">
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
import type CropsTable from "@/components/CropsTable.vue";
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
