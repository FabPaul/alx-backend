#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple
import csv
import math
from typing import List


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
