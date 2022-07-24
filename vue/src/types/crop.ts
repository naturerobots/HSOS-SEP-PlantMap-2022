import type { Health } from "./health";

export interface Crop {
  id: number;
  plant: string;
  variety: string;
  location: number;
  soilHumidity: string;
  health: Health[];
  status: string;
  harvest: string;
  yield: string;
}
