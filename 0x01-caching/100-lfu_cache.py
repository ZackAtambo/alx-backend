#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
# Import OrderedDict from collections module
from collections import OrderedDict

# Import the BaseCaching class from base_caching module
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        # Call the parent class's initializer
        super().__init__()
        # Initialize cache_data as an OrderedDict
        self.cache_data = OrderedDict()
        # Initialize a list to keep track of keys and their frequencies
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        # Initialize variables to track positions and frequencies
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0

        # Iterate over the keys and their frequencies
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                # Update frequency and position for the most recently used key
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)

        # Reverse the max positions to determine the insertion position
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos

        # Update the position and frequency of the most recently used key
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

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
                # Remove the least frequently used item from the cache
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                # Print the discarded key
                print("DISCARD:", lfu_key)

            # Assign the item to the cache dictionary at key
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            # Insert the key with initial frequency 0
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            # If the key already exists, update its value
            self.cache_data[key] = item
            # Reorder items based on the updated frequency
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        # Check if key is not None and exists in the cache
        if key is not None and key in self.cache_data:
            # Reorder items based on the key's access
            self.__reorder_items(key)
        # Return the value associated with key in cache_data,
        # or None if key is not present
        return self.cache_data.get(key, None)