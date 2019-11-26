# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# DESC:
# =====
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
################################################
from typing import List

from utils.tree.TreeNode import TreeNode


class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []

    queue = [root]
    result = []
    reverse = False
    while queue:
      thisLevel = []
      length = len(queue)
      for _ in range(length):
        node = queue.pop()
        if node is not None:
          if reverse:
            thisLevel.insert(0, node.val)
          else:
            thisLevel.append(node.val)
          if node.left:
            queue.insert(0, node.left)
          if node.right:
            queue.insert(0, node.right)
      result.append(thisLevel)
      reverse = not reverse
    return result
