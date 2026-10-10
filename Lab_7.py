# Q1. Write a program to reverse a string without using inbuilt function.

str = "Programing"
for i in range(len(str)-1, -1, -1):
    print(str[i], end = '')