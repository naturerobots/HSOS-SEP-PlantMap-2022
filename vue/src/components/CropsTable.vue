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
                  'bg-yellow': props.value == 'Okay',
                }"
                :label="props.value"
              />
            </div>
          </q-td>
        </template>

        <template v-slot:body-cell-3d="props">
          <q-td :props="props">
            <div>
              <router-link to="/3d"
                ><q-btn flat rounded
                  ><img src="@/assets/icons/3dBlack.svg" /></q-btn
              ></router-link>
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

<style lang="sass">
.header-table
  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #F5F5F5
  thead tr th
    position: sticky
    z-index: 1
    font-weight: bold
    color: #9C9B9B
  thead tr:first-child th
    top: 0
  tbody tr:nth-child(even)
    background-color: #F5F5F5
  tbody tr
      &:hover
        background: #B0BAB6

  /* this is when the loading indicator appears */
  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
</style>
