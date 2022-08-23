<template>
  <div class="card h-full w-full mr-24">
    <div class="overflow-x-auto overflow-y-auto">
      <div v-if="!cropstable">
        <q-table
          ref="table"
          class="crops-table no-shadow crops-table-hover"
          :title="title"
          :rows="beds.bedList"
          :columns="columns"
          no-data-label="I didn't find anything for you"
          row-key="id"
          :filter="input"
          :visible-columns="visColsBedTable"
          virtual-scroll
          :rows-per-page-options="[0]"
          :pagination="pagination()"
          hide-bottom
          :loading="isLoadingBeds"
          color="primary"
        >
          <template #body="props">
            <q-tr
              no-hover
              :props="props"
              :key="props.row.id"
              @mouseenter="rowEnter(props.row.id)"
              @mouseleave="rowLeave(props.row.id)"
              @click="
                (cropstable = !cropstable),
                  rowClicked(props.row.id),
                  (activeRow = props.row)
              "
            >
              <q-td key="location" :props="props">
                {{ props.row.id }}
              </q-td>

              <q-td key="plant" :props="props">
                {{ props.row.plant }}
              </q-td>

              <q-td key="variety" :props="props">
                {{ props.row.variety }}
              </q-td>

              <q-td key="soil_humidity" :props="props">
                {{ props.row.soil_humidity }}
              </q-td>

              <q-td key="health" :props="props">
                <div class="flex flex-row w-24 text-center">
                  <div
                    class="round-badge mx-1 text-black text-bold transition hover:scale-125"
                    v-for="h in props.row.health"
                    :key="h"
                    :class="{
                      'bg-n/a': h.loglevel === 0,
                      'bg-ok': h.loglevel === 1,
                      'bg-warning-custom': h.loglevel === 2,
                      'bg-danger': h.loglevel === 3,
                    }"
                  >
                    {{ getShortcut(h.type) }}
                    <status-popup
                      :health="h"
                      :plant="props.row.plant"
                      :props="props"
                      @remove-clicked="rowClicked(props.row.id)"
                    ></status-popup>
                  </div>
                </div>
              </q-td>

              <q-td key="harvest" :props="props">
                {{ props.row.harvest }}
              </q-td>

              <q-td key="yield" :props="props">
                {{ roundTwoDec(props.row.yield) }}
              </q-td>

              <q-td :props="props" key="3d">
                <div @click="setBedId(props.row.id)">
                  <router-link to="/3d/Scene">
                    <svg
                      class="fill-black crops3d-icon-active mx-auto"
                      xmlns="http://www.w3.org/2000/svg"
                      width="20.377"
                      height="21.432"
                      viewBox="0 0 30.377 31.432"
                    >
                      <g
                        id="Gruppe_143"
                        data-name="Gruppe 143"
                        transform="translate(-53.469 -373.116)"
                      >
                        <path
                          id="Pfad_148"
                          data-name="Pfad 148"
                          d="M4.838,0H1.026A.953.953,0,0,0,.073.953V4.829a.953.953,0,1,0,1.906,0V1.906H4.838A.953.953,0,1,0,4.838,0Z"
                          transform="translate(53.396 373.116)"
                        />
                        <path
                          id="Pfad_149"
                          data-name="Pfad 149"
                          d="M426.718,0h-3.812a.953.953,0,1,0,0,1.906h2.859V4.829a.953.953,0,0,0,1.906,0V.953A.953.953,0,0,0,426.718,0Z"
                          transform="translate(-343.826 373.116)"
                        />
                        <path
                          id="Pfad_150"
                          data-name="Pfad 150"
                          d="M4.837,424.757H1.978v-2.923a.953.953,0,1,0-1.906,0v3.876a.953.953,0,0,0,.953.953H4.837a.953.953,0,1,0,0-1.906Z"
                          transform="translate(53.397 -22.124)"
                        />
                        <path
                          id="Pfad_151"
                          data-name="Pfad 151"
                          d="M426.718,420.881a.953.953,0,0,0-.953.953v2.923h-2.859a.953.953,0,1,0,0,1.906h3.812a.953.953,0,0,0,.953-.953v-3.876A.953.953,0,0,0,426.718,420.881Z"
                          transform="translate(-343.826 -22.124)"
                        />
                        <path
                          id="Pfad_152"
                          data-name="Pfad 152"
                          d="M57.928,7.553,45.66.125a.848.848,0,0,0-.883,0L32.5,7.553a.932.932,0,0,0-.439.8s0,0,0,.005V23.083a.931.931,0,0,0,.448.8l12.265,7.423a.848.848,0,0,0,.883,0l12.26-7.423.006,0a.881.881,0,0,0,.442-.787s0-.007,0-.011V8.354s0,0,0-.005A.931.931,0,0,0,57.928,7.553ZM44.337,28.914l-9.624-5.827,7.419-4.446a.943.943,0,0,0,.326-1.257.861.861,0,0,0-1.2-.341l-7.431,4.45V9.94l10.512,6.309Zm.881-14.26L34.712,8.346,45.218,1.985,55.724,8.346Zm11.394,6.839-7.432-4.45a.861.861,0,0,0-1.2.341.943.943,0,0,0,.326,1.257l7.419,4.446L46.1,28.914V16.249L56.612,9.94V21.494Z"
                          transform="translate(23.439 373.116)"
                        />
                      </g>
                    </svg>
                  </router-link>
                </div>
              </q-td>
            </q-tr>
          </template>
          <template v-slot:top-right>
            <q-select
              v-model="visColsBedTable"
              multiple
              outlined
              dense
              rounded
              options-dense
              :display-value="$q.lang.table.columns"
              emit-value
              map-options
              :options="columns"
              option-value="name"
              style="min-width: 120px"
              class="mx-2"
            />
            <q-input
              outlined
              dense
              rounded
              v-model="input"
              placeholder="search"
              style="width: 150px"
            >
              <template v-slot:prepend>
                <q-icon name="search" class="search-icon" />
              </template>
            </q-input>
          </template>
        </q-table>
      </div>
      <div v-else>
        <q-table
          ref="table"
          :rows="crops.plants"
          :columns="columns"
          row-key="name"
          class="crops-table no-shadow crops-table-hover"
          :pagination="pagination()"
          virtual-scroll
          :visible-columns="visColsCropsTable"
          :rows-per-page-options="[0]"
          hide-bottom
          :loading="isLoadingCrops"
          color="primary"
        >
          <template v-slot:top-left>
            <div class="row">
              <button
                @click="(cropstable = !cropstable), cropsStore().resetCrops()"
              >
                <q-icon name="arrow_back_ios" style="font-size: 20px" />
              </button>
              <div class="ml-3 text-xl">
                {{ activeRow?.id }}
              </div>
            </div>
          </template>
          <template v-slot:top-right>
            <q-select
              v-model="visColsCropsTable"
              multiple
              outlined
              dense
              rounded
              options-dense
              :display-value="$q.lang.table.columns"
              emit-value
              map-options
              :options="visibleColumnsCrops"
              option-value="name"
              style="min-width: 120px"
              class="mx-2"
            />

            <q-input
              outlined
              dense
              rounded
              v-model="input"
              placeholder="search"
              style="width: 150px"
            >
              <template v-slot:prepend>
                <q-icon name="search" class="search-icon" />
              </template>
            </q-input>
          </template>
          <template #body="props">
            <q-tr no-hover :props="props" :key="props.row.id">
              <q-td key="location" :props="props">
                {{ props.row.bed_id }}
              </q-td>

              <q-td key="plant" :props="props">
                {{ props.row.plant }}
              </q-td>

              <q-td key="variety" :props="props">
                {{ props.row.variety }}
              </q-td>

              <q-td key="soil_humidity" :props="props">
                {{ props.row.soil_humidity }}
              </q-td>

              <q-td key="health" :props="props">
                <div class="flex flex-row w-24 text-center">
                  <div
                    class="round-badge mx-1 text-black text-bold transition hover:scale-125"
                    v-for="h in props.row.health"
                    :key="h"
                    :class="{
                      'bg-n/a': h.loglevel === 0,
                      'bg-ok': h.loglevel === 1,
                      'bg-warning-custom': h.loglevel === 2,
                      'bg-danger': h.loglevel === 3,
                    }"
                  >
                    {{ getShortcut(h.type) }}
                    <status-popup
                      :health="h"
                      :plant="props.row.plant"
                      :props="props"
                      @remove-clicked="rowClicked(props.row.id)"
                    ></status-popup>
                  </div>
                </div>
              </q-td>

              <q-td key="harvest" :props="props">
                {{ props.row.harvest }}
              </q-td>

              <q-td key="yield" :props="props">
                {{ roundTwoDec(props.row.yield) }}
              </q-td>

              <q-td :props="props" key="3d">
                <div @click="setCropId(props.row.id)">
                  <router-link to="/3d/Scene">
                    <svg
                      class="fill-black crops3d-icon-active mx-auto"
                      xmlns="http://www.w3.org/2000/svg"
                      width="20.377"
                      height="21.432"
                      viewBox="0 0 30.377 31.432"
                    >
                      <g
                        id="Gruppe_143"
                        data-name="Gruppe 143"
                        transform="translate(-53.469 -373.116)"
                      >
                        <path
                          id="Pfad_148"
                          data-name="Pfad 148"
                          d="M4.838,0H1.026A.953.953,0,0,0,.073.953V4.829a.953.953,0,1,0,1.906,0V1.906H4.838A.953.953,0,1,0,4.838,0Z"
                          transform="translate(53.396 373.116)"
                        />
                        <path
                          id="Pfad_149"
                          data-name="Pfad 149"
                          d="M426.718,0h-3.812a.953.953,0,1,0,0,1.906h2.859V4.829a.953.953,0,0,0,1.906,0V.953A.953.953,0,0,0,426.718,0Z"
                          transform="translate(-343.826 373.116)"
                        />
                        <path
                          id="Pfad_150"
                          data-name="Pfad 150"
                          d="M4.837,424.757H1.978v-2.923a.953.953,0,1,0-1.906,0v3.876a.953.953,0,0,0,.953.953H4.837a.953.953,0,1,0,0-1.906Z"
                          transform="translate(53.397 -22.124)"
                        />
                        <path
                          id="Pfad_151"
                          data-name="Pfad 151"
                          d="M426.718,420.881a.953.953,0,0,0-.953.953v2.923h-2.859a.953.953,0,1,0,0,1.906h3.812a.953.953,0,0,0,.953-.953v-3.876A.953.953,0,0,0,426.718,420.881Z"
                          transform="translate(-343.826 -22.124)"
                        />
                        <path
                          id="Pfad_152"
                          data-name="Pfad 152"
                          d="M57.928,7.553,45.66.125a.848.848,0,0,0-.883,0L32.5,7.553a.932.932,0,0,0-.439.8s0,0,0,.005V23.083a.931.931,0,0,0,.448.8l12.265,7.423a.848.848,0,0,0,.883,0l12.26-7.423.006,0a.881.881,0,0,0,.442-.787s0-.007,0-.011V8.354s0,0,0-.005A.931.931,0,0,0,57.928,7.553ZM44.337,28.914l-9.624-5.827,7.419-4.446a.943.943,0,0,0,.326-1.257.861.861,0,0,0-1.2-.341l-7.431,4.45V9.94l10.512,6.309Zm.881-14.26L34.712,8.346,45.218,1.985,55.724,8.346Zm11.394,6.839-7.432-4.45a.861.861,0,0,0-1.2.341.943.943,0,0,0,.326,1.257l7.419,4.446L46.1,28.914V16.249L56.612,9.94V21.494Z"
                          transform="translate(23.439 373.116)"
                        />
                      </g>
                    </svg>
                  </router-link>
                </div>
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Ref } from "vue";
import type { Crop } from "@/types/crop";
import { storeToRefs } from "pinia";
import { cropsStore } from "@/stores/cropsStore";
import { ref, onMounted } from "vue";
import type { QTable, QTableProps } from "quasar";
import StatusPopup from "@/components/StatusPopup.vue";
import type { Crops } from "@/types/crops";
import type { Beds } from "@/types/beds";
import { bedStore } from "@/stores/bedStore";

