# Count Even Digits

n = int(input("Enter a Number : "))
count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count += 1
    n = n // 10
print("Even digits:", count)