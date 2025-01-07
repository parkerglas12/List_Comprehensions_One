lst = ["Mare", "Cal", "Maven", "Kilhorn", "Iris", "Evangeline", "Farley", "Julian", "Shade", "Jon"]

# 1
print([name for name in lst if name[0] == "M"])

# 2
print([name for name in lst if len(name) > 4])

# 3 
print([name[0] for name in lst])

# 4
print([name.lower() for name in lst])

# 5
print([name for name in lst if "a" in name.lower()])

# 6
print([name for name in lst if len(name) % 2 == 0])

# 7
print([name for name in lst if "e" in name and len(name) > 5])

# 8
print([name for name in lst if name[1] == "a"])

# 9
print([(name, len(name)) for name in lst])

# 10
print([name for name in lst if name[1] in "aeiou"])

# 11
print(sum(1 for name in lst if len(name) > 5))

# 12 
print(sum(1 for name in lst if len(name) <= 5))

# 13
print(sum(len(name) for name in lst))

# 14
print(sum(1 for name in lst for letter in name.lower() if letter in "aeiou"))

# 15
print(sum(len(name) for name in lst) - sum(1 for name in lst for letter in name.lower() if letter in "aeiou"))

# 16
print([(name, "Short Name" if len(name) < 5 else "Long Name") for name in lst])

# 17
print([(name, "Even Length" if len(name) % 2 == 0 else "Odd Length") for name in lst])

# 18
print([(name, "Starts With Vowel" if name[0] in "aeiou" else "Starts With Consonant") for name in lst])

# 19
print([(name, "Large Ord Score" if sum(ord(letter) for letter in name) > 500 else "Small Ord Score") for name in lst])

# 20
print([(name, ">1 vowels" if sum(1 for letter in name.lower() if letter in "aeiou") > 1 else "1<= vowels", sum(ord(letter) for letter in name[::2])) for name in lst])