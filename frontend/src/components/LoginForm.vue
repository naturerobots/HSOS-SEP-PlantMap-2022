<template>
  <div class="card w-96 bg-light shadow-xl">
    <div class="card-body">
      <img
        src="@/assets/img/logo_small_color.svg"
        class="w-16 h-16 mb-3 mx-auto"
      />
      <div class="grid justify-items-center">
        <h2 class="card-title">Login to your account</h2>
      </div>
      <div class="py-4">
        <div class="form-control">
          <input
            type="email"
            placeholder="E-Mail"
            class="input input-bordered w-full max-w-xs my-2"
          />
        </div>
        <div class="form-control">
          <input
            type="password"
            placeholder="Password"
            class="input input-bordered w-full max-w-xs my-2"
          />
          <div class="grid justify-items-end text-secondary-focus text-sm">
            <a href="#">Forgot password?</a>
          </div>
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary">Login</button>
        </div>
        <div
          class="grid justify-items-center pt-2 text-secondary-focus text-sm"
        >
          <a href="#">You don't have an account?</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>
