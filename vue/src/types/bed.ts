import type { Health } from "./health";

export interface Bed {
  id: number;
  plant: string;
  variety: string;
  plants: string;
  soil_humidity: number;
  harvest: string;
  yield: string;
  health: Health[];
  //plant_coords
}