let crops: Ref<Crops> = storeToRefs(cropsStore()).getCrops;
const isLoadingBeds: Ref<boolean | undefined> = storeToRefs(
  bedStore()
).getIsLoading;

const isLoadingCrops: Ref<boolean | undefined> = storeToRefs(
  cropsStore()
).getIsLoading;

function setBedId(bedId: number) {
  bedStore().setSelectedBedId(bedId);
}

function setCropId(cropId: string) {
  cropsStore().setSelectedCropId(cropId);
}

const table = ref<null | InstanceType<typeof QTable>>(null);
const cropstable = ref<boolean>(false);
const activeRow = ref<Crop>();

const props = defineProps<{
  title: string;
  visibleColumnsBeds: string[];
  visibleColumnsCrops: string[];
  beds: Beds;
  columns: QTableProps["columns"];
}>();

let visColsBedTable = ref(props.visibleColumnsBeds);
let visColsCropsTable = ref(props.visibleColumnsCrops);
let input = ref<string>("");

const emit = defineEmits<{
  (event: "rowEnter", cropId: number): void;
  (event: "rowLeave", cropId: number): void;
}>();

defineExpose({
  setRowActiveBed,
  setRowInactiveBed,
  setRowActivePlant: setRowActiveCrop,
  setRowInactivePlant: setRowInactiveCrop,
});

