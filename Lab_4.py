'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
Ask user for their salary and years of service and print the net bonus amount.'''

'''sal = int(input("Enter Salary : "))
years = int(input("Enter Years of work : "))
if (years>=5):
    print("Yeah!, You got an additional bonus of 5%.")
    print("Your Salary : ", 0.05*sal + sal)
else: 
    print("Your Salary : ", sal)'''

'''Write a program that reads input data from the console - a password (one line of random text)
and checks if the input matches the phrase "s3cr3t!P@ssw0rd". If it matches, print "Welcome",
otherwise print "Wrong password!".'''

'''p = input("Enter Password : ")
x = "s3cr3t!P@ssw0rd"
if (p==x):
    print("Welcome!")
else: 
    print("Incorrect Password.")'''

'''Write a program that reads input data from the console - the measures of a geometric
shape and calculates its area. There are four types of
shapes: square, rectangle, circle and triangle.
The first line of input is the type of shape (square, rectangle, circle, triangle):
If the shape is a square, the next argument will be one number - the length of its side.
If the shape is a rectangle, the next argument will be two numbers - the lengths of its sides.
If the shape is a circle, the next argument will be one number - the radius of the circle.
If the shape is a triangle, the next argument will be two numbers - its base and the
corresponding altitude.'''

'''sh = input("Enter Shape : ")
if (sh == "square"):
    s = int(input("Enter Side of a Square : "))
    print("Area of Square is", s**2,"sq cm")
elif(sh == "rectangle"):
    l = int(input("Enter Length of Rectangle : "))
    b = int(input("Enter Breadth of Rectangle : "))
    print("Area of Rectagle is", l*b, "sq cm")
elif(sh == "circle"):
    pi = 3.14
    r = int(input("Enter Radius : "))
    print("Area of Circle is", pi*r**2,"sq cm")
else:
    l = int(input("Enter Length of Triangle : "))
    b = int(input("Enter Breadth of Triangle : "))
    print("Area of Triangle is",0.5*l*b,"sq cm")'''

'''Write a program that reads two integers - hours and minutes based on a 24-hour day format and
calculates what time it will be 15 minutes later. The result should be printed in the following
format hh:mm. Hours should always be between 0 and 23, while minutes should always be
between 0 and 59. Hours should be written with one or two digits as needed, while the minutes
should always be written with two digits - add a leading zero, as needed. Example, Given the time
1:46 as input, the output displayed should be 2:01.'''

'''hours = int(input("Enter Hours : "))
mins = int(input("Enter Minutes : "))
total = hours * 60 + mins + 15
h = total//60
m = total%60
print("After adding 15 mins : ",h,"Hours", m, "Minutes")
'''
'''A student has to travel n kilometers. He can choose between three types of transportation:
Taxi. Starting fee: 33.58 INR. Day rate: 37.89 INR/km. Night rate: 43.17 INR/km.
Bus. Day / Night rate: 4.32 INR/km. Can be used for distances of a minimum of 20 km.
Train. Day / Night rate: 2.88 INR/km. Can be used for distances of a minimum of 100 km.
Write a program that reads the number of kilometers n and period of the day (day or night) and
calculates the price for the cheapest transport.'''

'''n = float(input("Enter kilometers: "))
time = input("Enter day or night: ")

if (time == "day"):
    taxi = 33.58 + n * 37.89
else:
    taxi = 33.58 + n * 43.17

bus = n * 4.32
train = n * 2.88

if (n < 20):
    cheapest = taxi
elif (n < 100):
    if (taxi < bus):
        cheapest = taxi
    else:
        cheapest = bus
else:
    if (taxi < bus and taxi < train):
        cheapest = taxi
    elif (bus < train):
        cheapest = bus
    else:
        cheapest = train

print("Cheapest price:", cheapest)'''

'''Tom Cat likes to sleep all day but, unfortunately, his owner is always playing with him whenever
he has free time. To sleep well, the norm of games that Tom has is 30,000 minutes per year. The
time for games he has depends on the holidays that his owner has:
• During workdays, his owner plays with him 63 minutes per day.
• During holidays, his owner plays with him 127 minutes per day.
Write a program that reads the number of holidays and prints whether Tom can sleep well and
how much the difference from the norm for the current year is. It is assumed that there are 365
days in one year.'''

n = int(input("Enter Number of Holidays : "))
workdays = 365-n
total = 30000
during_workdays = workdays * 63
during_holidays = n*127
playing_time = during_workdays + during_holidays
if (playing_time >= total):
    print("can sleep well",(playing_time - total,"Hours"))
else:
    print("cant sleep well",total - playing_time,"Hours")

'''Most of the people start planning their vacations well in advance. A young programmer from
Bulgaria has a certain budget (BGN is the currency of Bulgaria) and spare time in a particular
season.
Write a program that accepts as input the budget and season and as output displays
programmer's vacation place and the amount of money they will spend.
The budget determines the destination, and the season determines what amount of the budget
will be spent. If the season is summer, the programmer will go camping, if it is winter – he will stay
in a hotel. If it is in Europe, regardless of the season, the programmer will stay in a hotel. Each
camp or hotel, according to the destination, has its price, which corresponds to a particular
percentage of the budget:
• If 100 BGN or less – somewhere in Bulgaria.
Summer – 30% of the budget
Winter – 70% of the budget.
• If 1000 BGN or less – somewhere in the Balkans.
Summer – 40% of the budget.
Winter – 80% of the budget.
• If more than 1000 BGN – somewhere in Europe.
Upon traveling in Europe, regardless of the season, the programmer will
spend 90% of the budget.'''

budget = int(input("Enter Budget : "))
s = input("Enter Season : ")

if (budget<=100):
    print("Bulgaria")
    if (s == 'summer'):
        print("Camping")
        print("Budget : ", budget*0.3)
    else:
        print("Hotel")
        print("Budget : ", budget*0.7)
elif (budget<=1000):
    print("Balkans")
    if (s == 'summer'):
        print("Camping")
        print("Budget : ", budget*0.4)
    else:
        print("Hotel")
        print("Budget : ", budget*0.8)
else:
    print("Europe")
    print("Hotel")
    print("Budget : ", budget*0.9)


