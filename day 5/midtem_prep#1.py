"""
1. Ask the user for:
• Number of guests (a whole number)
• Cost per person for food (a number)
• Cost per person for drinks (a number)
• Whether they need to rent a venue: yes or no (a string)
2. Calculate:
• Food total (guests x food cost per person)
• Drink total (guests x drink cost per person)
• Venue cost: $0 if they do not need a venue, $250.00 if they do
• Grand total (food + drinks + venue)
3. Print a formatted summary using f-strings with costs formatted to 2 decimal places:
--- Party Cost Summary ---
Guests: 20
Food total: $300.00
Drink total: $100.00
Venue cost: $250.00
Grand total: $650.00
4. If the grand total exceeds $500, print: "Tip: Ask guests to bring a dish to reduce costs!"

"""

number_guests = int(input("How many guests will there be? "))
food_cost = float(input("How much will food cost per person in dollars? "))
drink_cost = float(input("How much will drinks cost per person in dollars? "))
venue = input("Do you need a venue? yes/no ").lower().strip()

food_total = food_cost * number_guests
drink_total = drink_cost * number_guests
if venue == "yes":
    venue_cost = 250
else:
    venue_cost = 0
total_cost = food_total + drink_total + venue_cost

print(f"Guests: {number_guests}\nFood total: ${food_total:.2f}\nDrink total: ${drink_total:.2f}\nVenue cost: ${venue_cost:.2f}\nGrand total: ${total_cost:.2f}")
if total_cost > 500:
    print(f"Tip: Ask guests to bring a dish to reduce costs!")