onMounted(() => {
  // Reset selected Crop to empty string when table is loaded
  setCropId("");
});

function roundTwoDec(num: number): number {
  return Math.round(num * 100) / 100;
}

function getShortcut(healthType: string): string {
  return Array.from(healthType)[0].toUpperCase();
}

function getRowByBedId(bedId: number): HTMLTableRowElement | undefined {
  const tableValue: any = table.value;
  if (tableValue) {
    const filteredSortedRows = tableValue.filteredSortedRows;
    if (table.value?.rows?.length) {
      for (let i = 0; i < table.value.rows.length; i++) {
        if (bedId == table.value.rows[i].id) {
          const rowIndex = filteredSortedRows.indexOf(table.value.rows[i]);
          return document
            .getElementsByClassName("q-table")[0]
            .getElementsByTagName("tr")[rowIndex + 2];
        }
      }
    }
  }
}

function getRowByCropId(cropId: string): HTMLTableRowElement | undefined {
  const tableValue: any = table.value;
  if (tableValue) {
    const filteredSortedRows = tableValue.filteredSortedRows;
    if (table.value?.rows?.length) {
      for (let i = 0; i < table.value.rows.length; i++) {
        if (cropId === table.value.rows[i].id) {
          const rowIndex = filteredSortedRows.indexOf(table.value.rows[i]);
          return document
            .getElementsByClassName("q-table")[0]
            .getElementsByTagName("tr")[rowIndex + 2];
        }
      }
    }
  }
}

