import requests

from src.settings import settings

API_KEY = settings.API_KEY


class GetWeatherService:
    url_current: str = "https://api.m3o.com/v1/weather/Now"
    url_forecast: str = "https://api.m3o.com/v1/weather/Forecast"
    headers: dict = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    def get_current_weather(self, location: str) -> dict:
        data = {"location": location}
        response = requests.post(
            self.url_current,
            headers=self.headers,
            json=data
        )
        return response.json()

    def get_forecast_weather(self, location: str, days: int) -> dict:
        if days < 1 or days > 10:
            return {"detail": "Введите корректное число дней, от 1 до 10"}
        data = {
            "location": location,
            "days": days
        }
        response = requests.post(
            self.url_forecast,
            headers=self.headers,
            json=data
        )
        return response.json()


def weather_service() -> GetWeatherService:
    return GetWeatherService()
