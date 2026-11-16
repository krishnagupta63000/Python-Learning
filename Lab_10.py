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