function setRowActiveBed(bedId: number): void {
  const row: HTMLTableRowElement | undefined = getRowByBedId(bedId);
  if (row) {
    row.classList.add("crops-row-active");
  }
}

function setRowActiveCrop(cropId: string): void {
  const row: HTMLTableRowElement | undefined = getRowByCropId(cropId);
  if (row) {
    row.classList.add("crops-row-active");
  }
}

function setRowInactiveBed(bedId: number): void {
  const row: HTMLTableRowElement | undefined = getRowByBedId(bedId);
  if (row) {
    row.classList.remove("crops-row-active");
  }
}

function setRowInactiveCrop(cropId: string): void {
  const row: HTMLTableRowElement | undefined = getRowByCropId(cropId);
  if (row) {
    row.classList.remove("crops-row-active");
  }
}

function rowEnter(id: number): void {
  emit("rowEnter", id);
}

function rowLeave(id: number): void {
  emit("rowLeave", id);
}

function rowClicked(bedId: number): void {
  bedStore().setSelectedBedId(bedId);
  const bed = storeToRefs(bedStore()).getSelectedBed;
  if (bed.value) {
    cropsStore().loadDataFromApi(bed.value.plants);
  }
}

function pagination(): { sortBy: string; rowsPerPage: number } {
  return {
    sortBy: "location",
    rowsPerPage: 0,
  };
}
</script>
