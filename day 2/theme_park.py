"""
Inputs:
- age
- height
- day of the week
- waiver
- VIP pass
- parent presence

processes:
- use variables to verify which rides are available

outputs:
- list of rides
"""

age = int(input("How old are you? "))
height = int(input("How tall are you in inches? "))
day = input("Day of the week: ").lower()
waiver = input("Do you have a signed waiver? yes/no ").lower()
VIP = input("Do you have a VIP pass? yes/no ").lower()
parent = input("Parent present? yes/no ").lower()

#megadrop
if age >= 14 and waiver == "yes" and (height >= 54 or (height >=50 and VIP == "yes")):
    print("Megadrop")

#still megadrop but with nested if
if age >= 14 and waiver == "yes":
    if height >= 54:
        print("Megadrop")
    elif height >= 50 and VIP == "yes":
        print("Megadrop")

if age >= 10 and height >= 48 and day != "monday":
    print("Thunderbolt")

if age >= 8 or (parent == "yes"):
    print("Kiddie Coaster")

else:
    print("No ride found")