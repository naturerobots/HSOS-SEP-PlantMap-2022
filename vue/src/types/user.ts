import type { StoreOption } from "@/types/WidgetOption";

export interface User {
  settings: Settings;
  token: Token;
}

export interface Settings {
  widgetOptions: StoreOption[];
}

export interface Token {
  expiry: string;
  token: string;
}
