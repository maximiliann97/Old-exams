from collections import Counter
from collections import defaultdict

fn = 'A_Journal_of_the_Plauge_Year.txt'

def filter_file(word):
    return word.strip('.,!?;:)([]').lower()


def read_file(filename):
    N_words = 0
    occurences = defaultdict(str)
    with open(filename, encoding="utf8", mode='r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = filter_file(word)
                N_words += 1
                if word not in occurences:
                    occurences[word] = 1
                else:
                    occurences[word] += 1
    print('Total amount of words:', N_words)
    print('Number of unique words:', len(occurences))
    occurences.items().sort()
    return occurences

def print_table(words):
    prob = []
    for word, occurences in words.items():
        prob.append(words[word]/len(words))





occurences = read_file(fn)
print(occurences)
print_table(occurences)
