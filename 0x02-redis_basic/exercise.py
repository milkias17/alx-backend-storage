#!/usr/bin/env python3
"""Writing strings to Redis"""
import functools
from typing import Callable, Union
from uuid import uuid4

import redis


def count_calls(method: Callable) -> Callable:
    """Counts how many times a function has been called."""
    @functools.wraps(method)
    def increment(self, *args, **kwargs):
        """increments the count in redis store"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return increment


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function"""
    @functools.wraps(method)
    def store_history(self, *args, **kwargs):
        """implementation"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output

    return store_history


class Cache:
    """Cache system implementation using redis"""

    def __init__(self) -> None:
        """Initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key, store the input data in Redis using the
        random key and return the key.
        """
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Callable = None):
        """convert data back to desired format"""
        val = self._redis.get(key)
        if val is None or fn is None:
            return val

        return fn(val)

    def get_str(self, key: str):
        """Returns value as string"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """Returns value as integer"""
        return self.get(key, lambda x: int(x))
