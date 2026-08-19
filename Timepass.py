# sum = 0
# n = int(input("Enter Num: "))
# while (n!=1):
#     n = int(input("Enter Num: "))
#     if(n!=1):
#         sum+=n
#         print(sum)
#     else:
#         sum+=n
#         print(sum-1)

#mini calculator->
n = int(input("Enter first num: "))
opp = input("Enter Operator: ")
n2 = int(input("Enter Second num: "))
if(opp == "+"):
    print("sum:", n + n2 )
elif(opp == "-"):
    print("diffrence: ", n - n2)
elif(opp== "/"):
    print("division: ", n/n2)
elif(opp == "*"):
    print("Multiplication: ", n*n2)
else:
    print("Invalid Operator")


import.random