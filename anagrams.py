s = str(input())
p = str(input())


def text_formation(string: str) -> str:             # formatting the given string
    string_formatted = (string.replace(" ", "")).lower()
    return string_formatted


def finding_anagrams(s: str, p: str) -> list:
    p = text_formation(p)
    s = text_formation(s)

    if len(p) > len(s):  # if the second string is bigger than the initial one
        return []

    pCount, sCount = {}, {}    # calculating the occurrences of len(p) in a row
    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = [0] if pCount == sCount else []  # if the first occurrences match return index of 0
    left_pointer = 0

    for right_pointer in range(len(p), len(s)):
        sCount[s[right_pointer]] = 1 + sCount.get(s[right_pointer], 0)
        sCount[s[left_pointer]] -= 1

        if sCount[s[left_pointer]] == 0:
            sCount.pop(s[left_pointer])

        left_pointer += 1

        if sCount == pCount:
            res.append(left_pointer)

    return res


print(finding_anagrams(s, p))    # output: [0, 6]
