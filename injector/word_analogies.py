import re
from os.path import dirname, join

from os import rename


def load_word_analogies():
    words = []
    current_dir = dirname(__file__)
    file = join(current_dir, "word-analogies.txt")
    try:
        lines = open(file, "r", encoding="utf-8").read().split("\n")
        for line in lines:
            matched = re.match("\[.*\] (.*), (.*), (.*) => (.*) \(.*\), ((.*),)+", line)
            if matched:
                groups = matched.groups()
                words.extend(groups[:3])
                words.extend(groups[5].split(", "))
        words = list(set(words))
        rename(file, join(current_dir, "word-analogies-cached.txt"))
        return words
    except:
        return []

# load_word_analogies()
