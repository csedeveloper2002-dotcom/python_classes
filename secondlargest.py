s=[1,23,3,4,53]
Max=float("-inf")
max1=float("-inf")
for i in range(len(s)):
    if Max<s[i]:
        Max=s[i]
for i in range(len(s)):
    if max1<s[i] and Max!=s[i]:
        max1=s[i]
print(max1)        
