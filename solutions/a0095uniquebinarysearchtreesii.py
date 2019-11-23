# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/unique-binary-search-trees-ii/
#
# DESC:
# =====
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
################################################
from typing import List

from utils.tree.TreeNode import TreeNode


class Solution:
  def generateTrees(self, n: int) -> List[TreeNode]:
    return self.generate(1, n) if n >= 1 else []

  def generate(self, start, end):
    if start > end:
      return [None]

    if start == end:
      return [TreeNode(start)]

    result = []
    for num in range(start, end + 1):
      lefts = self.generate(start, num - 1)
      rights = self.generate(num + 1, end)
      for left in lefts:
        for right in rights:
          root = TreeNode(num)
          root.left = left
          root.right = right
          result.append(root)
    return result
