# this is a test
# it is only a test

import itertools


rack = input('Enter 9 letters here:')
candidates= set()

def compute_score(word):
    return len(word)

for i in range(1, len(rack) +1):
    for combination in itertools.combinations(rack, i):
        candidates|= {''.join(perm) for perm in itertools.permutations(combination)}

with open('dictionary.txt') as f:
    dictionary = {word.strip().lower() for word in f}


correct_words = dictionary & candidates
correct_words = [(word, compute_score(word)) for word in correct_words]
correct_words.sort(key=lambda word: word[1], reverse=True)

for word, score in correct_words:
    if score > 5:
        print(str(score) + ' - ' + word)
