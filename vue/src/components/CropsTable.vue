<template>
  <div class="card h-full w-full mr-24">
    <div class="overflow-x-auto overflow-y-auto rounded-2xl">
      <div v-if="!cropstable">
        <q-table
          ref="table"
          @row-click="rowclicked(0)"
          separator="none"
          class="crops-table no-shadow crops-table-hover"
          :title="title"
          :rows="crops"
          :columns="columns"
          no-data-label="I didn't find anything for you"
          row-key="id"
          :filter="input"
          :visible-columns="visCols"
          :pagination="pagination()"
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
                  rowclicked(props.row.id),
                  (activeRow = props.row)
              "
            >
              <q-td key="location" :props="props">
                {{ props.row.location }}
              </q-td>

              <q-td key="plant" :props="props">
                {{ props.row.plant }}
              </q-td>

              <q-td key="variety" :props="props">
                {{ props.row.variety }}
              </q-td>

              <q-td key="soilHumidity" :props="props">
                {{ props.row.soilHumidity }}
              </q-td>

              <q-td key="health" :props="props">
                <q-badge
                  rounded
                  class="mx-1 text-black text-bold transition hover:scale-125"
                  v-for="h in props.row.health"
                  :key="h"
                  :class="{
                    'bg-blue': h.loglevel === 0,
                    'bg-green': h.loglevel === 1,
                    'bg-warning': h.loglevel === 2,
                    'bg-red': h.loglevel === 3,
                  }"
                  :label="h.shortcut"
                >
                  <status-popup
                    :health="h"
                    :plant="props.row.plant"
                    :props="props"
                    @remove-clicked="rowclicked(props.row.id)"
                  ></status-popup>
                </q-badge>
              </q-td>

              <q-td key="status" :props="props">
                {{ props.row.status }}
              </q-td>

              <q-td key="harvest" :props="props">
                {{ props.row.harvest }}
              </q-td>

              <q-td key="yield" :props="props">
                {{ props.row.yield }}
              </q-td>

              <q-td :props="props" key="3d">
                <div>
                  <router-link to="/3d">
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
              v-model="visCols"
              multiple
              outlined
              dense
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
              v-model="input"
              placeholder="Search"
              style="width: 150px"
            >
              <template v-slot:append>
                <q-icon name="search" />
              </template>
            </q-input>
          </template>
        </q-table>
      </div>
      <div v-else>
        <q-table
          :rows="rows2"
          :columns="columns2"
          row-key="name"
          class="crops-table no-shadow crops-table-hover"
          separator="none"
          :pagination="pagination()"
        >
          <template v-slot:top-left>
            <div class="row">
              <button
                @click="(cropstable = !cropstable), $emit('removePolygon')"
              >
                <q-icon name="arrow_back_ios" style="font-size: 20px" />
              </button>
              <div class="ml-3 text-xl">
                {{ activeRow?.location }} - {{ activeRow?.plant }}
              </div>
            </div>
          </template>
          <template v-slot:top-right>
            <q-select
              v-model="visCols"
              multiple
              outlined
              dense
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
              v-model="input"
              placeholder="Search"
              style="width: 150px"
            >
              <template v-slot:append>
                <q-icon name="search" />
              </template>
            </q-input>
          </template>
        </q-table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Ref } from "vue";
import type { Crop } from "../types/crop";
import { storeToRefs } from "pinia";
import { cropsStore } from "../stores/cropsStore";
import { ref } from "vue";
import type { QTable, QTableProps } from "quasar";
import StatusPopup from "@/components/StatusPopup.vue";

const crops: Ref<Crop[]> = storeToRefs(cropsStore()).getCrops;
let input = ref<string>("");
const table = ref<null | InstanceType<typeof QTable>>(null);

const cropstable = ref<boolean>(false);

const activeRow = ref<Crop>();

const props = defineProps<{
  title: string;
  visibleColumns: string[];
  crops: Crop[];
}>();

const emit = defineEmits<{
  (event: "rowEnter", cropsId: number): void;
  (event: "rowLeave", cropsId: number): void;
  (event: "rowClick", cropsId: number): void;
  (event: "removePolygon"): void;
}>();

