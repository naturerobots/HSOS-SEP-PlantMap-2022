<template>
  <q-card class="shadow-1">
    <q-card-section>
      <div class="text-center text-h6 text-primary_hover">Soil parameters</div>
    </q-card-section>
    <q-card-section>
      <q-table
        separator="none"
        flat
        class="header-table"
        :rows="rows"
        :columns="columns"
        row-key="name"
      />
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
//icons for testing
const upGreen = "up_green";
const downGreen = "down_green";
const upRed = "up_red";
const downRed = "down_red";

const columns = [
  { name: "probe", label: "Probe", field: "probe", align: "left" },
  { name: "moisture", label: "Moisture", field: "moisture", align: "left" },
  {
    name: "temperature",
    label: "Temperature",
    field: "temperature",
    align: "left",
  },
  { name: "ph", label: "PH", field: "ph", align: "left" },
];

const rows = [
  { probe: "A", moisture: "59%", temperature: "8°C", ph: "4,5" },
  { probe: "B", moisture: "30%", temperature: "9°C", ph: "7,9" },
  { probe: "C", moisture: "48%", temperature: "6°C", ph: "7,5" },
];
</script>

<style lang="sass"></style>
