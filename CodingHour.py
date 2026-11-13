#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:19:27 2026

@author: krishnagupta63000gmail.com
"""
# l = [8, 5, 3, 1, 5]
# for i in range(len(l)):
#     for j in range(len(l) - (i+1)):
#         if (l[j+1] < l[j]):
#             l[j+1], l[j] = l[j], l[j+1]
# print(l)


# n = int(input())
# words = input().split()
# count = {}
# for i in range(n):
#     w = words[i]
#     if w in count:
#         count[w] =


# def add (a, b):
#     print(a+b)

# add(3, 4)
# add(10, 5)


# def add (a, b):
#     return a + b
# x = add (2, 3)
# print(x * 10)


# def check(n):
#     if n > 0:
#         return "Positive"
#     return "Not Positive"

# print (check(5))
# print(check(-2))


# def f():
#     return 1 
#     print(2)
# print(f())


def f(n):
    if (n == 0 or n == 1):
        return 1
    return n * f(n-1)
n = int(input("Enter Number: "))
print(f"Factorial of {n} is {f(n)}")