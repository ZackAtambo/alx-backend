#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
# Import OrderedDict from collections module
from collections import OrderedDict

# Import the BaseCaching class from base_caching module
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        # Call the parent class's initializer
        super().__init__()
        # Initialize cache_data as an OrderedDict
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        # Check if key or item is None
        if key is None or item is None:
            # Do nothing if either key or item is None
            return
        # Assign the item to the cache dictionary at key
        self.cache_data[key] = item

        # Check if cache exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first item from the cache
            first_key, _ = self.cache_data.popitem(False)
            # Print the discarded key
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        # Return the value associated with key in cache_data,
        # or None if key is not present
        return self.cache_data.get(key, None)