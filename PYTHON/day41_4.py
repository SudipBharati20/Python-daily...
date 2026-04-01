#An anagram is a word that contan=ins same characters in different order such as listen and silent. or schoolmaster and theclassroom.
#write a function that takes two words as input and determine whether they are anagrams or not.
def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)


print(are_anagrams("listen", "silent"))           # True
print(are_anagrams("schoolmaster", "the classroom"))  # True
print(are_anagrams("hello", "world"))            # False
