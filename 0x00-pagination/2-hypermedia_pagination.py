#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that takes 2 ints as args and returns a tuple of size 2
    containing a start index and end index corresponding to the range of
    indexes to return in a list for those particuler pagination parameters
    """
    # Calculate the start index based on the page and page size
    start_index = (page - 1) * page_size

    # The end index based on start index and page size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Takes 2 ints  and returns the appropriate page of the data set"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()  # get the data from the csv file

        try:
            start_input, end_input = index_range(page, page_size)
            return data[start_input:end_input]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary containing key-value pairs"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # Use get_page to get current page
        data = self.get_page(page, page_size)

        start_index, end_index = index_range(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Get the next page
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        # Get the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
