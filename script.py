import wikipedia

cached_pages = []


def crawl_page(title):
    try:
        p = wikipedia.page(title)
        original_title = p.title.lower()
        is_matched = "[Y]" if title == original_title else "[N]"
        print("%s %s -> %s" % (is_matched, title, original_title))
        filename = "viwiki/%s.txt" % original_title
        open(filename, "w", encoding="utf-8").write(p.content)
    except wikipedia.DisambiguationError as e:
        titles = [title.lower() for title in e.options]
        for title in titles:
            if title not in cached_pages:
                cached_pages.append(title)
                crawl_page(title)


if __name__ == '__main__':
    wikipedia.set_lang("vi")
    lines = open("list-pages.txt", "r", encoding="utf-8").readlines()
    titles = [l.strip() for l in lines]
    [crawl_page(title) for title in titles]
