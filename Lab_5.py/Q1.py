# Take 2 numbers as input (X and Y) and a third number N. Display all the numbers between X and Y
# (X < i <= Y) that are divisible by N.

x = int(input("Enter X : "))
y = int(input("Enter Y : "))
n = int(input("Enter N : "))
for i in range(y,x,-1):
    if (i % n == 0):
        print(i)