# Take a positive integer N as input and find its Factorial using a while loop. Handle invalid cases as
# well.

n = int(input("Enter a number : ")) #5! = 1*2*3*4*5
fact = 1
i = 1
while(i<n+1):
    fact=fact*i
    i += 1
print("Factorial of", n, "is", fact)

