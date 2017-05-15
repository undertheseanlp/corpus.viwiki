from os import listdir
import codecs
import wikipedia

crawled_pages = set()
page_queue = []


def crawl_page(title, recrawl=False):
    if title in crawled_pages and not recrawl:
        return
    try:
        p = wikipedia.page(title)
        original_title = p.title.lower()
        is_matched = "[Y]" if title == original_title else "[N]"
        content = "%s %s -> %s" % (is_matched, title, original_title)
        content = content.encode().decode("utf-8")
        print(content)
        try:
            out_pages = p.links
            page_queue.extend(out_pages)
        except:
            pass
        filename = "viwiki/%s.txt" % original_title
        open(filename, "w", encoding="utf-8").write(p.content)
        crawled_pages.add(original_title)
    except wikipedia.DisambiguationError as e:
        titles = [title.lower() for title in e.options]
        for title in titles:
            if title not in crawled_pages:
                crawled_pages.add(title)
                crawl_page(title)
    except wikipedia.PageError as e:
        pass
    crawled_pages.add(title)


def load_queue():
    return ""


def crawl(recrawl=False, num_pages=20):
    for i in range(num_pages):
        page = page_queue.pop(0)
        print("\n%d / %d" % (i, num_pages))
        crawl_page(page, recrawl=recrawl)


def load_context():
    global crawled_pages
    crawled_pages = set(open("crawled-pages.txt", "r", encoding="utf-8").read().split("\n"))
    global page_queue
    page_queue = open("page-queue.txt", "r", encoding="utf-8").read().split("\n")


def save_context():
    content = "\n".join(crawled_pages)
    open("crawled-pages.txt", "w", encoding="utf-8").write(content)
    content = "\n".join(page_queue)
    open("page-queue.txt", "w", encoding="utf-8").write(content)


if __name__ == '__main__':
    wikipedia.set_lang("vi")
    load_context()
    crawl(recrawl=True, num_pages=2)
    save_context()
