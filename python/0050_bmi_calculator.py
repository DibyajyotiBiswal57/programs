#Q50
print("This program calculates the BMI(Body Mass Index) of a person.")
weight=float(input("Enter your weight(in kgs):"))
height=float(input("Enter your height(in m):"))

height=height**2

bmi=weight/height

print(f"Your BMI is {bmi}.")
