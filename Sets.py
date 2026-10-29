#Q1. Write a Python program to create a set, add a new element to it, remove an element using remove(), and discard an element using discard().
fruits = {"Apple", "Banana", "Cherry"}
print(fruits)
fruits.add("Mango")
print(f'after add, {fruits}')
fruits.remove("Banana")
print(f'after remove, {fruits}')
fruits.discard("Cherry")
print("after discard ", fruits)