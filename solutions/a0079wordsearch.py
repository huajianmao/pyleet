# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/word-search/
#
# DESC:
# =====
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
################################################
from typing import List


class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    if not board:
      return False

    for i in range(len(board)):
      for j in range(len(board[0])):
        if self.helper(board, i, j, word):
          return True

    return False

  def helper(self, board, i, j, word):
    if len(word) == 0:
      return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
      return False

    tmp = board[i][j]
    board[i][j] = "#"
    result = self.helper(board, i + 1, j, word[1:]) \
        or self.helper(board, i - 1, j, word[1:]) \
        or self.helper(board, i, j + 1, word[1:]) \
        or self.helper(board, i, j - 1, word[1:])
    board[i][j] = tmp

    return result
