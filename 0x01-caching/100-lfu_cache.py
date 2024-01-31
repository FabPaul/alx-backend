#!/usr/bin/env python3
"""LFU cache module"""

from base_caching import BaseCaching
from collections import defaultdict
import time


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and prints caching system"""

    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)
        self.timestamp = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                min_freq = min(self.frequency.values())
                least_freq_keys = []
                for k, freq in self.frequency.items():
                    if freq == min_freq:
                        least_freq_keys.append(k)

                # if more than 1 item with least freq use LRU to find the least
                if len(least_freq_keys) > 1:
                    lru_key = min(least_freq_keys,
                                  key=lambda k: self.timestamp[k])
                else:
                    lru_key = least_freq_keys[0]

                print(f"DISCARD: {lru_key}")
                self.cache_data.pop(lru_key)
                self.frequency.pop(lru_key)
                self.timestamp.pop(lru_key)

            self.cache_data[key] = item

            self.frequency[key] += 1
            self.timestamp[key] = time.time()

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.timestamp[key] = time.time()
        return self.cache_data[key]
