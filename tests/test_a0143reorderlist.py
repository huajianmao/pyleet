from solutions.a0143reorderlist import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_reorderList1():
  head = ListNode.stringToListNode("[1,2,3,4]")
  expect = ListNode.stringToListNode("[1,4,2,3]")
  solution.reorderList(head)


def test_reorderList2():
  head = ListNode.stringToListNode("[1,2,3,4,5]")
  expect = ListNode.stringToListNode("[1,5,2,4,3]")
  solution.reorderList(head)


def test_reorderList3():
  head = ListNode.stringToListNode("[]")
  expect = ListNode.stringToListNode("[]")
  solution.reorderList(head)


def test_reorderList4():
  head = ListNode.stringToListNode("[1]")
  expect = ListNode.stringToListNode("[1]")
  solution.reorderList(head)


def test_reorderList5():
  head = ListNode.stringToListNode("[1,2]")
  expect = ListNode.stringToListNode("[1,2]")
  solution.reorderList(head)


def test_reorderList6():
  head = ListNode.stringToListNode("[1,2,3]")
  expect = ListNode.stringToListNode("[1,3,2]")
  solution.reorderList(head)
