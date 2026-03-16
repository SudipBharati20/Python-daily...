word = input("Enter a word: ")
count = 0

for ch in word:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels =", count)