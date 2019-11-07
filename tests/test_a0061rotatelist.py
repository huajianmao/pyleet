from solutions.a0061rotatelist import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_rotateRight1():
  head = ListNode.stringToListNode("[1, 2, 3, 4, 5]")
  k = 2
  actual = solution.rotateRight(head, k)
  expect = ListNode.stringToListNode("[4, 5, 1, 2, 3]")
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expect)


def test_rotateRight2():
  head = ListNode.stringToListNode("[0, 1, 2]")
  k = 4
  actual = solution.rotateRight(head, k)
  expect = ListNode.stringToListNode("[2, 0, 1]")
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expect)


def test_rotateRight3():
  head = ListNode.stringToListNode("[]")
  k = 0
  actual = solution.rotateRight(head, k)
  expect = ListNode.stringToListNode("[]")
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expect)


def test_rotateRight4():
  head = ListNode.stringToListNode("[0, 1, 2]")
  k = 3
  actual = solution.rotateRight(head, k)
  expect = ListNode.stringToListNode("[0, 1, 2]")
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expect)
