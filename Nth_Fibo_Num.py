number = int(input("Enter Number : "))
N = int(input("Enter Nth term : "))

first = 1
second = 1
i = 1
total = 0

while (total < N):
    if (first % number == 0):
        total += 1

        if (total == N):
            print(first)

    next = first + second
    first = second
    second = next
    i += 1