import load_dictionary


# two words must be the same length
# the ordered chars must coincide
def find_anagrams():

    word_list = load_dictionary.load('2of4brif.txt')
    anagram_list = []

    name = 'dog'
    name = name.lower()
    name_sorted = sorted(name)

    for word in word_list:
        word = word.lower()
        if word != name and sorted(word) == name_sorted:
            anagram_list.append(word)

    if len(anagram_list) == 0:
        print("None anagrams found")
    else:
        print(f"Anagrams: {anagram_list}")
