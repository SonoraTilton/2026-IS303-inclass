"""
A campus lost & found desk needs to log items that have been turned in. Write a program that:

Ask for the name of the staff member on duty (a string)
Use a while loop to let the user log items one at a time. After each item, ask "Log another item? (yes/no)". Stop when the user types "no".
For each item, collect:

Item name (a string)
Location found (a string) — e.g., Library, Gym, Cafeteria
Category: "electronics", "clothing", "jewelry", or "other" (a string)


Clean each entry's data before storing:

Item name should be converted to title case
Location should be converted to title case
Category should be converted to lowercase and stripped of whitespace


Store each item as a dictionary in a list with keys: "item", "location", "category"
After logging closes, produce a report:

Total number of items logged
Number of electronics and number of non-electronics (use an accumulator or counter)
A numbered list of all items showing item name, location, and category
If more than half the items are electronics, print: "Busy day for electronics!"

"""

staff = input("Who is the staff member on duty? ").title()
lost_things = []
add_item = "yes"
while add_item == "yes":
    item = input("What is the item? ").title()
    location = input("Where was it found? ").title()
    category = input("Is it an electronic, clothing, jewelry, or other? ").lower().strip()
    lost_things.append({"item": item, "location": location, "category": category})
    add_item = input("Would you like to add another item? yes/no ").lower().strip()

total_items = 0
for thing in lost_things:
    total_items += 1

electronics = 0
for thing in lost_things:
    if thing["category"] == "electronic":
        electronics += 1
non_electronics = total_items - electronics


print(f"Electronics: {electronics}")
print(f"Non-electronics: {non_electronics}")
for thing in enumerate(lost_things, start=1):
    print(thing)
if total_items/2 < electronics:
    print("Busy day for electronics!")