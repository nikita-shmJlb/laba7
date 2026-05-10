import requests
import json


def get_weather(city_name, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            temperature_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']

            print(f"Погода в городе: {city_name.title()}")
            print(f"Погода: {weather.capitalize()}")
            print(f"Температура: {temperature:.1f}°C")
            print(f"Ощущается как: {temperature_like:.1f}°C")
            print(f"Влажность: {humidity}%")
            print(f"Давление: {pressure} гПа")

        elif response.status_code == 401:
            print("Ошибка: Неверный API ключ")

        elif response.status_code == 404:
            print(f"Ошибка: Город '{city_name}' не найден")

        else:
            print(f"Ошибка: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
    except json.JSONDecodeError:
        print("Ошибка: Не удалось обработать ответ от сервера")
