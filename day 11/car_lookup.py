import requests
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


get_fuel_data(2020, "Honda", "Civic 4Dr")

get_fuel_data(2020, "Chevrolet", "Blazer AWD")