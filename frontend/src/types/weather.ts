export interface Weather {
  current: WeatherCurrent;
  forecast: WeatherForecast[];
}

export interface WeatherCurrent {
  dt: number;
  temp: number;
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
