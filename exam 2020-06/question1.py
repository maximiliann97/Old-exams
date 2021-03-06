from collections import defaultdict

fn = 'A_Journal_of_the_Plauge_Year.txt'

def filter_file(word):
    return word.strip('.,!?;:&)([]').lower()


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
    occurences_list = sorted(occurences.items(), key=lambda x:x[1])[::-1]
    sort_occurences = dict(occurences_list)
    return sort_occurences, N_words

def print_table(words, total_words):
    header = 'word | occurences | probability'
    line = "-"*len(header)
    print(header)
    print(line)
    for word, occurence in words.items():
        prob = (words[word]/total_words)*100
        print(f" {word:4s} | {occurence:10d} | {prob:10.1f}%")











occurences, N_words = read_file(fn)
print_table(occurences, N_words)
