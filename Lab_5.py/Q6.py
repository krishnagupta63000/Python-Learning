# Display the first N terms of the Fibonacci sequence starting from 1.
# 1, 1, 2, 3, 5, ….. till N terms

n = int(input("Enter N : "))
first = 1
second = 1
i = 1
while (i<=n):
    print(first)
    next = first + second
    first = second
    second = next
    i += 1
