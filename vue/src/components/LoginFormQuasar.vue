<template>
  <div class="p-12 mr-24 bg-light rounded-2xl shadow-2 w-100">
    <div class="mb-6">
      <img
        src="@/assets/img/logo_small_color.svg"
        class="w-16 h-16 mb-3 mx-auto"
      />
      <h3 class="text-center text-2xl font-semibold">
        Sign in to your account
      </h3>
    </div>
    <div class="space-y-5">
      <div class="space-y-2">
        <label class="text-sm font-medium text-gray-700 tracking-wide"
          >Email</label
        >
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type=""
          placeholder="mail@gmail.com"
        />
      </div>
      <div class="space-y-2">
        <label class="text-sm font-medium text-gray-700 tracking-wide">
          Password
        </label>
        <input
          class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type=""
          placeholder="Enter your password"
        />
      </div>
      <div class="flex items-center justify-between">
        <div class="text-sm">
          <a href="#" class="text-secondary hover:text-secondary_hover">
            Forgot your password?
          </a>
        </div>
      </div>
      <div>
        <button
          type="submit"
          class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-semibold shadow-lg"
        >
          Sign in
        </button>
      </div>
      <div
        class="text-center py-2 text-secondary hover:text-secondary_hover text-sm"
      >
        <a href="#">You don't have an account?</a>
      </div>
    </div>
    <div class="pt-5 text-center text-gray-400 text-xs">
      <span>
        Copyright © 2022
        <a
          href="https://naturerobots.de"
          rel=""
          target="_blank"
          title="Nature Robots"
          class="text-primary hover:text-primary_hover"
          >naturerobots</a
        ></span
      >
    </div>
  </div>
</template>

<script setup lang="ts"></script>
