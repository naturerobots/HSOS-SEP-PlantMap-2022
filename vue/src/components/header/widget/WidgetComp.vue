<template>
  <q-select
    dir="rtl"
    class="widget"
    v-model="widgetModel"
    :options="options"
    :display-value="label"
    hide-dropdown-icon
    multiple
    borderless
    popup-content-class="widget-content"
    menu-self="top middle"
    menu-anchor="bottom left"
    options-selected-class="widget-content-selected"
    option-value="name"
    option-label="label"
    map-options
    emit-value
  >
    <!-- TODO: check menu-anchor & menu-self -> when the website reloads, you can see the position changes -->
    <template v-slot:option="scope">
      <q-item v-bind="scope.itemProps">
        <q-item-section>
          <q-item-label v-html="scope.opt.label"></q-item-label>
        </q-item-section>
        <q-item-section avatar>
          <!-- TODO: adjust color -->
          <q-icon
            v-if="scope.selected"
            name="check"
            class="text-[#707070]"
          ></q-icon>
          <q-icon v-else name="none"></q-icon>
        </q-item-section>
      </q-item>
    </template>
  </q-select>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type { QSelect } from "quasar";
import type { WidgetOption } from "@/types/widgetOption";

const widgetModel = ref<InstanceType<typeof QSelect> | null>(null);

defineProps<{
  label: string;
  options: WidgetOption[];
}>();
</script>
