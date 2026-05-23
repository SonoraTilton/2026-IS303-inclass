"""
A personal trainer needs a weekly workout summary. Write a program that:
1. Ask the user how many workouts to log (a number)
2. For each workout, ask for:
• Activity name (a string) — e.g., Running, Swimming, Yoga
• Duration in minutes (a number)
• Whether it was outdoors: yes or no (a string)
3. Store each workout as a dictionary in a list. Each dictionary should have keys: "activity",
"minutes", and "outdoor" (True or False)
4. After all workouts are entered, calculate and display:
Total minutes (sum of all workout durations). Use the accumulator pattern.
Longest workout (the activity name and duration of the longest single workout). Use
the min/max pattern. If no workouts were entered, print "No workouts logged."
Outdoor workouts (a list of activity names that were done outdoors). Use the filter
pattern. If none were outdoors, print "No outdoor workouts this week."
5. Print a formatted summary:
--- Weekly Workout Summary ---
Total minutes: 245
Longest workout: Swimming (60 min)
Outdoor workouts: Running, Cycling
Constraints
• You must use a for loop to process the list
• You must store data in a list of dictionaries
• You must use at least two named loop patterns (accumulator, min/max, or filter)
"""

number_workouts = int(input("How many workouts would you like to log? "))
if number_workouts == 0:
    print("No workouts logged.")
else:
    workouts = []

    for i in range(number_workouts):
        activity = input("What activity did you do? ").lower()
        minutes = int(input("How long was your workout in minutes? "))
        outdoor = input("Was your activity outdoors? ").lower()
        workouts.append({"activity": activity, "minutes": minutes, "outdoor": outdoor == "yes"})

    #sum
    total_minutes = 0
    for workout in workouts:
        total_minutes += workout["minutes"]
    print(f"Total workout time: {total_minutes} mins")

    #max
    most_minutes = workouts[0]
    for workout in workouts:
        if workout["minutes"] > most_minutes["minutes"]:
            most_minutes = workout
    print(f"Longest workout: {most_minutes["activity"]} ({most_minutes["minutes"]} mins)")

    outdoor_workouts = []
    for workout in workouts:
        if workout["outdoor"]:
            outdoor_workouts.append(workout["activity"])
    if outdoor_workouts > 0:
        print(f"Outdoor workouts: {", ".join(outdoor_workouts)}")
    else:
        print("No outdoor activities.")
