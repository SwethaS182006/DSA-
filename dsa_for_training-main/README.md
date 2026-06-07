# DSA (Data Structures and Algorithms) Solutions

A modular Python library with implementations of common DSA concepts and problems, organized by topic for easy access and reuse.

## Project Structure

```
dsa/
├── __init__.py           # Package initialization - imports all modules
├── common.py             # Common imports and utilities
├── nodes.py              # Node classes (ListNode, TreeNode, GraphNode)
├── arrays.py             # Array manipulation and searching algorithms
└── README.md             # This file
```

## Usage

### Import Individual Functions
```python
from dsa.arrays import kadane_max_subarray_sum, sort_012

result = kadane_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)  # Output: 6
```

### Import Node Classes
```python
from dsa.nodes import ListNode, TreeNode, GraphNode

node = ListNode(val=5)
```

### Import Everything
```python
from dsa import *

# All functions and classes are now available
```

## Modules Overview

### `common.py`
Centralized imports and type hints used across the project:
- Collections: `Counter`, `OrderedDict`, `defaultdict`, `deque`
- Algorithms: `bisect_left`, `bisect_right`, `heapify`, `heappop`, etc.
- Type hints: `List`, `Dict`, `Set`, `Tuple`, `Optional`, etc.

### `nodes.py`
Node class definitions for data structure problems:
- **ListNode**: Linked list node with multiple pointer types (next, bottom, random)
- **TreeNode**: Binary tree node with left/right/next pointers
- **GraphNode**: Graph node with neighbor list

### `arrays.py`
Array manipulation algorithms (12 functions):
- **Finding elements**: `third_largest`, `majority_element`
- **Searching**: `pair_sum_sorted_rotated`, `find_missing_and_repeating`
- **Sorting**: `sort_012`, `remove_duplicates_sorted_array`
- **Manipulation**: `rotate_array_k`, `next_permutation`, `zig_zag_array`
- **Dynamic programming**: `kadane_max_subarray_sum`, `max_profit_one_transaction`
- **Greedy**: `stock_buy_sell_multiple`

## Function Reference

| Function | Time | Space | Description |
|----------|------|-------|-------------|
| `find_missing_and_repeating` | O(n) | O(1) | Find missing & repeating in 1..n |
| `max_profit_one_transaction` | O(n) | O(1) | Max profit from one buy-sell |
| `remove_duplicates_sorted_array` | O(n) | O(1) | Remove duplicates in-place |
| `zig_zag_array` | O(n) | O(1) | Arrange in zig-zag pattern |
| `third_largest` | O(n) | O(1) | Find 3rd largest distinct element |
| `pair_sum_sorted_rotated` | O(n) | O(1) | Find pair with sum in rotated array |
| `sort_012` | O(n) | O(1) | Sort 0s, 1s, 2s (Dutch flag) |
| `rotate_array_k` | O(n) | O(1) | Rotate array by k positions |
| `majority_element` | O(n) | O(1) | Find element > n/2 (Boyer-Moore) |
| `kadane_max_subarray_sum` | O(n) | O(1) | Maximum subarray sum |
| `stock_buy_sell_multiple` | O(n) | O(1) | Max profit with unlimited sales |
| `next_permutation` | O(n) | O(1) | Next lexicographic permutation |

## Example Usage

```python
from dsa import ListNode, TreeNode, kadane_max_subarray_sum, sort_012

# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Use array functions
arr = [3, 0, 1, 0, 2]
sort_012(arr)
print(arr)  # Output: [0, 0, 1, 2, 3]

# Maximum subarray sum
prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = kadane_max_subarray_sum(prices)
print(max_sum)  # Output: 6
```

## Notes

- Most functions modify arrays in-place (noted in docstrings)
- All functions avoid printing for easy testing and reuse
- Type hints included for better IDE support
- Each function includes time and space complexity in docstring
