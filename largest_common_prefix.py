strs = input("Enter strings separated by space: ").split()

if not strs:
    print("")
else:
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                break

    print("Largest Common Prefix:", prefix)
