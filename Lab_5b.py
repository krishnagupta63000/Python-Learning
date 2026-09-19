# Q1, Street Lamps on a Highway. The lamp posts on a highway are numbered from X to Y. Every
# post whose number is divisible by N is out of order. Display the numbers of the posts that are
# still working, along with how many of them there are. Consider the posts numbered X ≤ i < Y.
# Input: Three integers X, Y and N, each on a separate line.
# Output: In the first line, the numbers of the working posts separated by a single space. In the
# second line, the count of working posts.
# Constraints: 1 ≤ X < Y ≤ 10000, 1 ≤ N ≤ 100.
# In the second case every post is divisible by 1, so no post is working and the first line of the output stays
# empty.

# X = int(input("Enter X : "))
# Y = int(input("Enter Y : "))
# N = int(input("Enter N : "))

# count = 0

# for i in range(X, Y):
#     if i % N != 0:
#         print(i, end=" ")
#         count += 1

# print()
# print(count, "Count")

# Q2, Take a positive integer as input and display the product of its digits. The number can be of any
# length.
# n = int(input("Enter N : "))
# product = 1
# while (n>0):
#     digit = n % 10
#     product = product * digit
#     n = n // 10
# print(product)


#Q4, Take a positive integer N and a positive integer P as input and find the value of N raised to the
# power P using a while loop. Do not use the ** operator or the pow() function. Handle invalid
# cases as well.

# n = int(input("Enter Number : "))      #3
# p = int(input("Enter Power : "))        #3                                  #3 * 3 * 3
# if (n<=0 or p<=0):
#     print("Invalid Input")
# else:
#     result = 1
#     i = 1
#     while (i <= p):
#         result *= n
#         i += 1
# print(result)



#Q5, Take two positive integers as input. Check whether the second number is the exact reverse of
# the first one. Do not use any inbuilt reverse functions.

# og = int(input("Enter First Number : "))
# rev = int(input("Enter Second Number : "))
# if (og<= 0 or rev<=0):
#     print("Invalid Number")
# else:
#     reverse = 0
#     while(og>0):
#         digit = og % 10
#         reverse = reverse * 10 + digit
#         og //= 10
# if (reverse == rev):
#     print("Exact Reverse")
# else:
#     print("Not Exact Reverse")


#Q3, Canteen Billing Counter. The canteen cashier enters the amount of every bill of the day one
# by one. To close the counter, the cashier enters -999. A bill is called a large bill if its amount is
# greater than N, otherwise it is a small bill. Count the large bills and the small bills of the day.
# Input: The first line contains the integer N. Every following line contains one bill amount. The
# input ends with the value -999, which is not a bill.
# Output: Print the count of large bills in the first line and the count of small bills in the second
# line.
# Constraints: 1 ≤ N ≤ 100000, at most 100 bills are entered, every bill amount is a positive
# integer.

# N = int(input())

# large = 0
# small = 0

# while True:
#     bill = int(input())

#     if bill == -999:
#         break

#     if bill > N:
#         large += 1
#     else:
#         small += 1

# print(large)
# print(small)


#Q6, Display the first N terms of the sequence of powers of 2. Do not use the ** operator or the
# pow() function.
# 1, 2, 4, 8, 16, 32, ….. till N terms

n = int(input("Enter N : "))
i = 1
power = 1 
while (i<=n):
   print(power)
   power = power * 2
   i += 1


# Take an integer as input and check whether it is a perfect number or not (a perfect number is
# equal to the sum of all its divisors other than itself, for example 28 = 1 + 2 + 4 + 7 + 14). Handle
# invalid conditions and make your code efficient by minimizing the number of loop iterations.

n = int(input("Enter Number : "))

if (n <= 0):
    print("Invalid Number")

elif (n == 1):
    print("Not a Perfect Number")

else:
    sum = 1
    i = 2

    while (i * i <= n):
        if (n % i == 0):
            sum += i

            if (i != n // i):
                sum += n // i

        i += 1

    if (sum == n):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")



# Take a positive integer N as input and display the following pattern of N lines:
# \*
# \* \*
# \* \* \*
# \* \* \* \*
# (till N lines)


n = int(input("Enter N : "))

if (n <= 0):
    print("Invalid Number")
else:
    i = 1
    while (i <= n):
        j = 1
        while (j <= i):
            print("*", end=" ")
            j += 1
        print()
        i += 1



# Take a positive integer and a single digit D (0 to 9) as input. Count how many times the digit D
# appears in the number. Do not convert the number into a string.



number = int(input("Enter Number : "))
D = int(input("Enter Digit : "))

count = 0

while number > 0:
    digit = number % 10

    if digit == D:
        count = count + 1

    number = number // 10

print(count)


# Take a positive integer N as input and display all its divisors, one in each line, followed by the
# total count of divisors. Using this count, print whether N is a prime number or not.



N = int(input("Enter N : "))

if N <= 0:
    print("Invalid Number")
else:
    count = 0

    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
            count += 1

    print("Total divisors :", count)

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")




'''Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a
second point (x2, y2), and displays whether the second point lies inside, on the boundary of, or
outside the circle. The formula for computing the distance between two points is
distance = √[(x2 – x1)2 + (y2 – y1)2]'''

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
r = float(input("Enter radius: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance < r:
    print("Point is inside the circle")
elif distance == r:
    print("Point is on the boundary of the circle")
else:
    print("Point is outside the circle")