'''Q1. Read a line of space-separated integers and store the even and odd numbers in two separate
lists. Print both lists.'''
# s = list(map(int, input().split()))
# even = []
# odd = []
# for i in range (6):
#     if (s[i] % 2 == 0):
#         even.append(s[i])
#     else:
#         odd.append(s[i])
# print(f"Even: {even}")
# print(f'Odd: {odd}')



'''Q2. Read a sentence and build a list of all the words that have more than 3 letters, in the order
they appear. Print the list.'''

s = input().split()
l = []
for i in s:
    if (len(i) > 3):
        l.append(i)
    else:
        continue
print(f'{l}')