defineExpose({
  setRowActive,
  setRowInactive,
  setRowClicked,
});

function getRowByCropsId(cropsId: number): HTMLTableRowElement | undefined {
  const tableValue: any = table.value;
  const filteredSortedRows = tableValue.filteredSortedRows;
  if (table.value?.rows?.length) {
    for (let i = 0; i < table.value.rows.length; i++) {
      if (cropsId == table.value.rows[i].id) {
        const rowIndex = filteredSortedRows.indexOf(table.value.rows[i]);
        return document
          .getElementsByClassName("q-table")[0]
          .getElementsByTagName("tr")[rowIndex + 1];
      }
    }
  }
}

function removeClickedRow(): void {
  console.log("removeClickedRow");
  const tableValue: any = table.value;
  const filteredSortedRows = tableValue.filteredSortedRows;
  if (table.value?.rows?.length) {
    for (let i = 0; i < table.value.rows.length; i++) {
      const rowIndex = filteredSortedRows.indexOf(table.value.rows[i]);
      const row: HTMLTableRowElement = document
        .getElementsByClassName("q-table")[0]
        .getElementsByTagName("tr")[rowIndex + 1];
      if (row.classList != null) {
        if (row.classList.contains("crops-row-clicked")) {
          row.classList.remove("crops-row-clicked");
        }
      }
    }
  }
}

function setRowActive(cropsId: number): void {
  const row: HTMLTableRowElement | undefined = getRowByCropsId(cropsId);
  if (row) {
    row.classList.add("crops-row-active");
  }
}

function setRowClicked(cropsId: number): void {
  console.log("setRowClicked");
  const row: HTMLTableRowElement | undefined = getRowByCropsId(cropsId);
  // if (row) {
  //   removeClickedRow();
  //   row.classList.add("crops-row-clicked");
  //   let element: HTMLElement = document.getElementsByClassName('crops-row-clicked')[0] as HTMLElement;
  //   element.click();
  // }
  if (row) {
    if (row.classList.contains("crops-row-clicked")) {
      removeClickedRow();
      console.log("remove");
      row.classList.remove("crops-row-clicked");
      emit("rowClick", cropsId);
    } else {
      removeClickedRow();
      console.log("add");
      // row.classList.add("crops-row-clicked");
      let element: HTMLElement = document.getElementsByClassName(
        "crops-row-active"
      )[0] as HTMLElement;
      element.click();
    }
  }
}

function setRowInactive(cropsId: number): void {
  const row: HTMLTableRowElement | undefined = getRowByCropsId(cropsId);
  if (row) {
    row.classList.remove("crops-row-active");
  }
}

function rowEnter(cropsId: number): void {
  emit("rowEnter", cropsId);
}

function rowLeave(cropsId: number): void {
  emit("rowLeave", cropsId);
}

function rowclicked(cropsId: number): void {
  console.log("rowClicked " + cropsId);

  // removeClickedRow();
  emit("rowClick", cropsId);
  const row: HTMLTableRowElement | undefined = getRowByCropsId(cropsId);
  if (row) {
    if (row.classList.contains("crops-row-clicked")) {
      removeClickedRow();
      console.log("remove");
      row.classList.remove("crops-row-clicked");
    } else {
      removeClickedRow();
      console.log("add");
      row.classList.add("crops-row-clicked");
    }
  }
}

let visCols = ref(props.visibleColumns);

function pagination(): { sortBy: string; rowsPerPage: number } {
  return {
    sortBy: "location",
    rowsPerPage: 0,
  };
}

