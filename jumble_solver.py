#!/usr/bin/env python3
"""A jumble solver.
usage: python3 jumble_solver.py [word_list_path] [word_key]
"""
import sys
import collections
from typing import Dict, List

# There are n!/k!(n-k)! combinations where n is the string length
# O(n^k)
def string_combinations(string: str, k: int) -> List[str]:
    """An alphabetic order combination generator. Returns all k sized combinations."""
    combinations, str_len = [], len(string)

    def backtrack(start: int, comb: str):  # recursive
        if len(comb) == k:  # base case
            combinations.append(comb)
            return
        for i in range(start, str_len):
            comb += string[i]
            backtrack(i + 1, comb)
            comb = comb[:-1]
    backtrack(0, "")
    return combinations


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SyntaxError(
            "usage: python3 jumble_solver.py [word_list_path] [word_key]")

    _, word_list_path, jumble = sys.argv

    def anagram_key(jumble: str):
        return "".join(sorted(jumble.strip("\n")))

    anagram_dict: Dict[str, List[str]] = collections.defaultdict(list)

    # n = len(word_list), m = len(word)
    # O(n * mlogm), mlogm is sort speed
    with open(word_list_path, 'r') as f:
        for word in f:
            KEY = anagram_key(word)
            anagram_dict[KEY].append(word.strip("\n"))
    # O(k n^k)
    all_jumbles: List[str] = []
    for str_size in range(len(jumble)):
        all_jumbles += string_combinations(jumble, str_size + 1)

    # m = length of all_jumbles, n = word_list
    # O(m*n)
    for sub_jumble in reversed(all_jumbles):
        for word in anagram_dict[anagram_key(sub_jumble)]:
            if word != jumble:
                print(word)
