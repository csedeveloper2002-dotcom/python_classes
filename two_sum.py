arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum: "))

seen = {}

for i, num in enumerate(arr):
    diff = target - num
    if diff in seen:
        print("Indices:", seen[diff], i)
        print("Values:", diff, num)
        break
    seen[num] = i
else:
    print("No two sum solution")
