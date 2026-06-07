"""Node classes for linked list, tree, and graph data structures."""

from __future__ import annotations

from typing import List, Optional


class ListNode:
    """Node for linked list problems.
    
    Attributes:
        val: Node value
        data: Alias for val
        next: Next node in the list
        bottom: Bottom node for multi-level lists
        random: Random pointer for complex linked lists
    """
    
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
    """Node for binary tree problems.
    
    Attributes:
        val: Node value
        data: Alias for val
        left: Left child node
        right: Right child node
        next: Next node at same level (for level-order traversal)
    """
    
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
    """Node for graph problems.
    
    Attributes:
        val: Node value
        neighbors: List of neighboring nodes
    """
    
    def __init__(self, val: int = 0, neighbors: Optional[List["GraphNode"]] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


__all__ = ["ListNode", "TreeNode", "GraphNode"]
