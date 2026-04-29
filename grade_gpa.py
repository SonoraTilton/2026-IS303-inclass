"""
Sonora Tilton
IS 303

Inputs: 
- students name
- grade for 3 classes
- crerdits for 3 classes

Processes:
- calculate GPA using the ggrades and the credit total

- Outputs:
- Gpa
- report card for student

"""

#inputs
name = input("Student name: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credits: "))
credit2 = int(input("Course 2 credits: "))
credit3 = int(input("Course 3 credits: "))

#process
total_credits = credit1 + credit2 + credit3
gpa = (grade1*credit1 + grade2*credit2 + grade3*credit3) / total_credits

# outputs
print(f"{name}'s Report Card")
print(f"Total credits: total_credits")
print(f"Course 1: {grade1} credits: {credit1}\n"
      f"Course 1: {grade2} credits: {credit2}\n"
      f"Course 1: {grade3} credits: {credit3}")
print(f"Average GPA: {gpa}")