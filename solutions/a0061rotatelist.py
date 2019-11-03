# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/rotate-list/
#
# DESC:
# =====
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#
################################################
from utils.list.ListNode import ListNode


class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
      return head

    size = 0
    it = head
    while it is not None:
      size += 1
      it = it.next

    k %= size
    if k == 0:
      return head

    skip = size - k - 1
    it = head
    while skip > 0:
      it = it.next
      skip -= 1

    newHead = it.next
    it.next = None
    it = newHead
    while it.next is not None:
      it = it.next

    it.next = head
    return newHead
