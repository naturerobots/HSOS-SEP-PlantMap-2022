<script setup lang="ts"></script>

<template>
  <div class="sidebar">
    <div class="sidebar-content">
      <nav class="bg-primary sidebar-nav">
        <div class="mt-10 mb-10">
          <router-link :to="'/home'">
            <img
              src="@/assets/img/logo_small.svg"
              class="w-10 h-10 mb-3 mx-auto"
            />
            <!-- ToDo: Create Image Component & custom class for this -->
          </router-link>
          <div class="mt-10">
            <ul>
              <!-- ToDo: Edit icons & links -->
              <li class="my-12 text-center">1</li>
              <li class="my-12 text-center">2</li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>
