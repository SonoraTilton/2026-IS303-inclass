import requests

url = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year=2020&make=Honda&model=Civic%204Dr"
response = requests.get(url, headers={"Accept":"application/json"})
# Parse the JSON response
data = response.json()
vehicle_id = data["menuItem"][0]["value"]




mpg = data["menuItem"][0]["value"]

#get_fuel_data(year, make, model):