#!/usr/bin/env python3
'''
This module provides functionality to cache HTTP requests
'''

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis client instance for caching and tracking
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    '''
    A decorator that caches the output of an HTTP GET request and tracks
    the number of times the URL has been accessed.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with caching and tracking functionality.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''
        Wrapper function that handles the caching of the HTTP GET request
        response and tracks the access count.

        Args:
            url (str): The URL to fetch the content from.

        Returns:
            str: The content of the URL, either from cache or a fresh request.
        '''
        # Increment the access count for the URL
        redis_store.incr(f'count:{url}')

        # Check if the result is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # Fetch the data, cache it, and return the result
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''
    Fetches the HTML content of the specified URL, caches the result,
    and tracks how many times the URL has been accessed.

    Args:
        url (str): The URL to retrieve content from.

    Returns:
        str: The HTML content of the URL.
    '''
    response = requests.get(url)
    return response.text
