from bs4 import BeautifulSoup
import requests, time

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
    vehicle_id = data["menuItem"][0]["value"]
    print(vehicle_id)
#    mpg = data["vehicle"][22]["comb08"]

    #second call to grab mpg for vehicle ID
    url = base_url + f"vehicle/{vehicle_id}"
    response = requests.get(url, headers=base_headers)
    data = response.json()
    print(data["comb08"])
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

list_of_vehicles = [
    {"year": 2020, "make": "Honda", "model": "Civic", "extra_text": " 4Dr"},
    {"year": 2026, "make": "BMW", "model": "Z4", "extra_text": " sDrive30i"},
    {"year": 2020, "make": "Chevrolet", "model": "Blazer", "extra_text": " AWD"}
]
for vehicle in list_of_vehicles:
    mpg = get_fuel_data(vehicle["year"], vehicle["make"], vehicle["model"]+vehicle["extra_text"])
    ten_year_maintenance = get_maitenance_costs(vehicle["make"], vehicle["model"])
    tco = 11000*10/int(mpg)*4.5 + ten_year_maintenance
    print(f"{vehicle["year"], vehicle["make"], vehicle["model"]} TCO: {tco}")
    time.sleep(5)


"""
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table")[0]
for row in table.find_all("tr")[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
# Result: Year 1: $207 → Year 10: $670
"""