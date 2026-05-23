"""
A coffee shop wants to track their daily orders. Write a program that:

Ask the user how many orders to log (a number)
For each order, ask for:

Drink name (a string) — e.g., Latte, Espresso, Mocha
Price in dollars (a number)
Whether it was a mobile order: yes or no (a string)

Store each order as a dictionary in a list. Each dictionary should have keys: "drink", "price", and "mobile" (True or False)
After all orders are entered, calculate and display:

Total revenue (sum of all order prices). Use the accumulator pattern.
Most expensive order (the drink name and price of the most expensive single order). Use the min/max pattern. If no orders were entered, print "No orders logged."
Mobile orders (a list of drink names that were ordered via mobile). Use the filter pattern. If none were mobile, print "No mobile orders today."


Print a formatted summary:

"""
num_orders = int(input("How many orders would you like to log? "))
if num_orders > 0:
    orders = []
    for i in range(num_orders):
        drink = input("What was the drink? ").title()
        price = float(input("What was the price of the drink? $"))
        mobile = input("Was it a mobile order? yes/no ").lower().strip()
        orders.append({"drink": drink, "price": price, "mobile": mobile})

    #total rev
    total_revenue = 0
    for order in orders:
        total_revenue += order["price"]

    #max
    expensive = orders[0]
    for order in orders:
        if order["price"] > expensive["price"]:
            expensive = order

    #filter mobile
    mobile = []
    for order in orders:
        if order["mobile"] == "yes":
            mobile.append(order["drink"])

    print("--- Daily Order Summary ---")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Most expensive order: {expensive["drink"]} ${expensive["price"]:.2f}")
    if len(mobile) > 0:
        print(f"Mobile orders: {", ".join(mobile)}")
    else:
        print("No mobile orders logged.")

else:
    print("No orders logged.")