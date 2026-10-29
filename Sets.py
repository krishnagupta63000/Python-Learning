#Q1. Write a Python program to create a set, add a new element to it, remove an element using remove(), and discard an element using discard().
# fruits = {"Apple", "Banana", "Cherry"}
# print(fruits)
# fruits.add("Mango")
# print(f'after add, {fruits}')
# fruits.remove("Banana")
# print(f'after remove, {fruits}')
# fruits.discard("Cherry")
# print("after discard ", fruits)


# Q2. Write a Python program to remove all elements from a set using .clear(), while keeping the variable itself intact.
# colours = {"red", "green", 'blue'}
# colours.clear()
# print(colours)

# Q3. Write a Python program to determine how many elements are in a set without using the built-in len() function.
# animals = {"cat", "dog", "bird", "fish"}
# count = 0
# for i in animals:
#     count += 1
# print(f"Lenght of Set: {count}")

sum = 0
s = set()
count = 0
for i in range (10):
    x = int(input())
    s.add(x)
    
for j in s:
    sum += j
    count += 1
    
print(count)
print (sum)
avg = sum / count 
print(avg)