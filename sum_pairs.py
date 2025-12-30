arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter required sum: "))

seen = set()
pairs = set()

for num in arr:
    x = k - num
    if x in seen:
        pairs.add((min(num, x), max(num, x)))
    seen.add(num)

if pairs:
    print("Pairs with given sum:")
    for p in pairs:
        print(p)
else:
    print("No pairs found")
