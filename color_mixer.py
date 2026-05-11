"""
Color Mixer:
red+blue = purple
red+yellow = orange
blue+yellow = green

purple+red = pink
purple+blue = indigo
orange+red = red-orange
orange+yellow = mac&cheese
green+blue = teal
green+yellow = lime

else = brown

input: 2 colors

process: validate colors -- error messsage
mix colors

output: print new color in f-string

somewhere fit an and, or, or not

"""

valid_colors = ["red", "blue", "yellow", "purple", "orange", "green"]

color1 = input("Enter the first color: ").lower()
color2 = input("Enter the second color: ").lower()

if color1 not in valid_colors:
    print("Please input a valid color (red, blue, yellow, purple, orange, green).")
if color2 not in valid_colors:
    print("Please input a valid color (red, blue, yellow, purple, orange, green).")

if color1 == "red" and color2 == "blue":
    print(f"{color1} and {color2} make purple!")
elif color1 =="blue" and color2 == "red":
    print(f"{color1} and {color2} make purple!")
elif color1 =="blue" and color2 == "yellow":
    print(f"{color1} and {color2} make green!")
elif color1 =="yellow" and color2 == "blue":
    print(f"{color1} and {color2} make green!")
elif color1 =="red" and color2 == "yellow":
    print(f"{color1} and {color2} make orange!")
elif color1 =="yellow" and color2 == "red":
    print(f"{color1} and {color2} make orange!")
elif color1 =="blue" and color2 == "purple":
    print(f"{color1} and {color2} make indigo!")
elif color1 =="purple" and color2 == "blue":
    print(f"{color1} and {color2} make indigo!")
elif color1 =="purple" and color2 == "red":
    print(f"{color1} and {color2} make pink!")
elif color1 =="red" and color2 == "purple":
    print(f"{color1} and {color2} make pink!")
elif color1 =="yellow" and color2 == "orange":
    print(f"{color1} and {color2} make mac&cheese!")
elif color1 =="orange" and color2 == "yellow":
    print(f"{color1} and {color2} make mac&cheese!")
elif color1 =="red" and color2 == "orange":
    print(f"{color1} and {color2} make red-orange!")
elif color1 =="orange" and color2 == "red":
    print(f"{color1} and {color2} make red-orange!")
elif color1 =="blue" and color2 == "green":
    print(f"{color1} and {color2} make teal!")
elif color1 =="green" and color2 == "blue":
    print(f"{color1} and {color2} make teal!")
elif color1 =="yellow" and color2 == "green":
    print(f"{color1} and {color2} make lime!")
elif color1 =="green" and color2 == "yellow":
    print(f"{color1} and {color2} make lime!")
else:
    print(f"{color1} and {color2} make brown!")