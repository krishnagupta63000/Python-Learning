# Q1.
'''n = int(input("Enter a Number: "))
if(n%5==0):
    print("Hi")
else:
    print("Bye")'''

# Q2.
'''X = int(input("Enter First Side: "))
Y = int(input("Enter Second Side: "))
H = int(input("Enter Height: "))
area = (X+Y)/2+H
print("Area of Trapazoid:", area)

# Q3.
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

# Q4.
ch = ("Enter an Alphabet: ")
if (ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="i" or ch=="I" or ch=="o" or ch=="O" or ch=="u" or ch=="U"):
    print("Vowel")
else:
    print("Consonant")

# Q5

# Q6.
m = int(input("Enter The Number of Months: "))
y = m//12
m = m%12
print(y, "Years and",m,"Months")

# Q7.
colour = input("Blue or Red: ")
mode = input("Steady or Flashing: ")
if colour == "Blue"and mode == "Steady":
    print(mode, colour, ", clear view.")
elif colour == "Blue" and mode == "Flashing":
    print(mode, colour, ", clouds due.")
elif colour == "Red" and mode == "Steady":
    print(mode, colour, ", rain ahead.")
else:
    print(mode, colour, ", snow instead.")

# Q8.
cost = int(input("Enter Cost: "))
rev = int(input("Enter Revenue: "))
if (cost == rev):
    print("Break Even.")
elif (rev > cost):
    print("Profit of" ,rev - cost)
else:
    print("Loss of" ,cost - rev)

# Q9.
num = int(input("Enter how many widgets you want: "))
if (num<100):
    print("Cost:",25*num,"cents")
else:
    print("Cost:",20*num,"cents")

#Q10.
kg = int(input("How many KG of Apples: "))
amount = int(input("Enter how much cash you have: "))
if(amount<15*kg):
    print("You owe",-amount15*kg,"$ more")
else:
    print("You have",amount-2.50*pounds,"$ extra")

#Q11.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a>c):
    if(a>b):
        print("A is Greatest")
    else:
        print ("B is Greatest")
else:
    if(c>b):
        print("C is Greatest")
    else:
        print("B is Greatest")

#Q12.
BS = int(input("Enter The Basic Salary: "))
HRA = 0.2*BS
TA = 0.05*BS
DA = 0.1*BS
GS = BS+HRA+TA+DA
print("Gross Salary =",GS)
#Q13.
if (GS<300000):
    print(0*GS, "% Income Tax")
elif(GS>=30000 and GS<1000000):
    print(0.1*GS, "% Income Tax")
elif(GS>=1000000 and GS<2500000):
    print(0.2*GS, "% Income Tax")
else:
    print(0.3*GS, "% Income Tax")

#Q14.
income = int(input("Enter Taxable Income: "))
if(income<=20000):
    print("Set Tax =",0.02*income)
else:
    if(income<=50000):
        print("Set Tax =",400+0.025*(income-20000))
    else:
        print("Set Tax =",1150+0.0350*(income-50000))

'''