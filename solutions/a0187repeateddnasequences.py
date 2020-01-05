# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/repeated-dna-sequences/
#
# DESC:
# =====
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA,
# it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# Example:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
################################################
from typing import List


class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    dic = {}
    for i in range(len(s) - 9):
      seg = s[i:i + 10]
      dic[seg] = (dic[seg] if seg in dic else 0) + 1

    return [key for key in dic.keys() if dic[key] >= 2]
