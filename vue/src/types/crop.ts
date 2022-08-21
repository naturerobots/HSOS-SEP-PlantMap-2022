import type { Coords } from "./coords";
import type { Health } from "./health";

export interface Crop {
  id: string;
  bed_id: number;
  plant: string;
  variety: string;
  soil_humidity: string;
  harvest: string;
  yield: string;
  health: Health[];
  plant_coords: Coords;
}
