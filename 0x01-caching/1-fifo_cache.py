#!/usr/bin/env python3
"""FIFO cache module"""

from base_caching import BaseCaching
import queue


class FIFOCache(BaseCaching):
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
                    and key not in self.cache_data.keys():
                remove_key = self.queue.pop(0)
                self.cache_data.pop(remove_key)
                print(f"DISCARD: {remove_key}")

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
