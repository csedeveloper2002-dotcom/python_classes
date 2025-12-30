arr = list(map(int, input("Enter array elements: ").split()))

product = 1
for i in arr:
    product *= i

print("Product of array elements:", product)
