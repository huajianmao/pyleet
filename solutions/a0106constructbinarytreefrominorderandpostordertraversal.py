# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# DESC:
# =====
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if postorder is None or len(postorder) != len(inorder) or len(postorder) == 0:
      return None

    i = 0
    while i < len(inorder) and inorder[i] != postorder[-1]:
      i += 1
    root = TreeNode(postorder[-1])
    root.left = self.buildTree(inorder[0:i], postorder[0:i])
    root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
    return root
