# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/maximum-product-subarray/
#
# DESC:
# =====
# Given an integer array nums,
# find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
################################################
from typing import List


class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    result = nums[0]
    iMax = result
    iMin = result
    for i in range(1, len(nums)):
      if nums[i] < 0:
        iMax, iMin = iMin, iMax
      iMax = max(nums[i], iMax * nums[i])
      iMin = min(nums[i], iMin * nums[i])
      result = max(result, iMax)

    return result
