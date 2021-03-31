from django.urls import path
from .views import CityWeatherView, City_Delete
app_name = 'WeatherApp'
urlpatterns = [
    path('', CityWeatherView, name= 'city_weather'),
    path('remove/<city_name>/', City_Delete, name= 'city_remove'),
]