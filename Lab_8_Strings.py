# Q1. Read a string and count how many characters in it are vowels, consonants, digits, spaces and
# other symbols.

s = input().lower()
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
print(f"Others {sp_ch}")