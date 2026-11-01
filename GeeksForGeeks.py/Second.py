txt = "GeeksForGeeks"
pat = "Fr"
for ch in pat:
    if ch in txt:
        print(chr(ch))
        break
else:
    print("-1")