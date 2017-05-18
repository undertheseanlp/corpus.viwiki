lines = open("page-queue.txt", "r").read().split("\n")
print(len(lines))
print(lines[:10])
print(len(list(set(lines))))
pages = list(set(lines))
print(lines[:10])

crawled_pages = open("crawled-pages.txt", "r").read().split("\n")
print(len(crawled_pages))
print(len(list(set(crawled_pages))))

pages = pages + crawled_pages
print(len(pages))
print(len(list(set(pages))))