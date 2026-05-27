"""
create a class for the yelp attributes
Name
Slogan
Location
Food quality
Price
Service
Environment
Cleanliness
Seating (outdoor/indoor/family/bar)


"""
class Restaurant:
    def __init__(self, name, app, capacity):
        self.name = name
        self.ratings = []
        self.menu = []
        self.price = [] #this is prob part of the menu
        self.app = app #link to app
        self.capacity = capacity
        self.contact = {}
    def __str__(self):
    #    return f"{self.name} has ratings of {self.ratings} and is located at {self.location}. It's menu consists of {self.menu} and is around ${self.price}. Its app is {self.app} and you can contact them here: {self.contact}."
        return f"{self.name} - App: {self.app} \
        Menu items: {len(self.menu)} \
        Price range: ${self.calculate_price_range()} \n\
        {self.convert_menu_to_str()}"
#when you call the string method on restaurant, it calls calculate price range (using ())

    """
    inputs: none
    process: loop through menu items, find min and max
    output: string: min-max
    """
    def calculate_price_range(self):
        min_price = 99999999
        max_price = 0
        for menu_item in self.menu:
            if menu_item.price < min_price:
                min_price = menu_item.price
            if menu_item.price > max_price:
                max_price = menu_item.price
        return f"{min_price}-{max_price}"

    def convert_menu_to_str(self):
        menu_str = ""
        for menu_item in self.menu:
            menu_str += f"{menu_item.name} | {menu_item.price}\n"
        return menu_str
"""
    def cheapest(self):
        cheapest_item = []
        for menu_item in self.menu:
            if menu_item.price < cheapest_item:
                cheapest_item = menu_item.price
        return f"Cheapest item: {cheapest_item}"
"""

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"{self.name} | ${self.price} | {self.category}"

restaurant_1 = Restaurant("Wing Stop", "wingstop.com/app", 4)
restaurant_2 = Restaurant("Blue Line Deli", "dining.byu.edu", 60)

menu_item_1 = MenuItem("Bacon Bleu Burger", 14, "Burger")
menu_item_2 = MenuItem("Cobb Salad", 13, "Salad")
menu_item_3 = MenuItem("Pepperoni Pizza", 12, "Pizza")

restaurant_1.menu.append(menu_item_1)
restaurant_1.menu.append(menu_item_2)
restaurant_2.menu.append(menu_item_3)

print(restaurant_1)
print(restaurant_2)