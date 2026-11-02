'''Q1. Read a line of space-separated integers and store the even and odd numbers in two separate
lists. Print both lists.'''
s = list(map(int, input().split()))
even = []
odd = []
for i in range (6):
    if (s[i] % 2 == 0):
        even.append(s[i])
    else:
        odd.append(s[i])
print(f"Even: {even}")
print(f'Odd: {odd}')

