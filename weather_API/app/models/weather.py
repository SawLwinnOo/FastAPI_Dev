from pydantic import BaseModel


class WeatherData(BaseModel):
    location: str
    temperature: float
    humidity: float
    wind_speed: float
