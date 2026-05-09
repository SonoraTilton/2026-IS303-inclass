age = input("Age: ")
if int(age) < 0:
    print("Invalid age")
elif int(age) < 18:
    print("Minor")
else:
    print("Adult")

name = "Alice"
result = name.lower()
print(name)
print(result)

name = input("What's your name? ")
class1 = input("What is your first class?")
grade1 = int(input("What is your grade in this class?"))
class2 = input("What is your second class?")
grade2 = int(input("What is your grade in this class?"))

print(f"Hello {name}, your grade is {grade1} in {class1}, and your grade in {class2} is {grade2}")