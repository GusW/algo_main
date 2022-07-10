from collections import Counter


def are_anagrams(subject: str, anagram: str) -> bool:
    return Counter(subject) == Counter(anagram)


def are_anagrams_2(subject: str, anagram: str) -> bool:
    if len(subject) != len(anagram):
        return False

    freq_map = {}
    for char in subject:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    for char in anagram:
        if not freq_map[char]:
            return False

        freq_map[char] -= 1

    return max(freq_map.values()) == 0


print(are_anagrams("restful", "fluster"))
print(are_anagrams_2("restful", "fluster"))


print(are_anagrams("restful", "flutter"))
print(are_anagrams_2("restful", "flutter"))
