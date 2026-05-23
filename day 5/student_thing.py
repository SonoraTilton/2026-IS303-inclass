"""
A student organization is collecting sign-ups for campus events. Write a program that:

Ask for the name of the event coordinator (a string)
Use a while loop to let the user add sign-ups one at a time. After each sign-up, ask "Add another sign-up? (yes/no)". Stop when the user types "no".
For each sign-up, collect:

Attendee name (a string)
Event name (a string)
Department: "engineering", "business", "arts", or "science" (a string)

Clean each entry's data before storing:

Attendee name should be converted to title case
Event name should be converted to title case
Department should be converted to lowercase and stripped of whitespace

Store each sign-up as a dictionary in a list with keys: "attendee", "event", "department"
After sign-ups close, produce a report:

Total number of sign-ups - len(sign_ups)
Number of business sign-ups and number of non-business sign-ups (use an accumulator or counter)
A numbered list of all sign-ups showing attendee name, event, and department
If more than half the sign-ups are from business, print: "Business is taking over!"
"""
coordinator = input("Who is the event coordinator? ").title()
sign_ups = []
add_sign_up = "yes"
while add_sign_up == "yes":
    name = input("What is the attendee's name? ").title()
    event = input("What is the name of the event? ").title()
    department = input("What is the name of your department? engineering/business/arts/science ").lower().strip()
    sign_ups.append({"name": name, "event": event, "department": department})
    add_sign_up = input("Would you like to add another sign-up? yes/no ").lower().strip()

print(f"Total sign-ups: {len(sign_ups)}")

#accumulator
business_attendees = 0
for sign_up in sign_ups:
    if sign_up["department"] == "business":
        business_attendees += 1
non_business_attendees = len(sign_ups) - business_attendees
print(f"Business sign-ups: {business_attendees}")
print(f"Non-business sign-ups: {non_business_attendees}")
for i, sign_up in enumerate(sign_ups, start=1):
    print(f"{i}. {sign_up["name"]} from {sign_up["department"]} signed up for {sign_up["event"]}.")

if business_attendees > len(sign_ups) / 2:
    print("Business is taking over!")