'''Q1. Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a
second point (x2, y2), and displays whether the second point lies inside, on the boundary of, or
outside the circle. The formula for computing the distance between two points is
distance = √[(x2 – x1)2 + (y2 – y1)2]'''

# print("Center of the Circle")
# x1 = int(input("Enter the x co-ordinate: "))
# y1 = int(input("Enter the y co-ordinate: "))
# r = int(input("Enter radius: "))
# print("Co-ordinates of a Point")
# x2 = int(input("Enter the x co-ordinate: "))
# y2 = int(input("Enter the y co-ordinate: "))
# d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
# if (d < r):
#     print(f"{d".2f}, Inside the circle.")
# elif (d > r):
#     print(f"{d:.2f}, Outside the circle.")
# else:
#     print(f"{d:.2f}, On the boundary.")

'''Q2. Write a program that prompts the user to enter the side of a regular pentagon and displays its area.
The formula for computing the area of a pentagon is Area = (5 * s2) / (4 * tan(π / 5)), where s is the
length of a side.'''

# import math
# s = int(input("Enter the side of a regular pentagon: "))
# area = (5*s**2)/ (4*math.tan(math.pi/5))
# print(f"Area of Pentagon: {area:.2f} sq cm")

'''Q3. Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can,
further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases
also.'''

# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))

# if(a<=0 or b<=0 or c<=0 or a+b+c!=180):
#     print("Invalid Triangle")
# elif(a==90 or b==90 or c==90):
#     print("Right Angled Triangle")
# elif(a>90 or b>90 or c>90):
#     print("Obtuse Angle Triangle")
# else: 
#     print("Acute Angle Triangle")

'''Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two
digits separately. Also, check if the two sums are equal or not.
'''

# n = int(input("Enter 4-digit number(1000-9999): "))
# a = n//1000
# b = (n//100) % 10
# c = (n//10) % 10
# d = n%10
# sum1 = a + b
# sum2 = c + d
# print("Sum of first two digits", sum1)
# print("Sum of last two dogits", sum2)

# if(sum1==sum2):
#     print("Both sums are equal")
# else:
#     print("Both sums are not equal")

'''Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built
functions and do not use loops. Also print the position of that digit counted from the left. If the
largest digit occurs more than once, print the position of its first occurrence.'''

# n = int(input("Enter a five digit numner(10000-99999): "))
# a = n//10000
# b = (n//1000) % 10
# c = (n//100) % 10
# d = (n//10) % 10
# e = n%10
# if (a>=b and a>=c and a>=d and a>=e):
#     print(a, "is largest at postion 1")
# elif(b>=c and b>=d and b>=e):
#     print(b, "is largest at position 2")
# elif(c>=d and c>=e):
#     print(c, "is largest at postion 3")
# elif(d>=e):
#     print(d, "is largest at position 4")
# else:
#     print(e, "is largest at position 5")

'''Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of
b moves to c, and the value of c moves to a, without using a fourth variable or multiple
assignment operation.'''

# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# c = int(input("Enter C: "))

# temp = a
# a = b
# b = c
# c = temp
# print(f"A:",a)
# print("B:",b)
# print("C:",c)

'''Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is
exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad
number.'''

# n = int(input("Enter a 3-digit number(100-999): "))
# a = n//100
# b = (n//10) % 10
# c = n%10

# sum = a + b + c
# if (n%sum==0):
#     print("Yes its a Harshad Number: ", n)
# else:
#     print("No its not a Harshad Number: ", n)

'''Suppose a water tank initially holds V litres of water. Every day 5% of the water present in the tank
evaporates, and then exactly 10 litres of fresh water is added to it. Therefore, the daily retention
rate is 1 – 0.05 = 0.95. After the first day, the quantity in the tank becomes
V * 0.95 + 10
After the second day, the quantity in the tank becomes
(V * 0.95 + 10) * 0.95 + 10
After the third day, the quantity in the tank becomes
((V * 0.95 + 10) * 0.95 + 10) * 0.95 + 10
and so on.
Write a program that prompts the user to enter the initial quantity of water and the number of
days (N) and displays the quantity of water in the tank after the Nth day. Check for valid and
invalid cases. Do not use loops.'''

v = float(input("Enter Initial Amount of Water: "))
n = int(input("Enter Number of Days: "))
if (n>=0 and v>0):
    final_v = v*(0.95)**n + 200*(1-0.95**n)
    print("On day no.",n,"There is",round(final_v, 2),"L amount of Water")
else:
    print("Invalid case")


'''Enter the coefficients of two straight lines a1x + b1y = c1 and a2x + b2y = c2 and display their point
of intersection. Handle all the cases for invalid input as well as the cases where the two lines are
parallel or coincident, and display the solution till exactly 2 decimal places.'''

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

if (a1==0 and b1 == 0):
    print("Invalid Input")
elif (a2==0 and b2==0):
    print("Invalid Input")
else:
    d = a1*b2 - a2*b1

    if(d!=0):
        x = (c1*b2 - c2*b1)/d
        y = (a1*c2 - a2*c1) / d
        print("(",round(x,2),",",round(y,2),") is the Intersetion Point")

    elif (a1*c2 == a2*c1 and b1*c2 == b2*c1):
        print("Co-incident Lines")

    else:
        print("Parallel Lines")