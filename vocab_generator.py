words = set()
lines = open("question-words.txt", "r", encoding="utf-8").readlines()
for line in lines:
    if ":" in line:
        continue
    if line.strip() == "":
        continue
    print(0)
    items = set(line.strip().split("\t"))
    words = words.union(items)
content = "\n".join(sorted(words))
open("list-pages.txt", "w", encoding="utf-8").write(content)
