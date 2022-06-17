export interface WidgetOption {
  label: string;
  name: string;
}

export const widgetOptions = {
  weather: {
    label: "weather",
    name: "weather",
  },
  soilParameter: {
    label: "soil parameter",
    name: "soil-parameter",
  },
  notification: {
    label: "notifications",
    name: "notifications",
  },
  gardenMap: {
    label: "garden map",
    name: "garden-map",
  },
  cropsTable: {
    label: "crops table",
    name: "crops-table",
  },
  cropsMap: {
    label: "crops map",
    name: "crops-map",
  },
  crops3dTable: {
    label: "3D table",
    name: "3d-table",
  },
  crops3dMap: {
    label: "3D map",
    name: "3d-map",
  },
} as const;

//type of widgetOptions keys
type widgetOptionsKeys = keyof typeof widgetOptions;

//type of widgetOptions names
export type StoreOption = typeof widgetOptions[widgetOptionsKeys]["name"];
