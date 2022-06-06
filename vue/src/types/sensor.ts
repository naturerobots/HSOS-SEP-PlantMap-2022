export interface Sensor {
  id: number;
  name: string;
  moisture_value: number;
  moisture_trend: string;
  temp_value: number;
  temp_trend: string;
  ec_value: number;
  ec_trend: string;
  lat: number;
  lng: number;
}
