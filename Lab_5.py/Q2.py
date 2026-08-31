# Take a positive integer as input and display the sum of its digits. The number can be of any length.

n = int(input("Enter a number : "))
sum_digits = 0
while(n>0):
    digits = n % 10 
    sum_digits += digits
    n = n // 10
print("Sum of Digits: ", sum_digits)