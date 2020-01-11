# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/minimum-size-subarray-sum/
#
# DESC:
# =====
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
#
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Follow up:
# If you have figured out the O(n) solution,
# try coding another solution of which the time complexity is O(n log n).
################################################
from typing import List


class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    start = 0
    sum = 0
    minLen = len(nums) + 1

    for i in range(len(nums)):
      sum += nums[i]
      while sum - nums[start] >= s:
        sum -= nums[start]
        start += 1
      if sum >= s:
        minLen = min(minLen, i - start + 1)

    return minLen if minLen <= len(nums) else 0
