n = int(input("Enter N : "))
res = 0
for i in range(n,0, -1):
    res += i**3
print(res)