# -*- coding: utf-8 -*-

import json


# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  @classmethod
  def stringToListNode(cls, string):
    # Generate list from the input
    numbers = json.loads(string)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
      ptr.next = ListNode(number)
      ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

  @classmethod
  def listNodeToString(cls, node):
    if not node:
      return "[]"

    result = ""
    while node:
      result += str(node.val) + ", "
      node = node.next
    return "[" + result[:-2] + "]"
