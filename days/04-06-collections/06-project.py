#!python3
"""
Purpose of this script is to count the most common words in a file
"""

from collections import Counter, defaultdict

FILE = 'words.txt'


def get_words():
    words = defaultdict(list)
    with open(FILE, 'r') as f:
        if f.mode == "r":
            for line in f:
                for word in line.split():
                    words[word].append(word)

    return words


def main():
    get_words()

    words = get_words()

    cnt = Counter()

    for i, word in words.items():
        cnt[i] += len(word)

    print(cnt.most_common(20))


if __name__ == "__main__":
    main()


'''
Open file
read in all the words

'''