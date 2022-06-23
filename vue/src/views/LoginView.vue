<template>
  <div class="grid grid-cols-2 place-items-stretch h-full">
    <div class="bg-white grid grid-rows-6 gap-4">
      <div class="row-span-1">
        <div class="flex h-full pl-14">
          <img
            class="w-56"
            src="@/assets/img/logo_with_text.svg"
            alt="Nature Robots"
          />
        </div>
      </div>
      <div class="row-span-4 row-start-3">
        <login-form></login-form>
      </div>
    </div>
    <div class="bg-image bg-cover"></div>
  </div>
</template>

<script setup lang="ts">
import LoginForm from "@/components/login/LoginForm.vue";
</script>
