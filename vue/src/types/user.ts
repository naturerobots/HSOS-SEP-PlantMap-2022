import type { StoreOption } from "@/types/WidgetOption";

export interface User {
  settings: Settings;
}

export interface Settings {
  widgetOptions: StoreOption[];
}
