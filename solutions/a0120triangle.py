# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/triangle/
#
# DESC:
# =====
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.
#
################################################
from typing import List


class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    for i in range(1, len(triangle)):
      triangle[i][0] += triangle[i - 1][0]
      triangle[i][-1] += triangle[i - 1][-1]
      for j in range(1, len(triangle[i]) - 1):
        triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
    return min(triangle[-1])
