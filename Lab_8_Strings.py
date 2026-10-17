# Q1. Read a string and count how many characters in it are vowels, consonants, digits, spaces and
# other symbols.

'''s = input().lower()
vovels = 0
digits = 0
consonants = 0
spaces = 0
sp_ch = 0
for ch in s:
    if ch in "aeiou":
        vovels += 1
    elif ch in "qwertyuiopasdfghjklzxcvbnm" and ch not in "aeiou":
        consonants += 1
    elif  ch in "1234567890":
        digits += 1
    elif ch == " " :
        spaces += 1
    else:
        sp_ch += 1
print(f"Vovals: {vovels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Others {sp_ch}")'''


# Q2. Read a string and rewrite it so that the characters at even positions (0, 2, 4, …) are in
# uppercase and those at odd positions are in lowercase. Characters that are not letters stay
# unchanged but still occupy a position.

'''s = input()
for i in range(len(s)):
    if (s[i] == " "):
        print(" ", end = '')
        continue
    elif (i%2==0):
        print(s[i].upper(), end = '')
    else:
        print(s[i].lower(), end = '')'''

# Q3. JKLU's student portal is rolling out a new sign-up page. Before an account is created, the portal
# rates the password the student types. It looks for four kinds of characters: an uppercase letter,
# a lowercase letter, a digit, and a special character (anything that is not a letter, digit or space).
# A password shorter than 8 characters is always WEAK. Otherwise it is STRONG if all four kinds
# are present, MODERATE if two or three kinds are present, and WEAK if only one kind is
# present.
'''print()
print("         Sign-up Page")
print()

s = input("Type Password: ")
count = 0
uppercase = 0
lowercase = 0
digits = 0
specialchar = 0

for ch in s:
    if ch in "QWERTYUIOPASDFGHJKLZXCVBNM":
        count += 1
        uppercase = 1

    elif ch in "qwertyuiopasdfghjklzxcvbnm":
        count += 1
        lowercase = 1

    elif ch in "1234567890":
        count += 1
        digits = 1

    elif ch != " ":
        count += 1
        specialchar = 1

typee = uppercase + lowercase + digits + specialchar

if typee == 4 and count >= 8:
    print("Strong Password")

elif (typee == 2 or typee == 3) and count >= 8:
    print("Moderate Password")

else:
    print("Weak Password")'''


# Q4. Read a string and a single character. Print how many times the character occurs in the string
# and the index of every occurrence. If it does not occur, print -1 for the positions.

'''s = input()
ch = input()
count = 0
pos = 0
l = []
for i in s:
    if (ch == i):
        count += 1
        l.append(pos)
# else:
#     print("-1")
    pos += 1
if (count > 0):
    print("Count:", count)
    print()
    print(f"Positions: {l}")
    print()
else:
    print("Count:", count)
    print(f"Position: -1")'''


# Q5. Read a sentence and print the length of each word in it, in order, on one line. Words are
# separated by one or more spaces, and the sentence may begin or end with spaces.

s = input().lower()
count = 0
for ch in s:
    if (ch != " "):
        count += 1
    elif (count > 0):
        print(f"{count}", end = " ")
        count = 0
if (count > 0):
    print(f"{count}", end = " ")