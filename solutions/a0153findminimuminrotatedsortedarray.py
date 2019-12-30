# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/maximum-product-subarray/
#
# DESC:
# =====
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.
#
# Example 1:
# Input: [3,4,5,1,2]
# Output: 1
#
# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0
################################################
from typing import List


class Solution:
  def findMin(self, nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1

    if len(nums) == 1:
      return nums[0]
    elif nums[start] < nums[end]:
      return nums[start]
    else:
      middle = (start + end) // 2
      if nums[middle] >= nums[start]:
        return self.findMin(nums[middle + 1: end + 1])
      else:
        return self.findMin(nums[start: middle + 1])
