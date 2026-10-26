#1
s = input("Enter a string: ")
reversed_str = ""
for char in s:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)
#2
sentence = input("Enter a sentence: ")
last_word_len = 0
current_len = 0
for char in sentence:
    if char == " ":
        if current_len > 0:
            last_word_len = current_len  
            current_len = 0  
    else:
        current_len += 1
if current_len > 0:
    last_word_len = current_len
print("Length of the last word:", last_word_len)
#3.1
s = input("Enter a sentence: ")
w = input("Enter a word to search: ")
if w in s:
    print(f"Yes, the word '{w}' exists in the sentence.")
else:
    print(f"No, the word '{w}' does not exist.")
print(f"The word '{w}' occurs {sentence.count(w)} time(s).")   
#3.2
 

#4
text = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for char in alphabet:
    if char not in text:
        is_pangram = False
        break

if is_pangram:
    print("It is a pangram!")
else:
    print("It is NOT a pangram.")
#5
text = input("Enter a message: ")
shift = int(input("Enter the shift number: "))
encrypted_text = ""

for char in text:
    if char.isupper():
        # Shift uppercase letters
        encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        # Shift lowercase letters
        encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        # Keep spaces, numbers, and punctuation as they are
        encrypted_text += char

print("Encrypted message:", encrypted_text)
#6
counts = [0, 0, 0, 0, 0]  # For ranges: [1-2, 3-4, 5-6, 7-8, 9-10]
total_numbers = 0

print("Enter numbers between 1 and 10 (Enter -1 to stop):")
while True:
    num = int(input())
    if num == -1:
        break
    if 1 <= num <= 2:
        counts[0] += 1
    elif 3 <= num <= 4:
        counts[1] += 1
    elif 5 <= num <= 6:
        counts[2] += 1
    elif 7 <= num <= 8:
        counts[3] += 1
    elif 9 <= num <= 10:
        counts[4] += 1
    total_numbers += 1

ranges = ["1-2", "3-4", "5-6", "7-8", "9-10"]

for i in range(5):
    percentage = (counts[i] / total_numbers * 100) if total_numbers > 0 else 0.00
    hashes = "#" * counts[i]
    print(f"{ranges[i]}:{hashes}{percentage:.2f}%")

#7
s = input("Enter a string: ")
n = len(s)
is_pal = True

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_pal = False
        break

if is_pal:
    print("It is a palindrome.")
else:
    print("It is NOT a palindrome.")
#8
n = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers = numbers + [num]
total_sum = 0
product = 1
smallest = numbers[0]
for x in numbers:
    total_sum += x
    product *= x
    if x < smallest:
      smallest = x
print("Sum of numbers:", total_sum)
print("Product of numbers:", product)
print("Smallest number:", smallest)
#9
nums = [int(x) for x in input("Enter integers separated by space: ").split()]
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the element found is smaller than the next element
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("List sorted in descending order:", nums)
#10
sequence = input("Enter a hyphen-separated sequence of words: ")
words = sequence.split("-")
n = len(words)
for i in range(n):
    for j in range(0, n - i - 1):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]

sorted_sequence = "-".join(words)
print("Expected Result:", sorted_sequence)
#11
p = input("Enter a paragraph: ")
digits = 0
alphabets = 0
special = 0
upper = 0
lower = 0

for char in p:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
        if char.isupper():
            upper += 1
        else:
            lower += 1
    else:
        special += 1

print(f"Alphabets: {alphabets} (Uppercase: {upper}, Lowercase: {lower})")
print(f"Digits: {digits}")
print(f"Special characters: {special}")
#12
s = input("Enter a string: ")
result = ""

for char in s:
    if char not in result:
        result += char

print("Without duplicates:", result)