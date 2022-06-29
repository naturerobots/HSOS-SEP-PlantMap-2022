# Vite Env Variables and Modes

The `Vite` documentation for `Env Variables and Modes` is available _[here](https://vitejs.dev/guide/env-and-mode.html#env-variables-and-modes)_.

## Modes

### Development Mode

```bash
# run vite in development mode
cd vue
npm run dev
# or
make run-frontend
```

### Production Mode

```bash
# run vite in production mode
cd vue
npm run build
npm run preview
# or
make run-frontend-prod
```

## Environment

### Files

<!--python only added for syntax highlighting, would be text-->

```python
.env              # loaded in all cases
.env.development  # only loaded in development mode
.env.production   # only loaded in production mode
```

!!! danger
    **❗ Do not store sensitive information in `.env` files. ❗**
    Sensitive variables can be stored in `.env.*.local` files by adding it to your .gitignore to avoid them being
    checked into git.

▶ [Detailed information](https://vitejs.dev/guide/env-and-mode.html#env-files)

### Variables

| Variable           | Description                                                       | default     | dev            | prod            |
| ------------------ | ----------------------------------------------------------------- | ----------- | -------------- | --------------- |
| VITE_APP_TITLE     | Title of the app in specific mode                                 | PlantMap    | [DEV] PlantMap | [PROD] PlantMap |
| VITE_AUTH_REQUIRED | false/true, if auth is requried                                   | false       | false          | true            |
| VITE_TOKEN_MAPBOX  | [Mapbox](<[https://](https://www.mapbox.com/)>) token             | must be set | /              | /               |
| VITE_TOKEN_OWM     | [OpenWeatherMap](<[https://](https://openweathermap.org/)>) token | must be set | /              | /               |

!!! info
    An env file for a specific mode (e.g. .env.production) will take higher priority than the generic `.env`.
    Environment variables that already exist when Vite is executed have the highest priority and will not be
    overwritten by `.env` files.

<!--bash only added for syntax highlighting, would be text-->

```bash
# vue/.env
VITE_APP_TITLE=PlantMap
VITE_AUTH_REQUIRED=false
VITE_TOKEN_MAPBOX= ... #SET TOKEN
VITE_TOKEN_OWM= ... #SET TOKEN

# vue/.env.development
VITE_APP_TITLE=[DEV] PlantMap
VITE_AUTH_REQUIRED=false

# vue/.env.production
VITE_APP_TITLE=[PROD] PlantMap
VITE_AUTH_REQUIRED=true
```

## IntelliSense for TypeScript

```TypeScript
// vue/env.d.ts

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string;
  readonly VITE_AUTH_REQUIRED: string; //should be a boolean ❗
  readonly VITE_TOKEN_MAPBOX: string;
  readonly VITE_TOKEN_OWM: string;
}
```

<!--FIXME: MD046 can be ignored, but maybe add markdownlint config for that?-->

??? Bug
    The type of `VITE_AUTH_REQUIRED` should be a boolean, but if the type is set to boolean,
    `VITE_AUTH_REQUIRED` remains a string.

    ```diff
    - readonly VITE_AUTH_REQUIRED: string;
    + readonly VITE_AUTH_REQUIRED: boolean;
    ```
