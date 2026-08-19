'''Write a program that interprets the Body Mass Index (BMI) based on a user’s weight and
height.
It should tell them the interpretation of their BMI based on the BMI value.
• Under 18.5 they are underweight
• Over 18.5 but below 25 they have a normal weight
• Over 25 but below 30 they are slightly overweight
• Over 30 but below 35 they are obese
• Above 35 they are clinically obese.
The BMI is calculated by dividing a person weight (in kg) by the square of their height
(in m). Take height and weight from the user.'''

h = float(input("Enter Your Height in Meters: "))
w = float(input("Enter Your Weight in KG: "))
BMI = w/h**2
if(BMI<18.5):
    print(BMI, "Under Weight")
elif(BMI>=18.5):
    print(BMI, "Normal Weight")
elif(BMI>=25):
    print(BMI, "Slightly Overweight")
elif(BMI>=30):
    print(BMI, "Obese")
else:
    print("Clinically Obese")