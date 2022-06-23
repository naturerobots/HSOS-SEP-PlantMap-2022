<template>
  <div class="w-max m-auto px-14">
    <div class="mb-6 text-center">
      <h3 class="text-3xl font-bold">Welcome back</h3>
      <p class="text-secondary pt-2 font-bold">
        Welcome back! Please enter your details.
      </p>
    </div>
    <div class="grid grid-cols-4 gap-4 place-items-stretch">
      <div class="col-span-4 space-y-2">
        <label class="font-bold text-black"> Email </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="email"
          placeholder="Enter Email Address"
        />
      </div>
      <div class="col-span-4 space-y-2">
        <label class="font-bold text-black"> Password </label>
        <input
          class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Password"
        />
      </div>
      <div class="col-span-4 space-y-2 pt-3">
        <button
          type="submit"
          class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
        >
          Login
        </button>
        <p class="text-center pt-3 text-secondary">
          Don't have an account?
          <router-link to="/register" class="pl-1 text-black font-bold">
            Sign up for free
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>
