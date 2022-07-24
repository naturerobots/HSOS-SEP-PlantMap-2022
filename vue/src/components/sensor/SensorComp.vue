<template>
  <div class="card bg-white">
    <div class="card-title">Soil Parameter</div>
    <div class="overflow-x-auto overflow-y-auto">
      <q-table
        ref="table"
        flat
        class="sensor-table"
        :rows="sensors"
        :columns="columns"
        row-key="name"
        virtual-scroll
        :rows-per-page-options="[0]"
        hide-bottom
      >
        <template v-slot:body="props">
          <q-tr
            class="hover:sensor-row-active"
            no-hover
            :key="props.row.id"
            :props="props"
            @mouseenter="rowEnter(props.row.id)"
            @mouseleave="rowLeave(props.row.id)"
          >
            <q-td key="name" :props="props">
              {{ props.row.name }}
            </q-td>
            <q-td key="moisture_value" :props="props">
              {{ props.row.moisture_value }} {{ props.row.moisture_unit }}
            </q-td>
            <q-td key="temp_value" :props="props">
              {{ props.row.temp_value }} {{ props.row.temp_unit }}
            </q-td>
            <q-td key="ph_value" :props="props">
              {{ props.row.ph_value }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Sensor } from "@/types/sensor";
import type { QTable, QTableProps } from "quasar";
import { ref } from "vue";
const table = ref<InstanceType<typeof QTable> | null>(null);

defineProps<{
  sensors: Sensor[];
}>();

const emit = defineEmits<{
  (event: "rowEnter", sensorId: number): void;
  (event: "rowLeave", sensorId: number): void;
}>();

defineExpose({
  setRowActive,
  setRowInactive,
});

//icons for testing
const upGreen = "up_green";
const downGreen = "down_green";
const upRed = "up_red";
const downRed = "down_red";

function getRowBySensorId(sensorId: number): HTMLTableRowElement | undefined {
  if (table.value?.rows?.length) {
    for (let i = 0; i < table.value?.rows?.length; i++) {
      if (sensorId == table.value.rows[i].id) {
        return document
          .getElementsByClassName("q-table")[0]
          .getElementsByTagName("tr")[i + 1];
      }
    }
  }
}

function setRowActive(sensorId: number): void {
  const row: HTMLTableRowElement | undefined = getRowBySensorId(sensorId);
  if (row) {
    row.classList.add("sensor-row-active");
  }
}

function setRowInactive(sensorId: number): void {
  const row: HTMLTableRowElement | undefined = getRowBySensorId(sensorId);
  if (row) {
    row.classList.remove("sensor-row-active");
  }
}

function rowEnter(sensorId: number): void {
  emit("rowEnter", sensorId);
}

function rowLeave(sensorId: number): void {
  emit("rowLeave", sensorId);
}
//TODO: columns
const columns: QTableProps["columns"] = [
  {
    name: "name",
    label: "Name",
    field: "name",
    align: "center",
  },
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
  {
    name: "ph_value",
    label: "PH",
    field: "ph_value",
    align: "left",
  },
];
</script>
