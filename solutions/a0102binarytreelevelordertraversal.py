# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# DESC:
# =====
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
################################################
from typing import List

from utils.tree.TreeNode import TreeNode


class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []

    queue = [root]
    result = []
    while queue:
      thisLevel = []
      length = len(queue)
      for _ in range(length):
        node = queue.pop()
        if node is not None:
          thisLevel.append(node.val)
          if node.left:
            queue.insert(0, node.left)
          if node.right:
            queue.insert(0, node.right)
      result.append(thisLevel)
    return result
