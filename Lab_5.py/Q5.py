# Take a positive integer as input. It may be of any length. Check if it is palindrome or not. Do not
# use any inbuilt reverse functions.

n = int(input("Enter Number : "))
original = n
reversed_digit = 0
while (n>0):
    last_digit = n % 10
    reversed_digit = reversed_digit * 10 + last_digit
    n = n // 10
if (original== reversed_digit):
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")