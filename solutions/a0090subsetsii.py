# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/subsets-ii/
#
# DESC:
# =====
# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
################################################
from typing import List


class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result = [()]
    nums.sort()
    for i in range(len(nums)):
      result += [x + (nums[i],) for x in result]
      result = list(set(result))
    return [list(tupple) for tupple in result]
