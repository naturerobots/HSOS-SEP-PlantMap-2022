import axios from "axios";
import type { Weather, WeatherCurrent, WeatherForecast } from "@/types/weather";

//TODO: Find a solution that the token is not directly implemented
const token = "a8b46be95a90a7e303aa7edd4fc1463e";
const baseURL = "https://api.openweathermap.org/data/2.5/onecall";
const exclude = "minutely,hourly";

export async function getWeatherInformation(lon: number, lat: number) {
  //test lon + lat -> Osnabrueck
  lon = 52.2799112;
  lat = 8.0471788;

  //https://api.openweathermap.org/data/2.5/onecall?lat=52.2799112&lon=8.0471788&exclude=minutely,hourly&lang=de&appid=a8b46be95a90a7e303aa7edd4fc1463e
  const response = await axios.get(baseURL, {
    params: { lat: lat, lon: lon, exclude: exclude, lang: "de", appid: token },
  });

  //const response = await axios.get("https://api.openweathermap.org/data/2.5/weather?lat=52.2799112&lon=8.0471788&lang=de&appid=a8b46be95a90a7e303aa7edd4fc1463e");

  console.log(createWeatherObject(response.data));

  return createWeatherObject(response.data);
}

//TODO: Calls need to be splitted into two seperated calls for "current information" and forecast "information"

function createWeatherObject(data: any): Weather {
  console.log(data);

  const wetter: Weather = {
    current: {} as WeatherCurrent,
    forecast: [] as WeatherForecast[],
  };

  //WeatherCurrent
  wetter.current.dt = data["current"]["dt"];
  wetter.current.temp = data["current"]["temp"];
  wetter.current.description = data["current"]["weather"][0]["description"];
  wetter.current.icon = data["current"]["weather"][0]["icon"];

  // WeatherForecast[]
  for (const result of data["daily"]) {
    const currentForecast: WeatherForecast = {} as WeatherForecast;
    currentForecast.dt = result["dt"];
    currentForecast.tempMin = result["temp"]["min"];
    currentForecast.tempMax = result["temp"]["max"];
    currentForecast.description = result["weather"][0]["description"];
    currentForecast.icon = result["weather"][0]["icon"];
    wetter.forecast.push(currentForecast);
  }

  return wetter;
}
