#!/usr/bin/env python3
"""
Redis Cache Module
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize the Cache instance with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis using a randomly generated key.

        Args:
            data: The data to store, which can be of
            type str, bytes, int, or float.

        Returns:
            The randomly generated key as a string.
        """
        key = str(uuid.uuid4())  # Generate a random UUID as the key
        self._redis.set(key, data)  # Store the data in Redis using the key
        return key  # Return the generated key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it
        back to the desired format using fn.

        :param key: The key to retrieve data from Redis.
        :param fn: An optional callable that will be used to
        convert the data back to the desired format.
        :return: The retrieved data, converted by fn if provided,
        or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a string.

        :param key: The key to retrieve data from Redis.
        :return: The data as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        :param key: The key to retrieve data from Redis.
        :return: The data as an integer,
        or None if the key does not exist.
        """
        return self.get(key, fn=int)
