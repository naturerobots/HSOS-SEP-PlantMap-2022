export interface GardenImage {
  image: string;
  coordinates: Coordinate[];
}

export interface Coordinate {
  name: string;
  latitude: number;
  longitude: number;
}
