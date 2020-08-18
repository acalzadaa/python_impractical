"""Project #2 Find palindromes in dictionary file"""
import load_dictionary

word_list = load_dictionary.load("lista.txt")
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"I found {len(pali_list)} palindrome words")