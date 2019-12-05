# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/surrounded-regions/
#
# DESC:
# =====
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
# X X X X
# X O O X
# X X O X
# X O X X
#
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
#
# Explanation:
# Surrounded regions shouldn’t be on the border,
# which means that any 'O' on the border of the board are not flipped to 'X'.
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.
#
################################################
from typing import List


class Solution:
  def solve(self, board: List[List[str]]) -> None:
    if not any(board):
      return

    m = len(board)
    n = len(board[0])
    save = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]

    while save:
      i, j = save.pop()
      if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
        board[i][j] = 'S'
        save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

    board[:] = [['XO'[c == 'S'] for c in row] for row in board]
