import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('../2of4brif.txt')

dict_file.append('a')
dict_file.append('I')

dict_file = sorted(dict_file)

ini_name = input("Enter a name: ")

def find_anagrams(name, word_list):
    """Read name & dictionary file & display all anagrams in name.add()

    Args:
        name (string): the name
        word_list ([type]): [description]
    """
    name_letter_map = Counter(name)
    anagrams=[]
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")

def process_choice(name):
    """Check user choice for validity, return choice & leftover letters."""
    while True:
        choice = input('\nMake a choice else Enter to start over or # to end: ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
    for letter in candidate:
        if letter in left_over_list:
            left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)

    name = ''.join(left_over_list) # makes display more readable
    return choice, name