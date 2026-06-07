"""DSA (Data Structures and Algorithms) Solutions.

Organized by concept into separate modules for better organization and reusability.
"""

from .arrays import (
    find_missing_and_repeating,
    kadane_max_subarray_sum,
    majority_element,
    max_profit_one_transaction,
    next_permutation,
    pair_sum_sorted_rotated,
    remove_duplicates_sorted_array,
    rotate_array_k,
    sort_012,
    stock_buy_sell_multiple,
    third_largest,
    zig_zag_array,
)
from .common import *
from .nodes import GraphNode, ListNode, TreeNode

__all__ = [
    # Nodes
    "ListNode",
    "TreeNode",
    "GraphNode",
    # Arrays
    "find_missing_and_repeating",
    "max_profit_one_transaction",
    "remove_duplicates_sorted_array",
    "zig_zag_array",
    "third_largest",
    "pair_sum_sorted_rotated",
    "sort_012",
    "rotate_array_k",
    "majority_element",
    "kadane_max_subarray_sum",
    "stock_buy_sell_multiple",
    "next_permutation",
]
