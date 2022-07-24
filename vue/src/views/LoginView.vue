<template>
  <split-layout>
    <div class="row-span-4 row-start-3">
      <login-form></login-form>
    </div>
  </split-layout>
</template>

<script setup lang="ts">
import LoginForm from "@/components/login/LoginForm.vue";
import SplitLayout from "@/components/layout/SplitLayout.vue";
</script>
