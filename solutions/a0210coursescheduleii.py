# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/course-schedule-ii/
#
# DESC:
# =====
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites,
# for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
#
# Example 1:
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
#
# Example 2:
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites..
################################################
from typing import List


class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    inds = {}
    outds = {}
    for prerequisite in prerequisites:
      prev = prerequisite[1]
      post = prerequisite[0]
      if post not in inds:
        inds[post] = set()
      inds[post].add(prev)
      if prev not in outds:
        outds[prev] = set()
      outds[prev].add(post)
    result = list(set(i for i in range(numCourses) - inds.keys()))

    while True:
      starts = outds.keys() - inds.keys()
      if len(outds) == 0:
        return result
      if len(starts) == 0:
        return []
      for key in starts:
        for post in outds[key]:
          inds[post].remove(key)
          if len(inds[post]) == 0:
            result.append(post)
            del inds[post]
        del outds[key]
