# Q1, Street Lamps on a Highway. The lamp posts on a highway are numbered from X to Y. Every
# post whose number is divisible by N is out of order. Display the numbers of the posts that are
# still working, along with how many of them there are. Consider the posts numbered X ≤ i < Y.
# Input: Three integers X, Y and N, each on a separate line.
# Output: In the first line, the numbers of the working posts separated by a single space. In the
# second line, the count of working posts.
# Constraints: 1 ≤ X < Y ≤ 10000, 1 ≤ N ≤ 100.
# In the second case every post is divisible by 1, so no post is working and the first line of the output stays
# empty.



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



#Q4, Take two positive integers as input. Check whether the second number is the exact reverse of
# the first one. Do not use any inbuilt reverse functions.

og = int(input("Enter First Number : "))
rev = int(input("Enter Second Number : "))
if (og<= 0 or rev<=0):
    print("Invalid Number")
else:
    reverse = 0
    while(og>0):
        digit = og % 10
        reverse = reverse * 10 + digit
        og //= 10
if (reverse == rev):
    print("Exact Reverse")
else:
    print("Not Exact Reverse")


#Q3, Canteen Billing Counter. The canteen cashier enters the amount of every bill of the day one
# by one. To close the counter, the cashier enters -999. A bill is called a large bill if its amount is
# greater than N, otherwise it is a small bill. Count the large bills and the small bills of the day.
# Input: The first line contains the integer N. Every following line contains one bill amount. The
# input ends with the value -999, which is not a bill.
# Output: Print the count of large bills in the first line and the count of small bills in the second
# line.
# Constraints: 1 ≤ N ≤ 100000, at most 100 bills are entered, every bill amount is a positive
# integer.

N = int(input())

large = 0
small = 0

while True:
    bill = int(input())

    if bill == -999:
        break

    if bill > N:
        large += 1
    else:
        small += 1

print(large)
print(small)