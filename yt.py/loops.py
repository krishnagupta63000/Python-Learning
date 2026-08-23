'''Print numbers from 1 to 100.'''

'''i = 1
while (i<=100):
    print(i)
    i += 1'''

'''Print numbers from 100 to 1.'''

'''i = 100
while (i>=1):
    print(i)
    i -= 1'''

'''Print the multiplication table of a number n.'''

'''n = int(input("Enter Number: "))
i = 1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i+=1'''

'''Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''

'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while (i<=(len(nums)-1)):
    print(nums[i])
    i+=1'''

'''Search for a number x in this tuple using loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)'''

'''nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter x : "))
i = 0
while (i < len(nums)):
    if (x == nums[i]):
        print("Found at index : ", i)
        break
    i+=1
else:
    print("Not Present in the Tuple.s")'''

'''Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''

'''list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list:
    print(i)'''

'''Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]'''

'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = int(input("Enter x : "))
i = 0
for val in nums:
    if (x == val):
        print("Found at index : ", i)
        break
    i += 1
else:
    print("Not Found.")'''

'''Print numbers from 1 to 100.'''

for i in range(1,101):
    print(i)