from itertools import permutations

def find_permutations(name):
    """find permutations

    Args:
        name (String): the word that will be permuted into different words

    Returns:
        [Array]: All the words formed with the permutations of the input value
    """
    perms = [''.join(i) for i in permutations(name)]
    print(len(perms))
    return perms

find_permutations("voldemort")