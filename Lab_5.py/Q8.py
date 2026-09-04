# Take a sentence as input and using while loop count the number of capital letters, small letters,
# digits, and special characters in the sentence. Do not use any inbuilt function.

str = input("Enter a sentance : ")
capital = 0
small = 0
digits = 0
special_ch = 0
i = 0
while (i < len(str)):
    if (str[i]>= "A" and str[i]<="Z"):
        capital += 1
    elif(str[i]>="a" and str[i]<="z"):
        small += 1
    elif(str[i]>="0" and str[i]<="9"):
        digits += 1
    elif(str[i] == " "):
        pass
    else:
        special_ch += 1
    i += 1
print("Number of Capital Letters : ", capital)
print("Number of Small Letters : ", small)
print("Number of Digits : ", digits)
print("Number of Special Characters : ", special_ch)