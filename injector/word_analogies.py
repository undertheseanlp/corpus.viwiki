import re
def load_word_analogies():
    words = []
    lines = open("word-analogies.txt", "r", encoding="utf-8").read().split("\n")
    for line in lines:
        matched = re.match("\[✓?\] (\w+), (\w+), (\w+) => (.*) \(.*\), ((.*),)+", lines[4], re.UNICODE)
        if matched:
            groups = matched.groups()
            words.extend(groups[:3])
            words.extend(groups[5].split(", "))
            print(0)
    return words

load_word_analogies()