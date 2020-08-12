"""Find semordnilap in dictionary file"""
import load_dictionary

word_list = load_dictionary.load("lista.txt")
semordnilap_list = []

for word in word_list:
    if len(word) > 1 and (word[::-1] in word_list) and word == word[::-1] :
        semordnilap_list.append(word)

print(f"I found {len(semordnilap_list)} semordnilap words")