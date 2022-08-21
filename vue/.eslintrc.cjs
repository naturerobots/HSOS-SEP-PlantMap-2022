/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
  root: true,
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/eslint-config-typescript/recommended",
    "@vue/eslint-config-prettier",
  ],
  env: {
    "vue/setup-compiler-macros": true,
  },

  rules: {
    "@typescript-eslint/no-this-alias": [
      "error",
      {
        allowDestructuring: true,
        // Allow `const { props, state } = this`; false by default
        allowedNames: ["self"], // Allow `const self = this`; `[]` by default
      },
    ],
  },
};
