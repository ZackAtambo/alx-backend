#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
# Import OrderedDict from collections module
from collections import OrderedDict

# Import the BaseCaching class from base_caching module
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
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

        # Check if the key is not already in the cache
        if key not in self.cache_data:
            # Check if adding the new item exceeds MAX_ITEMS
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the last item from the cache
                last_key, _ = self.cache_data.popitem(True)
                # Print the discarded key
                print("DISCARD:", last_key)

        # Assign the item to the cache dictionary at key
        self.cache_data[key] = item
        # Move the key to the end of the order
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        # Return the value associated with key in cache_data,
        # or None if key is not present
        return self.cache_data.get(key, None)