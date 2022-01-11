#Asking user to insert data
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Calculation of BMI

bmi = weight / (height * height)
final_bmi = round(bmi,2)

#Result Printing

if final_bmi <= 18:
    print(f"Your BMI is {final_bmi}, you are underweight.")
elif final_bmi <= 25:
    print(f"Your BMI is {final_bmi}, you have a normal weight.")
elif final_bmi <=30:
    print(f"Your BMI is {final_bmi}, you are slightly overweight.")
elif final_bmi <=35:
    print(f"Your BMI is {final_bmi}, you are obese.")    
else:
    print(f"Your BMI is {final_bmi}, you are clinically obese.")