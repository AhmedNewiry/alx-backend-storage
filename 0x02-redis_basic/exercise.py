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
            data: The data to store, which can be of type str, bytes, int, or float.

        Returns:
            The randomly generated key as a string.
        """
        key = str(uuid.uuid4())  # Generate a random UUID as the key
        self._redis.set(key, data)  # Store the data in Redis using the key
        return key  # Return the generated key
