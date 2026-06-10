from bs4 import BeautifulSoup
import requests, time
from peewee import *

db = SqliteDatabase("vehicles.db")

class Vehicle(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()
    mpg = IntegerField()
    category = CharField()
    tco_10yr = IntegerField()
    class Meta:
        database = db

db.connect()
db.create_tables([Vehicle])

def get_fuel_data(year, make, model):
    """
    inputs: year int, make string, model string
    processes:
    - look up car id using fueleconomy.gov
    - use the vehicle id to get the comb08 mpg
    output: combined mpg
    """

    if year < 1900 and year > 2100:
        print ("Please enter a reasonable year.")
        return 0
    base_url = "https://www.fueleconomy.gov/ws/rest/"
    base_headers = {"Accept":"application/json"}
    url = base_url + f"vehicle/menu/options?year={year}&make={make}&model={model}"
    response = requests.get(url, headers=base_headers)
    data = response.json()
    if type(data["menuItem"]) == list:
        vehicle_id = data["menuItem"][0]["value"]
    else:
        vehicle_id = data["menuItem"]["value"]
#    print(vehicle_id)
#    mpg = data["vehicle"][22]["comb08"]

    #second call to grab mpg for vehicle ID
    url = base_url + f"vehicle/{vehicle_id}"
    response = requests.get(url, headers=base_headers)
    data = response.json()
#    print(data["comb08"])
    return data["comb08"]

def get_maitenance_costs(make, model):
    base_url = "https://caredge.com/"
    base_headers = {"User-Agent": "Mozilla/5.0"}
    url = base_url + f"{make.lower()}/{model.lower()}/maintenance"
    response = requests.get(url, headers=base_headers)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[0]
    total_maintenance = 0
    for row in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        dollar_amount = cells[2]
        dollar_amount = dollar_amount.replace("$", "")
        dollar_amount = dollar_amount.replace(",", "")
        int_amount = int(dollar_amount)
        total_maintenance += int_amount
    return total_maintenance

def store_vehicle(data):
    existing = Vehicle.get_or_none(
        (Vehicle.make == data["make"]) &
        (Vehicle.model == data["model"]) &
        (Vehicle.year == data["year"])
        )
    if existing:
        print(f"Skipping {data['make']} {data['model']}")
        return
    Vehicle.create(**data)
    print(f"Stored {data['make']}")

list_of_vehicles = [
    {"year": 2020, "make": "Honda", "model": "Civic", "extra_text": " 4Dr", "category": "Sedan"},
    {"year": 2026, "make": "BMW", "model": "Z4", "extra_text": " sDrive30i", "category": "Sports Car"},
    {"year": 2020, "make": "Chevrolet", "model": "Blazer", "extra_text": " AWD", "category": "SUV"},
    {"year": 2019, "make": "Cadillac", "model": "Escalade", "extra_text": " 2WD", "category": "SUV"},
    {"year": 2014, "make": "Nissan", "model": "Versa", "extra_text": "", "category": "Sedan"}
    ]

for vehicle in list_of_vehicles:
    mpg = get_fuel_data(vehicle["year"], vehicle["make"], vehicle["model"]+vehicle["extra_text"])
    ten_year_maintenance = get_maitenance_costs(vehicle["make"], vehicle["model"])
    tco = 11000*10/int(mpg)*4.5 + ten_year_maintenance
    if (int(mpg) < 5):
        print("No MPG data")
    print(f"{vehicle["year"]} {vehicle["make"]} {vehicle["model"]} TCO: {tco}")
    time.sleep(5)

    vehicle_data = {"make":vehicle["make"], "model":vehicle["model"],
                    "year":vehicle["year"], "mpg":mpg,
                    "category":vehicle["category"], "tco_10yr":tco}
    store_vehicle(vehicle_data)

 #   store_vehicle(vehicle_data)

#for v in Vehicle.select():
#    print(v.make, v.model, v.mpg)