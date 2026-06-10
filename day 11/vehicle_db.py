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

v1_data = {"make": "Toyta", "model":"Corolla",
    "year":2020, "mpg":34,
    "category":"Sedan", "tco_10yr":51200}
store_vehicle(v1_data)

v2_data = {"make": "Honda", "model":"Civic",
    "year":2020, "mpg":33,
    "category":"Sedan", "tco_10yr":20634}
store_vehicle(v2_data)

v3_data = {"make": "BMW", "model":"Z4",
    "year":2026, "mpg":28,
    "category":"Sports Car", "tco_10yr":32593.6}
store_vehicle(v3_data)

v4_data = {"make": "Chevrolet", "model":"Blazer",
    "year":2020, "mpg":21,
    "category":"Sedan", "tco_10yr":32961.4}
store_vehicle(v4_data)

v5_data = {"make": "Cadillac", "model":"Escalade",
    "year":2019, "mpg":17,
    "category":"SUV", "tco_10yr":43559.7}
store_vehicle(v5_data)

incorrect_row = Vehicle.get(Vehicle.make == "Toyta")
incorrect_row.make = "Toyota"
incorrect_row.save()
        

for v in Vehicle.select():
    print(v.make, v.model, v.mpg)