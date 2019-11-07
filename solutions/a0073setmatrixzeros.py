# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/set-matrix-zeroes/
#
# DESC:
# =====
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
# Example 2:
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?"
#
################################################
from typing import List


class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    row = 1
    for i in range(n):
      if matrix[0][i] == 0:
        row = 0
        break
    col = 1
    for i in range(m):
      if matrix[i][0] == 0:
        col = 0
        break

    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0

    for i in range(1, m):
      if matrix[i][0] == 0:
        for j in range(1, n):
          matrix[i][j] = 0

    for j in range(1, n):
      if matrix[0][j] == 0:
        for i in range(1, m):
          matrix[i][j] = 0

    if row == 0:
      for i in range(n):
        matrix[0][i] = 0
    if col == 0:
      for i in range(m):
        matrix[i][0] = 0
