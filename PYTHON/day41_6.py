#write a function that takes a word with numeric values as inpye an d counts the number of numeric value and consonents present in the word
def count_numeric_consonants(word):
    numeric_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isdigit():
            numeric_count += 1
        elif char.isalpha() and char.lower() not in "aeiou":
            consonant_count += 1
            
    return numeric_count, consonant_count