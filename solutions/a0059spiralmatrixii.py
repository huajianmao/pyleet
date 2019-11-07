# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/spiral-matrix/
#
# DESC:
# =====
# Given a positive integer n,
# generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#
################################################
from typing import List


class Solution:

  def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for turn in range((n + 1) // 2 + 1):
      for g in range(4):
        ox, ix, signX = g // 2, g % 2, 1
        if g >= 2:
          signX = -1

        oy, iy, signY = 0, 1 - g % 2, 1
        if g == 1 or g == 2:
          oy, signY = 1, -1

        for i in range(n - 2 * turn - 1):
          x = signX * (turn + ox * 1 + ix * i)
          y = signY * (turn + oy * 1 + iy * i)
          matrix[x][y] = num
          num += 1

    if n % 2 == 1:
      matrix[n // 2][n // 2] = num

    return matrix
