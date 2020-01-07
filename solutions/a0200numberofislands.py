# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/number-of-islands/
#
# DESC:
# =====
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
################################################
from typing import List


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0

    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          self.dfs(grid, i, j)
          count += 1

    return count

  def dfs(self, grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
      return

    grid[i][j] = '#'
    self.dfs(grid, i + 1, j)
    self.dfs(grid, i - 1, j)
    self.dfs(grid, i, j + 1)
    self.dfs(grid, i, j - 1)
