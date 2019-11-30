# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
# DESC:
# =====
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
################################################
from utils.list.ListNode import ListNode
from utils.tree.TreeNode import TreeNode


class Solution:
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    tail = TreeNode(0)
    queue = [root] if root else []
    while queue:
      node = queue.pop()
      if node.right:
        queue.append(node.right)
      if node.left:
        queue.append(node.left)
      node.left = None
      tail.right = node
      tail = tail.right
