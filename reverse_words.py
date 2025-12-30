s = input("Enter a sentence: ")

words = s.split()
rev_words = words[::-1]

result = " ".join(rev_words)
print("Reversed words:", result)
