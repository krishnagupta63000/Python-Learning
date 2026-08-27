'''Write a program that takes a number and prints whether it is positive, negative, or zero.'''
n = int(input("Enter Number : "))
if (n>0):
    print(n, "Positive Number")
elif(n==0):
    print(n, "Zero")
else: 
    print(n, "Negative Number")