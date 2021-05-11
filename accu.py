import requests
import json
import time
from apikey import apikey

APIKEY = apikey
country_code = "UY"

def city_normalize(city):
	city_name = city.strip().replace(" ","%20")
	return city_name

def separator(symbol):
	print("\n"+(symbol*20)+"\n")
	
def far_to_cel(far_grades):
	celsius = (int(far_grades) - 32) * 5/9
	return celsius

def get_location(country_code, city):
	search = requests.get("http://dataservice.accuweather.com/locations/v1/cities/"+country_code+"/search?apikey="+APIKEY+"&q="+city+"&details=true")

	data = search.json()

	location_key = data[0]["Key"]
	return(str(location_key))
	

def get_Forecast(location_key):

	forecast_url = requests.get(
		f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey="+APIKEY+"&language=es-es&details=true")

	data = forecast_url.json()
		
	for key1 in data["DailyForecasts"]:
		
		minTemp = far_to_cel(key1['Temperature']['Minimum']['Value'])
		maxTemp = far_to_cel(key1['Temperature']['Maximum']['Value'])
		date = key1['Date']
	
		print(f"Clima para el día {date}")
		print(f"Temperatura mínima: {round(minTemp)}C°")
		print(f"Temperatura máxima: {round(maxTemp)}C°")
		print(f"Pronóstico: {str(key1['Day']['ShortPhrase'])}")
		separator("---")
		  
		
city = city_normalize(str(input("\n"+"Ciudad uruguaya de la que quiera pronóstico: ")))
key = get_location(country_code, city)
get_Forecast(key)
