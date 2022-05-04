export interface Weather {
  current: WeatherCurrent;
  forecast: WeatherForecast[];
}

//Current and Forecast could be combined into one interface
export interface WeatherCurrent {
  name: string;
  dt: number;
  tempMin: number;
  tempMax: number;
  description: string;
  icon: string;
}

export interface WeatherForecast {
  dt: number;
  tempMin: number;
  tempMax: number;
  description: string;
  icon: string;
}
