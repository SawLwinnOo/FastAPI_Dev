from app.models.weather import WeatherData


class WeatherService:
    def get_weather(self, location: str) -> WeatherData:
        # In a real implementation, this would make an API call to a weather data provider
        # Here, we mock the data for demonstration purposes
        return WeatherData(location=location, temperature=25.0, humidity=65.0, wind_speed=10.0)
