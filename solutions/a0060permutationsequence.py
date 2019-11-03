# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/permutation-sequence/
#
# DESC:
# =====
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"
#
################################################


class Solution:

  def getPermutation(self, n: int, k: int) -> str:
    factorial = [1]
    for i in range(n):
      factorial.append(factorial[-1] * (i + 1))
    numbers = [i + 1 for i in range(n)]

    result = ""
    k -= 1
    for i in range(1, n + 1):
      index = k // factorial[n - i]
      result += str(numbers[index])
      numbers.remove(numbers[index])
      k -= index * factorial[n - i]

    return result
