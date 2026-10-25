'''Q1. Display the following addition table:'''

# print("\t     Addition Table")
# for j in range(0, 10):
#     print(j, end="   ")
# print()
# print("---------------------------------------")
# for i in range(1, 10):
#     print(i, end = " | ")
#     for j in range(1, 10):
#         if (i+j >= 10):
#             print(i+j, end = "  ")
#         else:
#             print(i + j, end="   ")
#     print()

'''Q2. Parking Slot Allotment. A parking area has slots numbered from 1 to 1000. Every slot whose
number is divisible by N is reserved. However, a reserved slot whose number is also divisible
by 4 is kept for electric vehicle charging and is not given to staff. Display the slot numbers
given to the staff. Use the continue statement with a while loop.'''


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
#     i += 1

i = 0
while (i<4):
    j = 0
    while (j<4-i):
        print("*", end = " ")
        j += 1
    print()
    i += 1