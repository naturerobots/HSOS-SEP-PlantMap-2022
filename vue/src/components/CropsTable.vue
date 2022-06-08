<template>
  <q-card class="h-full w-full shadow-1 bg-light">
    <div class="overflow-x-auto overflow-y-auto">
      <q-table
        @row-click="rowclicked()"
        separator="none"
        class="header-table"
        title="Overview"
        :rows="crops"
        :columns="columns"
        row-key="name"
        :filter="input"
        :visible-columns="visibleColumns"
      >
        <template v-slot:top-right>
          <q-input outlined dense v-model="input" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </template>

        <template v-slot:body-cell-health="props">
          <q-td :props="props">
            <div>
              <q-badge
                :class="{
                  'bg-red': props.value == 'Bad',
                  'bg-green': props.value == 'Good',
                  'bg-warning': props.value == 'Okay',
                }"
                :label="props.value"
              />
            </div>
          </q-td>
        </template>

        <template v-slot:body-cell-3d="props">
          <q-td :props="props">
            <div>
              <router-link to="/3d">
                <svg
                  class="fill-black hover-icon mx-auto"
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
        </template>

        <template v-slot:top-left>
          <q-select
            v-model="visibleColumns"
            multiple
            outlined
            dense
            options-dense
            :display-value="$q.lang.table.columns"
            emit-value
            map-options
            :options="columns"
            option-value="name"
            style="min-width: 150px"
          />
        </template>
      </q-table>
    </div>
  </q-card>
</template>

<script setup lang="ts">
import type { Ref } from "vue";
import type { Crop } from "../types/crop";
import { storeToRefs } from "pinia";
import { cropsStore } from "../stores/cropsStore";
import { ref } from "vue";

const crops: Ref<Crop[]> = storeToRefs(cropsStore()).getCrops;
let input = ref("");

function rowclicked() {
  console.log("rowClicked");
}
const columns = [
  {
    name: "id",
    required: true,
    label: "ID",
    align: "left",
    field: (row: any) => row.id,
    format: (val: any) => `${val}`,
    sortable: true,
  },
  {
    name: "plant",
    align: "left",
    label: "PLANT",
    field: "plant",
    sortable: true,
  },
  {
    name: "variety",
    align: "left",
    label: "VARIETY",
    field: "variety",
    sortable: true,
  },
  {
    name: "location",
    align: "left",
    label: "LOCATION",
    field: "location",
    sortable: true,
  },
  {
    name: "soilHumidity",
    align: "left",
    label: "HUMIDITY",
    field: "soilHumidity",
    sortable: true,
    sort: (a: any, b: any) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "health",
    align: "left",
    label: "HEALTH",
    field: "health",
    sortable: true,
  },
  {
    name: "status",
    align: "left",
    label: "STATUS",
    field: "status",
    sortable: true,
  },
  {
    name: "harvest",
    align: "left",
    label: "HARVEST",
    field: "harvest",
    sortable: true,
    sort: (a: any, b: any) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "yield",
    align: "left",
    label: "YIELD",
    field: "yield",
    sortable: true,
  },
  { name: "3d", align: "left", label: "3D", field: "3d", sortable: false },
];

let visibleColumns = ref([
  columns[0].name,
  columns[1].name,
  columns[2].name,
  columns[3].name,
  columns[4].name,
  columns[5].name,
  columns[6].name,
  columns[7].name,
  columns[8].name,
  columns[9].name,
]);
</script>

<style lang="scss">
.hover-icon:hover {
  fill: $primary;
}

.header-table .q-table__top,
.q-table__bottom,
thead tr:first-child th,
tbody tr:nth-child(even) {
  background-color: #f8f8fa;
}

.header-table thead tr th {
  position: sticky;
  z-index: 1;
  font-weight: bold;
  color: #9c9b9b;
}

// .header-table tbody tr:nth-child(even) {
//     background-color: #F5F5F5;
// }

.header-table tbody tr:hover {
  background: #f4f4f8;
}

/* this is when the loading indicator appears */
.header-table .q-table--loading thead tr:last-child th {
  /* height of all previous header rows */
  top: 48px;
}
</style>
