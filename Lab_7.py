# Q1. Write a program to reverse a string without using inbuilt function.

# str = "Programing"
# for i in range(len(str)-1, -1, -1):
#     print(str[i], end = '')

# Q2. Write a program to find the length of the last word in a sentence.

str = "My name is Krishna"
length = 0
for i in range (len(str)-1, -1, -1):
    if (str[i] == " "):
        break
    length += 1
print("Length of Last Word: ", length)