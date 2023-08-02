import requests
import datetime


def get_weather_forecast(city, days):
    api_key = "f9ada9efec6a3934dad5f30068fdcbb8"
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"

    response = requests.get(url)
    data = response.json()

    return data


def save_weather_forecast_to_file(city, days, data):
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    filename = f"{current_date}-{city}-{days}-days-weather-forecast.txt"

    with open(filename, "w") as file:
        file.write("Дата Температура вдень Температура вночі\n")
        for day in data['list']:
            date = datetime.datetime.fromtimestamp(day['dt']).strftime("%d-%m-%Y")
            day_temp = day['temp']['day']
            night_temp = day['temp']['night']

            file.write(f"{date} {day_temp:.2f} {night_temp:.2f}\n")

    print(f"Прогноз погоди для {city} на наступні {days} днів збережено у файл {filename}")


city = input("Введіть назву міста: ")
days = int(input("Введіть кількість днів: "))

weather_data = get_weather_forecast(city, days)
save_weather_forecast_to_file(city, days, weather_data)