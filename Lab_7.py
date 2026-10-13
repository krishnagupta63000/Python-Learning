# Q1. Write a program to reverse a string without using inbuilt function.

# str = "Programing"
# for i in range(len(str)-1, -1, -1):
#     print(str[i], end = '')

# Q2. Write a program to find the length of the last word in a sentence.

# str = "My name is Krishna"
# length = 0
# for i in range (len(str)-1, -1, -1):
#     if (str[i] == " "):
#         break
#     length += 1
# print("Length of Last Word: ", length)

# Q3. Take a sentence and a word as input and check if the string contains the word in it. Also, count the
# number of times that word occurs in the string. Do this by using inbuilt string functions and then
# without using inbuilt string functions.

# str = "My name is Krishna"

# word = "Krishna"
# count =str.count(word)
# print("count:",count)
    


# Q4. program that takes a string as input and checks where the string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
str = "The quick brown fox jumps over the lazy dog"
str.lower
s = ''
count = 0
for ch in "qwertyuiopasdfghjklzxcvbnm":
    if ch not in str:
        print("Not a Pangram")
        break
else:
    print("Pangram")


# The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret
# messages to his allies. It works by shifting the letters in the plaintext message by a certain number
# of positions, known as the “shift” or “key”. Take a string as input from user which contains English
# alphabets only in lower or upper case. Also, take the shift (an integer) as input from the user. Write
# a program to convert the string into its corresponding Ceaser Cipher which also contains English
# alphabets only.

# str = "My name is Krishna Gupta"
# s = ''
# shift = 5
# for i in str:
#     if (i == " "):
#         print(""*5)

# print(str)



#Q7. Write a program to check if a string is palindrome or not without using any inbuilt function except
# len().
# str = "krirk"
# for i in 