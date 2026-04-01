#a palindrome is a word or a sequence of characters which reads the same backward as forward such as madam or racecar.
#write a function that takes a word as input and determine whether it is a palindrome or not.
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]