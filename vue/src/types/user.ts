import type { StoreOption } from "@/types/WidgetOption";

export interface User {
  username: string;
  first_name: string;
  last_name: string;
}
export interface Settings {
  widgetOptions: StoreOption[];
}

export interface Token {
  expiry: string;
  token: string;
}
