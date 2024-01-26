#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple


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
