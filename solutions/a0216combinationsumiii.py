# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/combination-sum-iii/
#
# DESC:
# =====
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
#
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
################################################
from typing import List


class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    return self.helper(k, n, 9)

  def helper(self, k, n, maxNum):
    if k > maxNum or ((maxNum + (maxNum - k + 1)) * k // 2) < n or (1 + k) * k // 2 > n:
      return []

    if k == 1 and n <= maxNum:
      return [[n]]

    result = []
    for _max in range(min(maxNum, n), k - 1, -1):
      thisResult = self.helper(k - 1, n - _max, _max - 1)
      for arr in thisResult:
        arr.append(_max)
      result += thisResult

    return result
