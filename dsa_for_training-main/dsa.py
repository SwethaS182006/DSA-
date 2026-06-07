"""Python solutions for the DSA roadmap.

The module is organized by topic and keeps each problem as a standalone
function or class. Most functions return the computed answer and avoid
printing, which makes them easy to test and reuse on coding platforms.
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import Counter, OrderedDict, defaultdict, deque
from functools import cmp_to_key, lru_cache
from heapq import heapify, heappop, heappush, heappushpop, nlargest
from math import gcd, inf
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None,
        bottom: Optional["ListNode"] = None,
        random: Optional["ListNode"] = None,
    ) -> None:
        self.val = val
        self.data = val
        self.next = next
        self.bottom = bottom
        self.random = random


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.data = val
        self.left = left
        self.right = right
        self.next: Optional["TreeNode"] = None


class GraphNode:
    def __init__(self, val: int = 0, neighbors: Optional[List["GraphNode"]] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ---------------------------------------------------------------------------
# Arrays
# ---------------------------------------------------------------------------


def find_missing_and_repeating(arr: List[int]) -> Tuple[int, int]:
    """Return (missing, repeating) for an array containing 1..n with one duplicate."""
    n = len(arr)
    diff = sum(arr) - n * (n + 1) // 2
    sq_diff = sum(x * x for x in arr) - n * (n + 1) * (2 * n + 1) // 6
    total = sq_diff // diff
    repeating = (diff + total) // 2
    missing = total - repeating
    return missing, repeating


def max_profit_one_transaction(prices: List[int]) -> int:
    best = 0
    low = inf
    for price in prices:
        low = min(low, price)
        best = max(best, price - low)
    return best


def remove_duplicates_sorted_array(arr: List[int]) -> int:
    if not arr:
        return 0
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    return write


def zig_zag_array(arr: List[int]) -> List[int]:
    less = True
    for i in range(len(arr) - 1):
        if less and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not less and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        less = not less
    return arr


def third_largest(arr: List[int]) -> Optional[int]:
    first = second = third = -inf
    for x in arr:
        if x in (first, second, third):
            continue
        if x > first:
            first, second, third = x, first, second
        elif x > second:
            second, third = x, second
        elif x > third:
            third = x
    return None if third == -inf else third


def pair_sum_sorted_rotated(arr: List[int], target: int) -> bool:
    n = len(arr)
    if n < 2:
        return False
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break
    left = (pivot + 1) % n
    right = pivot
    while left != right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        if total < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    return False


def sort_012(arr: List[int]) -> List[int]:
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


def rotate_array_k(arr: List[int], k: int, direction: str = "right") -> List[int]:
    n = len(arr)
    if n == 0:
        return arr
    k %= n
    if direction == "left":
        k = n - k
    arr[:] = arr[-k:] + arr[:-k] if k else arr
    return arr


def majority_element(arr: List[int]) -> Optional[int]:
    candidate = None
    count = 0
    for x in arr:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    if candidate is not None and arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


def kadane_max_subarray_sum(arr: List[int]) -> int:
    if not arr:
        return 0
    best = current = arr[0]
    for x in arr[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best


def stock_buy_sell_multiple(prices: List[int]) -> int:
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


def next_permutation(arr: List[int]) -> List[int]:
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1