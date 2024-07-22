#!/usr/bin/env python3

"""
Module for calculating pagination index ranges.

This module provides a function to calculate
the start and end indexes for a list based on
pagination parameters. The pagination parameters
include the page number and the number of items
per page. Page numbers are 1-indexed.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end
        index for the given page and page size.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
