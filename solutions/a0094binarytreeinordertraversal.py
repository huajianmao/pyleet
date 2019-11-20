# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# DESC:
# =====
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
################################################
from typing import List
from utils.tree.TreeNode import TreeNode


class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    result = []
    stack = []
    while True:
      while root:
        stack.append(root)
        root = root.left
      if not stack:
        return result
      node = stack.pop()
      result.append(node.val)
      root = node.right
