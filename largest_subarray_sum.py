arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))

sum_index = {}
curr_sum = 0
max_len = 0
start = end = -1

for i in range(len(arr)):
    curr_sum += arr[i]

    if curr_sum == k:
        max_len = i + 1
        start = 0
        end = i

    if (curr_sum - k) in sum_index:
        length = i - sum_index[curr_sum - k]
        if length > max_len:
            max_len = length
            start = sum_index[curr_sum - k] + 1
            end = i

    if curr_sum not in sum_index:
        sum_index[curr_sum] = i

if max_len > 0:
    print("Length of largest subarray:", max_len)
    print("Subarray:", arr[start:end+1])
else:
    print("No subarray found")
