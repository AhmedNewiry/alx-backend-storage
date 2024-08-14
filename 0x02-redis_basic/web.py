#!/usr/bin/env python3
"""
This module defines a function to fetch the HTML content of a URL w
"""

import requests
import redis
from typing import Callable


# Initialize Redis connection
redis_store = redis.Redis()


def cache_page(fn: Callable) -> Callable:
    """
    Decorator that caches the page content and tracks the access count.

    Args:
        fn (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function.
    """
    def wrapper(url: str) -> str:
        # Track access count
        redis_store.incr(f"count:{url}")

        # Check if cached content exists
        cached_page = redis_store.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')

        # Fetch the page using the decorated function
        html_content = fn(url)

        # Cache the content with an expiration time of 10 seconds
        redis_store.setex(f"cached:{url}", 10, html_content)

        return html_content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
