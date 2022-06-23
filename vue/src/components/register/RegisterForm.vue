<template>
  <div class="m-auto max-w-xl px-14">
    <div class="mb-6">
      <h3 class="text-3xl font-bold">Sign up</h3>
      <p class="text-secondary pt-2 font-bold">
        Sign up for free. Please enter your details.
      </p>
    </div>
    <div class="grid grid-cols-4 gap-4 place-items-stretch">
      <div class="col-span-2 space-y-2">
        <label class="font-bold text-black"> Last Name </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Enter Last Name"
        />
      </div>
      <div class="col-span-2 space-y-2">
        <label class="font-bold text-black"> First Name </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Enter First Name"
        />
      </div>
      <div class="col-span-3 space-y-2">
        <label class="font-bold text-black"> Street </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Enter Street Name"
        />
      </div>
      <div class="col-span-1 space-y-2">
        <label class="font-bold text-black"> Number </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Number"
        />
      </div>
      <div class="col-span-2 space-y-2">
        <label class="font-bold text-black"> City </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Enter City"
        />
      </div>
      <div class="col-span-2 space-y-2">
        <label class="font-bold text-black"> Zip/Postal Code </label>
        <input
          class="w-full text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Enter Zip/Postal Code"
        />
      </div>
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
          placeholder="Enter Password"
        />
      </div>
      <div class="col-span-4 space-y-2">
        <label class="font-bold text-black"> Repeat Password </label>
        <input
          class="w-full content-center text-base px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-primary"
          type="text"
          placeholder="Repeat Password"
        />
      </div>
      <div class="col-span-4 space-y-2 pt-3">
        <button
          type="submit"
          class="w-full flex justify-center bg-primary text-white p-3 rounded-full tracking-wide font-bold shadow-lg"
        >
          Sign up
        </button>
        <p class="text-center pt-3 text-secondary">
          Already a member?
          <router-link to="/login" class="pl-1 text-black font-bold">
            Login
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>
