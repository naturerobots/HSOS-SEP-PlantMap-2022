<template>
  <q-popup-proxy
    ref="cropsTableRef"
    class="w-80"
    anchor="bottom middle"
    self="top middle"
    style="border-radius: 1rem"
  >
    <!-- fit -->
    <div class="absolute right-0">
      <button class="text-secondary p-1" v-close-popup @click="removeClicked()">
        <span
          class="material-icons hover:text-black p-1"
          style="font-size: 20px"
          >close</span
        >
      </button>
      <!-- <q-btn class="text-secondary" flat icon="close" v-close-popup/> -->
    </div>
    <div class="p-4 grid grid-cols-3 grid-flow-row auto-rows-max">
      <div class="grid-span-1">
        <div class="font-bold text-[#707070]">Status:</div>
        <div class="font-bold text-lg">Sprout</div>
      </div>
      <div class="grid-span-2">
        <div class="font-bold text-[#707070]">Health:</div>
        <div>
          <p>
            <!-- <q-badge class="bg-warning" text-color="black"> -->
            <!-- <div class="font-bold">Disease Detection</div> -->
            <!-- </q-badge> -->
            <q-expansion-item
              class="shadow-1 overflow-hidden mt-3"
              label="Disease Detection"
              dense
              style="width: 193px; border-radius: 0.25rem"
              header-class="bg-warning font-bold text-sm p-0"
              group="health"
            >
              <div class="px-4 p-2">
                <div class="text-warning font-bold text-sm">2: Attention</div>
                <div class="font-bold text-sm">
                  A desease has been detected in your lettuce.
                </div>
              </div>
            </q-expansion-item>
          </p>
          <p>
            <!-- <q-badge class="bg-red" text-color="black">
                            <div class="font-bold">Nutrient Deficiency</div>
                        </q-badge> -->
            <q-expansion-item
              class="shadow-1 overflow-hidden mt-3"
              label="Nutrient Deficiency"
              dense
              style="width: 193px; border-radius: 0.25rem"
              header-class="bg-red font-bold text-sm p-0"
              group="health"
            >
              <div class="px-4 p-2">
                <div class="text-red font-bold text-sm">3: Warning</div>

                <div class="font-bold text-sm">
                  Action required, a nutrient deficiency has been detected in
                  your lettuce.
                </div>
              </div>
            </q-expansion-item>
          </p>
          <p>
            <!-- <q-badge class="bg-green" text-color="black">
                            <div class="font-bold">Watering</div>
                        </q-badge> -->
            <q-expansion-item
              class="shadow-1 overflow-hidden mt-3"
              label="Watering"
              dense
              style="width: 193px; border-radius: 0.25rem"
              header-class="bg-green font-bold text-sm p-0"
              group="health"
            >
              <div class="px-4 p-2">
                <div class="text-green font-bold text-sm"></div>
                <div class="font-bold text-sm">
                  Your lettuce is perfectly watered.
                </div>
              </div>
            </q-expansion-item>
          </p>
        </div>
      </div>
    </div>
  </q-popup-proxy>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type CropsTable from "@/components/CropsTable.vue";

const cropsTableRef = ref<InstanceType<typeof CropsTable> | null>(null);

function removeClicked(): void {
  console.log("removeClicked");
  // console.log(cropsTableRef.value?.removeClickedRow());
  // cropsTableRef.value?.removeClickedRow();
}
</script>

<style></style>
