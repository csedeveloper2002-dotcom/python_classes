s = input("Enter a string: ")

found = False
for ch in s:
    if ch.isdigit():
        found = True
        break

if found:
    print("String contains a digit")
else:
    print("String does not contain any digit")
