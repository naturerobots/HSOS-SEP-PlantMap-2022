<template>
  <div class="card p-4 bg-white shadow-1">
    <div class="card-title text-h6">Soil parameters</div>
    <div class="rounded-xl overflow-x-auto overflow-y-auto">
      <q-table
        separator="none"
        flat
        class="header-table body-table"
        :rows="sensors"
        :columns="columns"
        row-key="name"
      >
        <template v-slot:body="props">
          <q-tr
            :props="props"
            @mouseenter="rowEnter(props.row.id)"
            @mouseleave="rowLeave(props.row.id)"
          >
            <q-td key="name" :props="props">
              {{ props.row.name }}
            </q-td>
            <q-td key="moisture_value" :props="props">
              {{ props.row.moisture_value }}
            </q-td>
            <q-td key="temp_value" :props="props">
              {{ props.row.temp_value }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Sensor } from "@/types/sensor";

defineProps<{
  sensors: Sensor[];
}>();

const emit = defineEmits<{
  (event: "rowEnter", sensorId: number): void;
  (event: "rowLeave", sensorId: number): void;
}>();
//icons for testing
const upGreen = "up_green";
const downGreen = "down_green";
const upRed = "up_red";
const downRed = "down_red";

function rowEnter(sensorId: number) {
  emit("rowEnter", sensorId);
}

function rowLeave(sensorId: number) {
  emit("rowLeave", sensorId);
}

//TODO: columns
const columns = [
  { name: "name", label: "Name", field: "name", align: "left" },
  {
    name: "moisture_value",
    label: "Moisture",
    field: "moisture_value",
    align: "left",
  },
  {
    name: "temp_value",
    label: "Temperature",
    field: "temp_value",
    align: "left",
  },
];
</script>

<style lang="scss">
.body-table tbody {
  font-weight: bold;
}
</style>
