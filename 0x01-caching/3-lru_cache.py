#!/usr/bin/env python3
"""LRU cache module"""

from base_caching import BaseCaching
import queue


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and prints caching system"""

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                remove_key = self.queue.pop(0)
                print(f"DISCARD: {remove_key}")
                self.cache_data.pop(remove_key)

            self.cache_data[key] = item

            # Create a new list excluding the specified key
            new_queue = []
            for k in self.queue:
                if k != key:
                    new_queue.append(k)

            # Update self.queue with the new list
            self.queue = new_queue

            # Add the key to the end of the queue
            self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # FInd the index of the key
        key_index = self.queue.index(key)

        # Remove the key from its current position and get its value
        remove_key = self.queue.pop(key_index)

        # Append the removed key to the end of the queue
        self.queue.append(remove_key)

        return self.cache_data.get(key)
