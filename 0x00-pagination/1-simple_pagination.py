#!/usr/bin/env python3

import csv
from typing import List, Tuple


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a list of baby names for a given page and page size."""
        assert isinstance(page, int) and page > 0, "must be + int."
        assert isinstance(page_size, int) and page_size > 0, "must be a + int."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and
        end index for the given page and page size.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
