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


for row in range (1,6):
    for pos in range(1,row+1):
        if pos == 1 or pos == row:
            print("D", end = " ")
        elif(row + pos) % 2 == 0:
            print("R", end = " ")
        else:
            print("Y", end = " ")
    print()