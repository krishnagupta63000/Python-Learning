# ques 3, 
votes = input().split()
d = {}
for name in votes:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
for name in d:
    print(f"{name}, : {d[name]}")
highest = 0
winner = ""
for name in d:
    if (d[name] > highest):
        highest = d[name]
        winner = name
print("Winner: ", winner)



# ques 6, 
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
n = int(input())
d = {}
for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    grade = get_grade(marks)
    print(name, ":", grade)
    if grade in d:
        d[grade] += 1
    else:
        d[grade] = 1
print("Grade Count: ", d)



# Ques 8 
n = int(input())
d = {}
for i in range(n):
    country, capital = input().split()
    d[country] = capital
name = input()
if name in d:
    print(d[name])
else:
    print("Not Found")



# Ques 9, 
n = int(input())
d = {}
for i in range(n):
    item, qty = input().split()
    d[item] = int(qty)
q = int(input())
for i in range(q):
    action, item, qty = input().split()
    qty = int(qty)
    if action == "Sell":
        if d[item] >= qty:
            d[item] -= qty
        else:
            print("Insufficient Stock: ", item)
    else:
        if item in d:
            d[item] += qty
        else:
            d[item] = qty
for items in d:
    print(item, d[item])


# my streak is geting very hard right now 
# ghee khatam