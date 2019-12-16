# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/sort-list/
#
# DESC:
# =====
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
#
# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->55
################################################
from utils.list.ListNode import ListNode


class Solution:
  def sortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head

    slow = head
    fast = head
    prev = None
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    prev.next = None

    first = self.sortList(head)
    second = self.sortList(slow)

    return self.merge(first, second)

  def merge(self, head1, head2):
    dummy = ListNode(None)
    tail = dummy
    while head1 and head2:
      if head1.val < head2.val:
        tail.next = head1
        tail = tail.next
        head1 = head1.next
      else:
        tail.next = head2
        tail = tail.next
        head2 = head2.next

    tail.next = head1 or head2
    return dummy.next
