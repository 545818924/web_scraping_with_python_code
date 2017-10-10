import re
from common import download


def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            print("link:%s" % link)
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(link)


def get_links(html):
    """Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # print("html:%s" % html)
    # list of all links from the webpage
    allhtml = webpage_regex.findall(html)
    print("allhtml:%s" % allhtml)
    return allhtml
    # search = webpage_regex.search(html)
    # if search:
    #     print("allhtml:%s" % search.group())
    # return search.group()
  

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(.*?)(index|view)')
    # link_crawler('http://example.webscraping.com', '/places/default/(index|view)')
