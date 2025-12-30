arr = list(map(int, input("Enter array elements: ").split()))

count = 0
candidate = None

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

if arr.count(candidate) > len(arr) // 2:
    print("Majority element:", candidate)
else:
    print("No majority element")
