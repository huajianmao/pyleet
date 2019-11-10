# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/combinations/
#
# DESC:
# =====
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
################################################
from typing import List


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    if n <= k:
      return [[i + 1 for i in range(n)]]
    if k == 1:
      return [[i + 1] for i in range(n)]

    result = self.combine(n - 1, k - 1)
    for it in result:
      it.append(n)

    return result + self.combine(n - 1, k)
