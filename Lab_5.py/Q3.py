# Take a positive integer N as input followed by repeatedly taking numbers from the user till the time
# user entered -999. At the end display the count of input numbers that are divisible by N and the
# count of input numbers that are not divisible by N.

N = int(input("Enter a positive number : "))
i = 0
divisible = 0
not_divisible = 0
while (True):
    num = int(input("Enter any number : "))
    if (num == -999):
        break
    if (num % N == 0):
        divisible += 1
    else:
        not_divisible += 1
print ("Divisile : ", divisible)
print("Not Divisile : ", not_divisible)



    
    