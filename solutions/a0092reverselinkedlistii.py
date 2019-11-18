# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/reverse-linked-list-ii/
#
# DESC:
# =====
# Reverse a linked list from position m to n.
# Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
################################################
from utils.list.ListNode import ListNode


class Solution:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if m == n:
      return head
    n -= m - 1

    dummy = ListNode(0)
    tail1, dummy.next = dummy, head
    for _ in range(m - 1):
      tail1, head = head, head.next

    tail2, head, tail1.next = head, head.next, head
    for _ in range(n - 1):
      head.next, tail1.next, head = tail1.next, head, head.next
    tail2.next = head

    return dummy.next
