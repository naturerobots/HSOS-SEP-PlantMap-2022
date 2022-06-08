<template>
  <q-card class="w-96 bg-background shadow-xl">
    <div class="card-body">
      <img
        src="@/assets/img/logo_small_color.svg"
        class="w-16 h-16 mb-3 mx-auto"
      />
      <div class="grid justify-items-center">
        <div class="text-3xl">Login to your account</div>
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
          <div class="grid justify-items-end text-secondary_hover text-sm">
            <a href="#">Forgot password?</a>
          </div>
        </div>
        <div class="form-control mt-6">
          <button class="btn bg-primary no-border">Login</button>
        </div>
        <div
          class="grid justify-items-center pt-2 text-secondary_hover text-sm"
        >
          <a href="#">You don't have an account?</a>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script setup lang="ts"></script>
