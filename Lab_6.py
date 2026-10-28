'''Q1. Display the following addition table:'''

print("\t     Addition Table")
for j in range(0, 10):
    print(j, end="   ")
print()
print("---------------------------------------")
for i in range(1, 10):
    print(i, end = " | ")
    for j in range(1, 10):
        if (i+j >= 10):
            print(i+j, end = "  ")
        else:
            print(i + j, end="   ")
    print()

'''Q2. Parking Slot Allotment. A parking area has slots numbered from 1 to 1000. Every slot whose
number is divisible by N is reserved. However, a reserved slot whose number is also divisible
by 4 is kept for electric vehicle charging and is not given to staff. Display the slot numbers
given to the staff. Use the continue statement with a while loop.'''

#  n = int(input("enter n :"))
# i = n 
# while i<= 1000:
#     if i % 4!= 0:
#         print(i,end =" ")
#     i = i+n 

'''Q3. Display the following patterns for N lines (value of N taken from the user) using while loop:'''

# for i in range (4):
#     n = 1
#     for j in range (i+1):
#         print(n, end = " ")
#         n += 1
#     print()

# i = 0
# while (i<4):
#     n = 1
#     j = 0
#     while (j<i+1):
#         print(n, end = " ")
#         n += 1
#         j += 1
#     print()
    # i += 1

# i = 0
# while (i<4):
#     j = 0
#     while (j<4-i):
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1

# i = 0
# while (i<4):
#     j = 0
#     while (j<(3-i)):
#         print(" ", end = " ")
#         j += 1
#     j = 0
#     while (j<(i+1)):
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1

'''Q4. Take a positive integer as input from the user and display its octal equivalent via the repeated
division method. (without using any inbuilt function or format specifier). The final result
should be displayed as a string. Check if the result matches the output of inbuilt oct() function.'''
# n =int(input("enter n:"))
# ans = " " 
# for i in range(n):
#     if n == 0:
#         break
#     r = n % 8
#     ans = str(r) +ans
#     n = n// 8
# print()   

'''Q5.Sports Day Javelin Throw. N students take part in the javelin throw event and the distance
thrown by each of them is recorded. Find the winning distance and the runner-up distance,
where the runner-up distance is the largest distance that is strictly smaller than the winning
one. Do not use any inbuilt function.
Input: The first line contains the integer N. The next N lines contain one distance each (a
positive integer, in metres).
Output: Print the winning distance in the first line and the runner-up distance in the second
line.
Constraints: 2 ≤ N ≤ 100. At least two different distances are recorded.'''


# n = int(input("enter n:"))
# winner = 0
# runner = 0
# for i in range(n):
#     x = int(input("enter distance:"))
#     if x > winner:
#         runner = winner
#         winner = x
#     elif x> runner and x< winner:
#         runner = x 
# print("winner =",winner)
# print("runner_up =",runner) 

'''Q6. Display all the Armstrong numbers between 1 and N, where the value of N is taken as input
from the user.'''

# n =   int(input("Enter a number: "))
# original = n
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** 3
#     n = n // 10
# if sum == original:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")


'''Q7. Print the following table to display the square, cube and square root of the numbers from 1
to 15. Round the value to keep four digits after the decimal point.'''

# i = 1
# print("Number\tSquare\tCube\tSquare Root")
# print("----------------------------------------------")
# while i <= 15:
#     square = i * i
#     cube = i * i * i
#     root = i ** 0.5
#     print(i, "\t", square, "\t", cube, "\t", round(root, 4))
#     i = i + 1

'''Q8. Display the following pattern using nested loops:
     1
    2 2
   3 3 3
  4 4 4 4
(till N lines)'''

# n = 0
# for i in range (4):
#     n += 1
#     for j in range (4-i):
#         print(" ", end = "")
#     for j in range (i+1):
#         print(n, end = " ")
#     print()

'''Q9. Display the following triangle of consecutive numbers using nested loops:
1
2 3
4 5 6
7 8 9 10
(till N lines)'''

# n = 1
# for i in range(4):
#     for j in range (i+1):
#         print(n, end = " ")
#         n += 1
#     print()

'''Q10. Take an odd positive integer N as input and display the following diamond pattern of N lines
using nested loops:
   *
  ***
 *****
  ***
   *
(shown for N = 5)'''

# for i in range(3):
#     for j in range (3-i):
#         print(" ", end = " ")
#     for j in range (2*i + 1):
#         print("*", end = " ")
#     print()
# for i in range(2):
#     for j in range(i+2):
#         print(" ", end=" ")
#     for j in range(3 - 2 * i):
#         print("*", end=" ")
#     print()