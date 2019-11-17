# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/decode-ways/
#
# DESC:
# =====
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).]
#
################################################


class Solution:
  def numDecodings(self, s: str) -> int:
    length = len(s)
    count = [0 for _ in range(length + 1)]
    count[0] = 1
    count[1] = 0 if s[0] == '0' else 1

    for i in range(2, length + 1):
      if count[i - 1] == 0 and count[i - 2] == 0:
        return 0
      if 0 < int(s[i - 1: i]) <= 9:
        count[i] += count[i - 1]
      if 10 <= int(s[i - 2:i]) <= 26:
        count[i] += count[i - 2]

    return count[length]
