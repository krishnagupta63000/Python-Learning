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

# s = input().split()
# l = []
# for i in s:
#     if (len(i) > 3):
#         l.append(i)
#     else:
#         continue
# print(f'{l}')

'''Q3. The JKLU inter-hostel cricket league keeps a ball-by-ball record of every innings as a single line.
Each ball is recorded as the runs scored on it (0, 1, 2, 3, 4 or 6), or as W if a wicket fell (no runs
on that ball). An over has 6 balls, and the last over may be incomplete. The scorer wants the
total runs, the number of wickets, the number of boundaries (balls on which 4 or 6 was
scored), and a list of runs scored in each over.
Input: A single line containing the ball-by-ball record, separated by spaces.
Output: Print the total runs, wickets, boundaries and the list of runs per over, as shown in the
samples.
Constraints:
1 ≤ number of balls ≤ 120'''

s = input().split() 
for i in s:
    if (i == "W"):
        continue
    else:
        i = int(i)
total = 0
wicket = 0
boundary = 0
for i in range(6):
    if (s[i] == "W"):
        wicket += 1
    else:
        total += s[i]
        if (s[i] == 4 or s[i] == 6):
            boundary += 1
        
    