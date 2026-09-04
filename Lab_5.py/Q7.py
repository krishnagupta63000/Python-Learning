# Take an integer as input and check if it is prime or not. Handle invalid conditions and make your
# code efficient by minimizing the number of loop iterations.

n = int(input("Enter Number : "))
if (n<=1):
    print("Not a Prime Number")
elif(n == 2):
    print("Prime Number ")
elif(n%2==0):
    print("Not a Prime Number")
else: 
    prime = True
    i = 3
    while(i**2 <= n):
        if (n % i == 0):
            prime = False
            break 
        i = i + 2
    if (prime):
        print("Its a Prime Number")
    else:
        print("Its not a Prime Number")
