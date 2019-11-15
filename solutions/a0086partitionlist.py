# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/partition-list/
#
# DESC:
# =====
# Given a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
################################################

from utils.list.ListNode import ListNode


class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    node = head

    head = ListNode(0)
    prevTail = head
    pivot = ListNode(0)
    postTail = pivot

    while node:
      if node.val >= x:
        postTail.next = node
        postTail = node
      else:
        prevTail.next = node
        prevTail = node
      node = node.next

    prevTail.next = pivot.next
    postTail.next = None
    return head.next
