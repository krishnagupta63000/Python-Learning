#average of 3 numbers
'''def avgOf (a, b, c):
    print(avgOf)
    return (a+b+c)/3

print(avgOf(1, 2, 3))'''

# product of 3 numbers 
'''def product(a, b, c):
    return a*b*c
print(product(2,3,4))'''

# WAF to print the length of a list. (list is the parameter)

'''fruits = ['apple', 'banana', 'orange']
marks = [90, 98, 75, 74, 78]
def lengthOf(list):
    print(len(list))
lengthOf(fruits)
lengthOf(marks)'''

# WAF to print the elements of a list in a single line. (list is the parameter)
'''marks = [90, 98, 75, 74, 78]
def elementsof(list):
    for i in range (5):
        print(list[i])

elementsof(marks)'''

# WAF to find the factorial of n. (n is the parameter)

'''n = int(input("Enter N : "))
fact = 1
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return(fact)
print(fact(n))'''

# WAF to convert USD to INR.

'''USD = int(input("Enter amount in USD : "))
def convert(USD):
    INR = USD*94
    print("₹",INR)
convert(USD)'''

#Even or Odd from function

n = int(input("Enter Any Number : "))
def tell(n):
    if (n%2==0):
        return "Even Number"
    else:
        return "Odd Numbers"
print(tell(n))
