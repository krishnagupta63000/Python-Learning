# def student(name, age):
#     print("Name of Student is: ", name, "Age: ", age)
# student("Amit", 20)
# student(20, "Amit")

# def student(name, age, sem = 1):
#     print("Name of the student", name, ", Age:", age, ", Semester:", sem)
# student("Krishna", 18)


x = 50
def show():
    x = 100
    print("Inside:", x)
show()
print("Outside:", x)