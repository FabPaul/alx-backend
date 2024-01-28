#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dict with key-value pairs"""
        assert isinstance(index, int)
        assert 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        total_rows = len(dataset)

        # calculate start and end index for the requested page
        if index is not None:
            start_index = index
        else:
            start_index = 0
        end_index = start_index + page_size

        # Fix the end_indes if it exceeds the total number of rows
        end_index = min(end_index, total_rows)

        if end_index < total_rows:
            next_index = end_index
        else:
            next_index = None

        # Get the data for the current page
        data = []
        for value in range(start_index, end_index):
            if self.indexed_dataset().get(value):
                data.append(self.indexed_dataset()[value])
            else:
                value += 1
                next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
