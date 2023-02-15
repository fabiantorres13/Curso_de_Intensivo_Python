import requests
import ClaveApi

ciudad = input("Ingresa la Ciudad: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={ClaveApi.Apikey}&units=metric"

res = requests.get(url)

datos = res.json()


temp = datos["main"]["temp"]
tempMax = datos["main"]["temp_max"]
tempMin = datos["main"]["temp_min"]

print("")
print("Resultados de la búsqueda: ")
print("")
print(f'Temperatura: {temp}')
print(f'Temperatura Máxima: {tempMax}')
print(f'Temperatura Mínima: {tempMin}')