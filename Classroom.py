#Q.
'''You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"python",
" "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C"'''

# set = {'jawa', 'python', "C++", "python", "jawascript", "jawa", "python", "jawa", "C++", "C"}
# print(len(set), "Classrooms")


'''marks = [76, 67, 90, 69, 67, 58]
marks.append(65)
marks.insert(1, 82)
marks.remove(58)
marks.pop()
print(marks)'''

# fruits = ["Apple", "Banana", "Cherry"]
# for ch in fruits:
#     print(ch)

# fruits = ["Apple", "Banana", "Cherry"]
# [print(x) for x in fruits]


# fruits = ["Apple", "Banana", "Cherry"]
# fruits1 = [x for x in fruits if "a" in fruits]
# print(fruits1)

# fruits =["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if "a" in x else " " for x in fruits]
# print(newlist)

# n = 5
# star = [j for i in range(n) for j in range(n-i)]
# print(star)

# [print("* "*n) for n in range (1, 10)]

# l = []
# n = 5
# for i in range (n):
#     l.append(int(input()))
# product = 1
# for j in l:
#     product *= l
# print(product)


# l = [8, 5, 3, 1, 5]
# for i in range(len(l)):
#     for j in range(len(l) - (i+1)):
#         if (l[j+1] < l[j]):
#             l[j+1], l[j] = l[j], l[j+1]
# print(l)

# marks = (90, 88, 90)
# print(marks.count(90))

# t = (10,)
# t1 = (20)
# t3 = ()
# # print(type(t))
# # print(type(t1))
# t4 = t3 + t
# print(t4)
# print(type(t4))


t1 = (10, 20)
t2 = t1 + (30, )
print(t2)
t3 = t2[1:3]
print(t3)