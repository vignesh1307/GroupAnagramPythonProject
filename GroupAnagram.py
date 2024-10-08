from collections import defaultdict


def group_anagrams(words):

    anagrams = defaultdict(list)

    for word in words:
        sorted_word = tuple(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
    print(anagrams)




# Example usage


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = group_anagrams(words)
print(grouped_anagrams)
