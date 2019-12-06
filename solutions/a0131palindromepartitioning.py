# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/palindrome-partitioning/
#
# DESC:
# =====
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
################################################
from typing import List


class Solution:
  def partition(self, s: str) -> List[List[str]]:
    result = []
    if len(s) == 1 or (len(s) > 1 and self.isPalindrome(s)):
      result.append([s])

    for length in range(1, len(s)):
      part1 = s[:length]
      if self.isPalindrome(part1):
        lefts = self.partition(s[length:])
        for left in lefts:
          left.insert(0, part1)
          result.append(left)

    return result

  def isPalindrome(self, s):
    length = len(s)
    for i in range(length // 2):
      if s[i] != s[length - 1 - i]:
        return False
      else:
        pass
    return True
