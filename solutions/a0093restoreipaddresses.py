# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/restore-ip-addresses/
#
# DESC:
# =====
# Given a string containing only digits,
# restore it by returning all possible valid IP address combinations.
#
# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
################################################
from typing import List


class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    length = len(s)
    if length > 12 or length < 4:
      return []

    result = []
    for i in range(1, 4):
      if length - i > 9 or (i == 3 and int(s[0:i]) > 255) or (i > 1 and s[0] == '0'):
        continue
      for j in range(i + 1, i + 4):
        if length - j > 6 or (j == i + 3 and int(s[i:j]) > 255) or (j > i + 1 and s[i] == '0'):
          continue
        for k in range(j + 1, j + 4):
          if length - k > 3 or k >= length \
            or (k == j + 3 and int(s[j:k]) > 255) \
            or (k > j + 1 and s[j] == '0') \
            or (length - k > 1 and s[k] == '0'):
            continue
          if int(s[k:]) <= 255:
            result.append('.'.join([s[:i], s[i:j], s[j:k], s[k:]]))
    return result
