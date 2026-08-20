n = float(input("Enter Attandance: "))
if(n>=75):
    print("Good!, You're Eligible for Exams")
elif(n<0 or n>100):
    print("Invalid Input")
else:
    print("Not Eligilbe for Exams")