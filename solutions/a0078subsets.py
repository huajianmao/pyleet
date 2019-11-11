# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/combinations/
#
# DESC:
# =====
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
################################################
from typing import List


class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
      return [[]]
    else:
      sub = self.subsets(nums[:-1])
      return sub + [it + [nums[-1]] for it in sub]
