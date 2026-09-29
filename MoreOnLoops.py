# WAP to print all natural numbers from 1 to n. - using while loop

n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i += 1



# WAP to print all natural numbers in reverse (from n to 1). - using while loop


n = int(input("Enter N: "))

while n >= 1:
    print(n)
    n -= 1



# WAP to print all alphabets from a to z. - using while loop Hint:chr()


i = 97

while i <= 122:
    print(chr(i))
    i += 1


# WAP to print all even numbers between 1 to 100. - using while loop

i = 1

while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1


# WAP to print all odd number between 1 to 100.

i = 1

while i <= 100:
    print(i)
    i = i + 2


# WAP to find sum of all natural numbers between 1 to n.


n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)



# WAP to find sum of all even numbers between 1 to n.

n = int(input("Enter n: "))
total_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum = total_sum + i

print("Sum:", total_sum)

