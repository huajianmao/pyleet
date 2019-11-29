# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
#
# DESC:
# =====
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
################################################
from utils.list.ListNode import ListNode
from utils.tree.TreeNode import TreeNode


class Solution:
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    nums = []
    while head:
      nums.append(head.val)
      head = head.next
    return self.helper(nums)

  def helper(self, nums):
    if len(nums) == 0:
      return None
    pivot = len(nums) // 2
    root = TreeNode(nums[pivot])
    root.left = self.helper(nums[:pivot])
    root.right = self.helper(nums[pivot + 1:])
    return root
