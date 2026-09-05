p = int(input("Enter Principle Amount : "))
r = int(input("Enter Rate of Interest : "))
t = int(input("Enter amount of Time : "))
a = p*(1+r/100)**t
print("Compound Interest : ", a)