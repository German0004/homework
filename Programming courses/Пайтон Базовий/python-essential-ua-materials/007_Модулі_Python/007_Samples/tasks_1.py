import collections
import itertools
import random


def get_max_count_word(counts_dict):
    max_count = 0
    max_count_word = None
    for word, count in counts_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word
    return max_count_word


def get_max_count_word_combinations(words, max_count_word):
    combinations = itertools.combinations(words, 2)
    max_count_word_combinations = [comb for comb in combinations if max_count_word in comb]
    return max_count_word_combinations


def process(text):
    words = text.split(' ')
    counts = collections.Counter(words)
    max_count_word = get_max_count_word(counts)
    max_count_word_combinations = get_max_count_word_combinations(words, max_count_word)
    random_combination = max_count_word_combinations[random.randint(0, len(max_count_word_combinations)-1)]
    return random_combination


text = "blue cat is parked right behind the blue building with blue walls and red door"
rc = process(text)
print(rc)
