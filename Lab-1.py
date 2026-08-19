#Q1. Write a Python program to display 'Hello JKLU!' and 'I am learning Python.'
print("Hello JKLU!", "I am learing Python")

#Q2. Accept the student's name and branch as input and display a welcome message.
name = input("Enter Name: ")
branch = input("Enter Branch: ")
print(name, branch)

#Q3. Input the length and width (in metres) of a rectangular plot and calculate its area.
l = int(input("Enter Length: "))
b = int(input("Enter Breadth: "))
print(l*b,"meters")

#Q4. Modify Problem 3 to accept dimensions in feet and display the area in square metres.
l = int(input("Enter Length in Feet: "))
b = int(input("Enter Breadth in Feet: "))
print((l*b)/3.2,"meters")

#Q5. Input two positive integers x and y. Check whether y is divisible by x. For negative inputs, display 'Invalid Input'.
# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# if(y%x==0):
#     print("Divisible")
# else:
#     print("Not Divisible")

#Q6. Input an integer and determine whether it is even or odd.
# num = int(input("Enter a number: "))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")

#Q7. Input the radius of a circle (1–100 only) and calculate its area. Handle invalid inputs.
# r = int(input("Enter Radius(1-100): "))
# if(r>=1 and r<=100):
#     print("AREA=", 3.14*r**2)
# else:
#     print("Invalid Radius")

#Q8. Input temperature in Celsius and display the equivalent Fahrenheit and Kelvin values.
# c = int(input("Enter Temp:  "))
# print(((9*c)/5) + 32, "In Farebheit")
# print(c+273.15, "In Kelvin")

#Q9. Input the number of seconds (1–86400) and display the equivalent time in HH:MM: SS format.
# s = int(input("Enter Seconds: "))
# h = s//3600
# s = s%3600

# m = s//60
# s = s%60
# print(h,"Hours", m,"Mins", s, "Sec")

#Q10. Mini Challenge (Choose ONE):
#(a) Attendance Percentage Calculator (eligible if attendance ≥75%), 
at = int(input("Enter Attandace: "))
if(at>=75):
    print("Eligilbe")
else:
    print("Not Eligilbe")