"""
inputs:
- height
- weight
- age
- name
- sex

processes:
- input validation
- calculate bmi --> weight / height^2 * 703
- categorize bmi
    underweight < 18.5
    healthy 18.5 - 24.9
    overweight 25 - 29.9
    obestiy 30 - 39.9
    severe obesity 40+

outputs:
- report for an individual
"""

name = input("name: ")
age = input("age: ")
sex = input("sex: ")
height = input("height in inches: ")
weight = input("weight in pounds: ")

#input validation
age = age.replace(".", " ",1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = False
if age_is_int == True and age < 140 and age > 1:
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True

height = height.replace(".", "",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_reasonable = False
if height_is_int == True and height >= 12 and height <= 140:
    height_reasonable = True

weight = weight.replace(".", "",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_reasonable = False
if weight_is_int and weight > 12 and weight < 1200:
    weight_reasonable = True

ready_to_process = True


#error messages
if age_is_int == False:
    print("An unexpected age was entered, please enter full numbers")
    ready_to_process = False

if sex_is_valid == False:
    print("An unexpected sex was entered. Please use male or female")
    ready_to_process = False

if height_is_int == False or height_reasonable == False:
    print("An unexpected height was entered, please use whole numbers between 12-140")
    ready_to_process = False

if weight == False or weight_reasonable == False:
    print("An unexpected weight was entered, please use whole numbers between 12-1200")
    ready_to_process = False

#calculation
if ready_to_process == True:
    bmi = (weight / height**2)*703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi <= 24.9:
        bmi_category = "Healthy"
    elif bmi <= 29.9:
        bmi_category = "Overweight"
    elif bmi <= 39.9:
        bmi_category = "Obesity"
    else:
        bmi_category = "Severe obesity"

#output
    print(f"Report for {name}\n"
        f"your gender is {sex}\n"
        f"at {height} inches and {weight} pounds, your BMI is {bmi:.2f} and your BMI Category is {bmi_category}")
