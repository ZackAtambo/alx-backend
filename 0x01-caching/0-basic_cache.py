#!/usr/bin/env python3
"""Basic caching module.
"""
# Import the BaseCaching class from base_caching module
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """

    def put(self, key, item):
        """Adds an item in the cache.
        """
        # Check if key or item is None
        if key is None or item is None:
            return  # If either key or item is None, do nothing

        # Assign the item to the cache dictionary at key
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        # Return the value associated with key in cache_data,
        # or None if key is not present
        return self.cache_data.get(key, None)