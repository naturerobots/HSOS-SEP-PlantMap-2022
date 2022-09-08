# External APIs

## OpenWeatherMap

The following [APIs](https://openweathermap.org/api) from [OpenWeatherMap](https://openweathermap.org/) were used for the `weather widget`. 
To use the APIs, an [OpenWeatherMap account](https://home.openweathermap.org/users/sign_up) and a [token](https://home.openweathermap.org/api_keys) must be created. 
The token must then be added as environment variable `VITE_TOKEN_OWM`.

| API                                                                                           | Description                                                                                                                                                       | [Pricing](https://openweathermap.org/price)          |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [Current weather data](https://openweathermap.org/current)                     | Used to get the current temperature, weather and city name based on the coordinates of the garden. <br>**The geocoder used in the API will soon be deprecated.**  | 60 free calls/minute <br> 1,000,000 free calls/month |
| [One Call API 3.0](https://openweathermap.org/api/one-call-3)                                 | Used to get the current day's temperature low and high, as well as the hourly forecast for temperature, rain probability, and wind speed and direction.           | 1,000 free calls/day                                 |
| [Geocoding API](https://openweathermap.org/api/geocoding-api) | **Not used yet**, but the service has already been implemented for it, so it can be used when the `Current weater data API` geocoder API is deprecated.             | 60 free calls/minute <br> 1,000,000 free calls/month |

## Mapbox

The following [APIs](https://www.mapbox.com/product-apis) from [Mapbox](https://www.mapbox.com/) were used for the `garden map`.
To use the APIs, an [Mapbox account](https://account.mapbox.com/auth/signup/) and a `token` must be created.
The token must then be added as environment variable `VITE_TOKEN_MAPBOX`.

| API                                                            | Description                                                                                                    | [Pricing](https://www.mapbox.com/pricing)          |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------|
| [Static Tiles](https://docs.mapbox.com/api/maps/static-tiles/) | Used to add tiles to the map for the garden, so that the garden image can be better placed in the environment. | 200,000 free tile requests/month |
