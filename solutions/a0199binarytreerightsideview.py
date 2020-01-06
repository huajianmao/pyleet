# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/binary-tree-right-side-view/
#
# DESC:
# =====
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
#
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
################################################
from typing import List
from utils.tree.TreeNode import TreeNode


class Solution:
  def rightSideView(self, root: TreeNode) -> List[int]:
    result = []
    level = [root] if root is not None else []
    while level:
      result.append(level[-1].val)

      nextLevel = []
      for node in level:
        if node.left:
          nextLevel.append(node.left)
        if node.right:
          nextLevel.append(node.right)
      level = nextLevel

    return result
