# num = [1, 2, 4, 5]
# print(sum(num))

# for i in range (3):
#     for j in range (3):
#         if i == j:
#             break
#         else:
#             print("Inner Completed for i =", i)
#     print("Outer continues, i =", i)



# a = 256
# b = 77
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)


# x = 6
# y = 3
# if x % y == 0 or x // y == 2 and x * y > 20:
#     print("True Branch")
# else:
#     print("False Branch")


# x = 0.1
# total = 0
# for i in range(10):
#     total += x
# if total == 1.0:
#     print("Exact")
# elif total > 1.0:
#     print("Slightly Over")
# else:
#     print("Slightly Under")
# print(total)


# x = -2**2
# if not x > 0:
#     if x == -4:
#         if not (-x == 4):
#             print("A")
#         else:
#             print("B")
#     else:
#         print("C")
# elif x == 4:
#     print("D")
# else:
#     print("E")


# for row in range (1,6):
#     for pos in range(1,row+1):
#         if pos == 1 or pos == row:
#             print("D", end = " ")
#         elif(row + pos) % 2 == 0:
#             print("R", end = " ")
#         else:
#             print("Y", end = " ")
#     print()


# str = input()
# vowels = 0
# consonants = 0
# space = 0
# digits = 0
# for ch in str :
#     if ch in "AEIOUaeiou":
#         vowels += 1
#     elif (ch == " "):
#         space += 1
#     elif (ch>"0" and ch<"9"):
#         digits += 1
#     else:
#         consonants += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants) 
# print("Digits:", digits)
# print("Spaces:", space)



# for i in range (5):
#     for j in range (i+1):
#         print("*", end= " ")
#     print()

              
# for i in range(5, 0, -1):
#     for j in range (i):
#         print("*", end=" ")
#     print()


# for i in range (4):
#     for j in range (1, 5):
#         print(j, end=" ")
#     print()

# n = int(input("Enter N: "))
# for i in range (n):
#     for j in range (n):
#         print("*", end=" ")
#     print()


# for i in range (4):
#     for j in range (4):
#         print(chr(65+j), end=" ")
#     print()

# num = 1
# for i in range (3):
#     for j in range (3):
#         print(num, end=" ")
#         num += 1
#     print()



# for i in range(4):
#     num = 1
#     for j in range (4):
#         print(num, end = " ")
#         num += 1
#     print()


# n = 65
# for i in range (3):
#     for j in range (3):
#         print(chr(n), end = " ")
#         n += 1
#     print()

# n = int(input("Enter N: "))
# for i in range (n):
#     for j in range (i+1):
#         print("*", end = " ")
#     print()


# n = 1
# for i in range (4):
#     for j in range (i+1):
#         print(i+1, end = " ")
#     print()

# for i in range (5):
#     for j in range (i+1):
#         print(chr(i+65), end = " ")
#     print()


# for i in range(4):
#     n = 1
#     for j in range (i+1):
#         print(n, end = " ")
#         n += 1
#     print()

# for i in range (4):
#     for j in range (i+1, 0, -1):
#         print(j, end=" ")
#     print()

# n = 1
# for i in range (4):
#     for j in range (i+1):
#         print(n, end = " ")
#         n += 1
#     print()


# n = 65
# for i in range (4):
#     for j in range (i+1):
#         print(chr(n), end = " ")
#         n += 1
#     print()


# n = 65
# for i in range (4):
#     n += 1
#     for j in range (i+1, 0, -1):
#         print(chr(n-1), end = " ")
#         n +=1 
#     print()


# n = 0
# for i in range (4):
#     for j in range (i):
#         print(" ", end = " ")
#     n += 1
#     for j in range (4-i):
#         print(n, end = " ")
#     print()



# n = int(input())
# print()
# for i in range (n):
#     d = 1
#     for j in range (i+1):
#         print(d, end = " ")
#         d += 1
#     print()



# n = int(input())
# print()
# i = 0
# while (i<n):
#     j = 0
#     d = 1
#     while (j < (i+1)):
#         print(d, end = " ")
#         d += 1
#         j += 1
#     i += 1
#     print()


# n = int(input())
# print()
# for i in range (n):
#     for j in range (n-i):
#         print("*", end = " ")
#     print()


n = int(input())
i = 0
while (i<n):
    j = 0
    while(j < (n-i)):
        print("*", end = " ")
        j += 1
    i += 1
    print()