/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string; //.env
  readonly VITE_AUTH_REQUIRED: string; //FIXME: should be a boolean, but it's always a string
  readonly VITE_TOKEN_MAPBOX: string;
  readonly VITE_TOKEN_OWM: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
