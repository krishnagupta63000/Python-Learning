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
print()
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
    print("Weak Password")

