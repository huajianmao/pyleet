# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/merge-intervals/
#
# DESC:
# =====
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
################################################
from typing import List


class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
      return intervals
    else:
      result = []
      intervals.sort(key=lambda x: x[0])
      current = intervals[0]

      for interval in intervals:
        if interval[0] <= current[1]:
          current = [current[0], max(interval[1], current[1])]
        else:
          result.append(current)
          current = interval
      result.append(current)
      return result
