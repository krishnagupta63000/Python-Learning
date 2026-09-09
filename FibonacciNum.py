n = int(input("Enter Number : "))
first = 1
second = 1
i = 1
while (i<=n):
    print(first)
    next = first + second
    first = second 
    second = next
    i += 1
print(next)