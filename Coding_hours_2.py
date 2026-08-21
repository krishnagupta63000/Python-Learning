'''Q1. You are given two integers A and B. Using arithmetic operators, print their sum, difference (A - B), and
average in that order, each on a new line. The average should be printed as a floating-point number
rounded to 2 decimal places.'''

# a, b = map(int, input(). split())
# print(a+b)
# print(a-b)
# print(f"{(a+b)/2 :.2f}")

'''Q2. Given the principal amount P, rate of interest R (per annum), and time T (in years), calculate the Simple
Interest using the formula: SI = (P × R × T) / 100. Print the result rounded to 2 decimal place'''

p, r, t = input().split()
p, r, t = float(p), float(r), float(t)
si = (p*r*t)/100
print(f"{si:.2f}")