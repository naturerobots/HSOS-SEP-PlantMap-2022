export interface Weather {
  current: WeatherCurrent;
  forecast: WeatherForecast[];
}

export interface WeatherCurrent {
  name: string;
  dt: Date;
  tempMin: number;
  tempMax: number;
  description: string;
  icon: string;
}

export interface WeatherForecast {
  dt: Date;
  tempMin: number;
  tempMax: number;
  description: string;
  icon: string;
}
