# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#
# DESC:
# =====
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
#
################################################

from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    # return target in nums
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] == target:
            return True
        while start < middle and nums[start] == nums[middle]:
            start += 1
        if nums[start] <= nums[middle]:
            if nums[start] <= target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if nums[middle] < target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1
    return False
