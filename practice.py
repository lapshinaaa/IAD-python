from itertools import permutations
import re

s = str(input())
p = str(input())


def anagrams(first_string, second_string) -> list:
    formatted_first = text_formation(first_string)
    formatted_second = text_formation(second_string)
    indexes = []
    result = []

    permuts = [''.join(p) for p in permutations(formatted_second)]

    for permutation in permuts:
        if permutation in formatted_first:
            indexes.append([m.start() for m in re.finditer(permutation, formatted_first)])

    for list in indexes:
        for elem in list:
            if elem not in result:
                result.append(elem)

    result = sorted(result)

    return result


def text_formation(string: str) -> str:
    string_formatted = (string.replace(" ", "")).lower()
    return string_formatted


print(anagrams(s, p))
