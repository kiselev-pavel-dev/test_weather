from fastapi import FastAPI, Depends

from starlette.status import HTTP_200_OK

from src.services.services import GetWeatherService, weather_service

app = FastAPI()


@app.get(
    "/api/v1/current_weather/{city}",
    summary="Текущая погода",
    description="Получение текущей погоды по городу",
    status_code=HTTP_200_OK,
    tags=["Погода"],
)
def get_current_weather(
    city: str,
    service: GetWeatherService = Depends(weather_service)
):
    return service.get_current_weather(location=city)


@app.get(
    "/api/v1/forecast_weather/{city}",
    summary="Прогноз погоды",
    description="Получение прогноза погоды по городу",
    status_code=HTTP_200_OK,
    tags=["Погода"],)
def get_forecast_weather(
    city: str,
    interval: int,
    service: GetWeatherService = Depends(weather_service)
):
    return service.get_forecast_weather(location=city, days=interval)
