from fastapi import APIRouter, Depends
from app.models.weather import WeatherData
from app.services.weather_services import WeatherService

router = APIRouter()
weather_service = WeatherService()


@router.get("/current-weather/{location}", response_model=WeatherData)
def get_current_weather(location: str):
    weather_data = weather_service.get_weather(location)
    return weather_data
