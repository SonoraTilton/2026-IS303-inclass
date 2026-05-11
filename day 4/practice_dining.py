# --- DATA (do not modify) -----------------------------------
restaurants = ["Cupbop", "Costa Vida", "Chick-fil-A", "Subway",
               "Taco Bell", "MOD Pizza", "Panda Express"]
ratings     = [4.5, 4.2, 4.8, 3.1, 3.6, 4.0, 3.9]
prices      = [11.50, 9.75, 8.99, 7.25, 6.99, 10.50, 8.75]
# ------------------------------------------------------------


# TODO 1 — Accumulator
# Calculate the average rating across all restaurants.
# Hint: sum all ratings, then divide by the count.

total_rating = 0
for rating in ratings:
    total_rating += rating
average_rating = total_rating / len(ratings)
print(f"Average rating: {average_rating:.2f}")  # replace ___ with your variable

top_restaurants = []
for i in range(len(ratings)):
    if ratings[i] >= 4:
        top_restaurants.append(restaurants[i])

print(f"Top-rated (4.0+): {top_restaurants}")  # replace ___ with your list

found = False
for restaurant in restaurants:
    if restaurant == "Cupbop":
        found = True

print(f"Cupbop found: {found}")  # replace ___ with your flag