# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# DESC:
# =====
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
################################################
from typing import List

from utils.tree.TreeNode import TreeNode


class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if preorder is None or len(preorder) != len(inorder) or len(preorder) == 0:
      return None

    i = 0
    while i < len(inorder) and inorder[i] != preorder[0]:
      i += 1
    root = TreeNode(preorder[0])
    root.left = self.buildTree(preorder[1:i + 1], inorder[0:i])
    root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
    return root
