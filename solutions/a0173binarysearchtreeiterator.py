# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/binary-search-tree-iterator/
#
# DESC:
# =====
# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
#
#
# Example:
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#
#
# Note:
# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# You may assume that next() call will always be valid,
# that is, there will be at least a next smallest number in the BST when next() is called.
################################################
from utils.tree.TreeNode import TreeNode


class BSTIterator:

  def __init__(self, root: TreeNode):
    self.stack = []
    self.__append(root)

  def next(self) -> int:
    node = self.stack.pop()
    if node.right:
      self.__append(node.right)
    return node.val

  def hasNext(self) -> bool:
    return len(self.stack) != 0

  def __append(self, node):
    while node:
      self.stack.append(node)
      node = node.left
