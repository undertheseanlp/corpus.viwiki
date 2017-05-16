from os import listdir
import codecs
import wikipedia

from injector.word_analogies import load_word_analogies

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
            extend_pages(out_pages)
        except:
            pass
        filename = "viwiki/%s.txt" % transform_page_name(original_title)
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
    except Exception as e:
        print(e)
    crawled_pages.add(title)


def load_queue():
    return ""


def transform_page_name(page):
    page = page.replace("/", "")
    return page


def crawl(recrawl=False, num_pages=20):
    for i in range(num_pages):
        page = page_queue.pop(0)
        print("\n%d / %d" % (i, num_pages))
        crawl_page(page, recrawl=recrawl)

def extend_pages(pages):
    global page_queue
    global crawled_pages
    pages = [page for page in pages if page not in list(crawled_pages) + page_queue]
    page_queue = page_queue + pages

def inject_pages(pages):
    global page_queue
    global crawled_pages
    pages = [page for page in pages if page not in list(crawled_pages) + page_queue]
    page_queue = pages + page_queue


def load_context():
    global crawled_pages
    crawled_pages = set(open("crawled-pages.txt", "r", encoding="utf-8").read().split("\n"))
    global page_queue
    page_queue = open("page-queue.txt", "r", encoding="utf-8").read().split("\n")
    pages_from_word_analogies_task = load_word_analogies()
    # inject_pages(pages_from_word_analogies_task)


def save_context():
    content = "\n".join(crawled_pages)
    open("crawled-pages.txt", "w", encoding="utf-8").write(content)
    content = "\n".join(page_queue)
    open("page-queue.txt", "w", encoding="utf-8").write(content)


if __name__ == '__main__':
    wikipedia.set_lang("vi")
    load_context()
    crawl(recrawl=False, num_pages=200)
    save_context()
