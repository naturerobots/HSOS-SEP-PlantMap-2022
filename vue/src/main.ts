import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import "./assets/base.css";
import { Quasar, Notify } from "quasar";
// Import icon libraries
import "@quasar/extras/material-icons/material-icons.css";
import MaterialIconSet from "quasar/icon-set/material-icons";
// // Import Quasar css
import "quasar/src/css/index.sass";

const app = createApp(App);

app.use(createPinia());
app.use(router);

// import Quasar plugins and add here
app.use(Quasar, {
  plugins: {
    Notify,
  },
  config: {
    notify: {
      /* look at QuasarConfOptions from the API card */
    },
  },
});

app.mount("#app");
MaterialIconSet.table.arrowUp = "expand_more";
