import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import "./assets/base.css";
import { Quasar } from "quasar";
// Import icon libraries
import "@quasar/extras/material-icons/material-icons.css";
// // Import Quasar css
import "quasar/src/css/index.sass";
const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
});
app.mount("#app");
