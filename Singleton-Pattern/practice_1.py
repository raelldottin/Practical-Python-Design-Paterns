import httplib2
import os
import re
import threading
import urllib
import urllib.request
import argparse
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class CrawlerSingleton(object):
    def __new__(cls):
        """creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, "instance"):
            cls.instance = super(CrawlerSingleton, cls).__new__(cls)
        return cls.instance


def navigate_site():
    """navigate the website using BFS algorithm, find links and
    arrange them for downloading images"""

    # singleton instance
    parser_crawlersingleton = CrawlerSingleton()

    # During the initial stage, url_queue has the main_url.
    # Upon parsing the main_url page, new links that belong to the
    # same website is added to the url_queue until
    # it equals to max _links.
    while parser_crawlersingleton.url_queue:
        # pop the url from the queue
        url = parser_crawlersingleton.url_queue.pop()

        # connect to the web page
        http = httplib2.Http()
        try:
            status, response = http.request(url)
        except Exception:
            continue

        # add the link to download the images
        parser_crawlersingleton.visited_url.add(url)
        print(url)

        # crawl the web page and fetch the links within
        # the main page
        bs = BeautifulSoup(response, "html.parser")

        for link in BeautifulSoup.findAll(bs, "a"):
            link_url = link.get("href")
            if not link_url:
                continue

            # parse the fetched link
            parsed = urlparse(link_url)

            # skip the link, if it leads to an external page
            if parsed.netloc and parsed.netloc != parsed_url.netloc:
                continue

            scheme = parsed_url.scheme
            netloc = parsed.netloc or parsed_url.netloc
            path = parsed.path

            # construct a full url
            link_url = scheme + "://" + netloc + path

            # skip, if the link is already added
            if link_url in parser_crawlersingleton.visited_url:
                continue

            # Add the new link fetched,
            # so that the while loop continues with next iteration.
            parser_crawlersingleton.url_queue = [
                link_url
            ] + parser_crawlersingleton.url_queue


class ParallelDownloader(threading.Thread):
    """Download the images parallelly"""

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting thread", self.name)
        # function to download the images
        download_images(self.name)
        print("Finished thread", self.name)


def download_images(thread_name):
    # singleton instance
    singleton = CrawlerSingleton()
    # visited_url has a set of URLs.
    # Here we will fetch each URL and
    # download the images in it.
    while singleton.visited_url:
        # pop the url to download the images
        url = singleton.visited_url.pop()

        http = httplib2.Http()
        print(thread_name, "Downloading images from", url)

        try:
            status, response = http.request(url)
        except Exception:
            continue

        # parse the web page to find all images
        bs = BeautifulSoup(response, "html.parser")

        # Find all <img> tags
        images = BeautifulSoup.findAll(bs, "img")

        for image in images:
            src = image.get("src")
            src = urljoin(url, src)

            basename = os.path.basename(src)
            print("basename:", basename)

            if basename != "":
                if src not in singleton.image_downloaded:
                    singleton.image_downloaded.add(src)
                    print("Downloading", src)
                    # Download the images to local system
                    urllib.request.urlretrieve(src, os.path.join("images", basename))
                    print(thread_name, "finished downloading images from", url)


def main():
    # singleton instance
    crwSingltn = CrawlerSingleton()

    # adding the url to the queue for parsing
    crwSingltn.url_queue = [main_url]

    # initializing a set to store all visited URLs
    # for downloading images.
    crwSingltn.visited_url = set()

    # initializing a set to store path of the downloaded images
    crwSingltn.image_downloaded = set()

    # invoking the method to crawl the website
    navigate_site()

    # create images directory if not exists
    if not os.path.exists("images"):
        os.makedirs("images")

    thread1 = ParallelDownloader(1, "Thread-1", 1)
    thread2 = ParallelDownloader(2, "Thread-2", 2)
    thread3 = ParallelDownloader(3, "Thread-3", 3)
    thread4 = ParallelDownloader(4, "Thread-4", 4)

    # Start new threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Url to crawl and download images")
    parser.add_argument(
        "--url",
        action="store",
        dest="main_url",
        default="https://www.geeksforgeeks.org/",
        help="Main URL for the web crawler",
        required=True,
    )
    args = parser.parse_args()

    main_url = args.main_url
    parsed_url = urlparse(main_url)
    main()
