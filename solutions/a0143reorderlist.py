# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/reorder-list/
#
# DESC:
# =====
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
################################################
from utils.list.ListNode import ListNode


class Solution:
  def reorderList(self, head):
    if not head or not head.next or not head.next.next:
      return
    slow = head
    fast = head
    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    head1 = head
    head2 = slow.next
    slow.next = None
    cur = head2
    pre = None
    while cur:
      curnext = cur.next
      cur.next = pre
      pre = cur
      cur = curnext

    cur1 = head1
    cur2 = pre
    while cur2:
      next1 = cur1.next
      next2 = cur2.next
      cur1.next = cur2
      cur2.next = next1
      cur1 = next1
      cur2 = next2
