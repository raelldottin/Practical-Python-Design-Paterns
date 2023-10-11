from urllib.parse import urlparse, urlunparse
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
import functools


def clean_url(base_url):
    # Parse the base_url to extract scheme and netloc (domain)
    parsed_url = urlparse(base_url)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc

    # Reconstruct the base_url with only scheme and domain
    return urlunparse((scheme, netloc, "", "", "", ""))


class SessionManager:
    _instances = {}

    def __new__(cls, base_url):
        clean_base_url = clean_url(base_url)
        retry = Retry(
            total=3,  # Total number of retries
            backoff_factor=1,  # Back-off factor (exponential back-off)
            # Retry for HTTP 429 and 503 status codes
            status_forcelist=[429, 503],
        )
        if clean_base_url not in cls._instances:
            cls._instances[clean_base_url] = super(SessionManager, cls).__new__(cls)
            cls._instances[clean_base_url].session = requests.Session()
            cls._instances[clean_base_url].session.mount(
                clean_base_url, HTTPAdapter(max_retries=retry)
            )
        return cls._instances[clean_base_url]

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.session.put(url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, **kwargs)


def rate_limited(requests_per_minute):
    interval = 60 / requests_per_minute

    def decorator(func):
        last_request_time = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_request_time
            current_time = time.time()
            time_since_last_request = current_time - last_request_time
            if time_since_last_request < interval:
                time_to_wait = interval - time_since_last_request
                time.sleep(time_to_wait)
            last_request_time = time.time()
            return func(*args, **kwargs)

        return wrapper

    return decorator
