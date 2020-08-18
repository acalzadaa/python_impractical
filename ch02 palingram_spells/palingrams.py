"""Project #3 Find palingrams in dictionary file: Nurses Run => nuR sesruN"""
import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")


def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

for element in palingrams_sorted:
    print(element)