const columns: QTableProps["columns"] = [
  // {
  //   name: "id",
  //   // required: true,
  //   label: "ID",
  //   align: "left",
  //   field: (row: any) => row.id,
  //   format: (val: any) => `${val}`,
  //   sortable: true,
  // },
  {
    name: "location",
    align: "left",
    label: "Location",
    field: "location",
    sortable: true,
  },
  {
    name: "plant",
    align: "left",
    label: "Plant",
    field: "plant",
    sortable: true,
  },
  {
    name: "variety",
    align: "left",
    label: "Variety",
    field: "variety",
    sortable: true,
  },

  {
    name: "soilHumidity",
    align: "left",
    label: "Humidity",
    field: "soilHumidity",
    sortable: true,
    sort: (a: any, b: any) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "health",
    align: "center",
    label: "Health",
    field: "health",
    sortable: true,
  },
  {
    name: "status",
    align: "left",
    label: "Status",
    field: "status",
    sortable: true,
  },
  {
    name: "harvest",
    align: "left",
    label: "Harvest",
    field: "harvest",
    sortable: true,
    sort: (a: any, b: any) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "yield",
    align: "left",
    label: "Yield",
    field: "yield",
    sortable: true,
  },
  { name: "3d", align: "left", label: "3D", field: "3d", sortable: false },
];

// let visibleColumns = ref([
//   columns[0].name,
//   columns[1].name,
//   columns[2].name,
//   columns[3].name,
//   columns[4].name,
//   columns[5].name,
//   columns[6].name,
//   columns[7].name,
//   columns[8].name,
//   columns[9].name,
// ]);

const columns2 = [
  {
    name: "name",
    required: true,
    label: "Dessert",
    align: "left",
    field: (row) => row.name,
    format: (val) => `${val}`,
    sortable: true,
  },
  {
    name: "calories",
    align: "center",
    label: "Calories",
    field: "calories",
    sortable: true,
  },
  { name: "fat", label: "Fat (g)", field: "fat", sortable: true },
  { name: "carbs", label: "Carbs (g)", field: "carbs" },
  { name: "protein", label: "Protein (g)", field: "protein" },
  { name: "sodium", label: "Sodium (mg)", field: "sodium" },
  {
    name: "calcium",
    label: "Calcium (%)",
    field: "calcium",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "iron",
    label: "Iron (%)",
    field: "iron",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
];

const rows2 = [
  {
    name: "Frozen Yogurt",
    calories: 159,
    fat: 6.0,
    carbs: 24,
    protein: 4.0,
    sodium: 87,
    calcium: "14%",
    iron: "1%",
  },
  {
    name: "Ice cream sandwich",
    calories: 237,
    fat: 9.0,
    carbs: 37,
    protein: 4.3,
    sodium: 129,
    calcium: "8%",
    iron: "1%",
  },
  {
    name: "Eclair",
    calories: 262,
    fat: 16.0,
    carbs: 23,
    protein: 6.0,
    sodium: 337,
    calcium: "6%",
    iron: "7%",
  },
  {
    name: "Cupcake",
    calories: 305,
    fat: 3.7,
    carbs: 67,
    protein: 4.3,
    sodium: 413,
    calcium: "3%",
    iron: "8%",
  },
  {
    name: "Gingerbread",
    calories: 356,
    fat: 16.0,
    carbs: 49,
    protein: 3.9,
    sodium: 327,
    calcium: "7%",
    iron: "16%",
  },
  {
    name: "Jelly bean",
    calories: 375,
    fat: 0.0,
    carbs: 94,
    protein: 0.0,
    sodium: 50,
    calcium: "0%",
    iron: "0%",
  },
  {
    name: "Lollipop",
    calories: 392,
    fat: 0.2,
    carbs: 98,
    protein: 0,
    sodium: 38,
    calcium: "0%",
    iron: "2%",
  },
  {
    name: "Honeycomb",
    calories: 408,
    fat: 3.2,
    carbs: 87,
    protein: 6.5,
    sodium: 562,
    calcium: "0%",
    iron: "45%",
  },
  {
    name: "Donut",
    calories: 452,
    fat: 25.0,
    carbs: 51,
    protein: 4.9,
    sodium: 326,
    calcium: "2%",
    iron: "22%",
  },
  {
    name: "KitKat",
    calories: 518,
    fat: 26.0,
    carbs: 65,
    protein: 7,
    sodium: 54,
    calcium: "12%",
    iron: "6%",
  },
];
</script>
