a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))
c = int(input("Enter The Third Number: "))
if (a>b and a>c):
    print(a, "is the Greatest")
elif(b>c and b>a):
    print(b, "is the Greatest")
else:
    print(c, "is the Greatest")