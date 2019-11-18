from solutions.a0092reverselinkedlistii import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_reverseBetween1():
  head = ListNode.stringToListNode("[1,2,3,4,5]")
  m = 2
  n = 4
  expect = "[1, 4, 3, 2, 5]"
  actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
  assert actual == expect


def test_reverseBetween2():
  head = ListNode.stringToListNode("[1,2,3,4,5]")
  m = 5
  n = 5
  expect = "[1, 2, 3, 4, 5]"
  actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
  assert actual == expect


def test_reverseBetween3():
  head = ListNode.stringToListNode("[1,2,3,4,5]")
  m = 1
  n = 1
  expect = "[1, 2, 3, 4, 5]"
  actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
  assert actual == expect


def test_reverseBetween4():
  head = ListNode.stringToListNode("[1,2,3,4,5]")
  m = 1
  n = 3
  expect = "[3, 2, 1, 4, 5]"
  actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
  assert actual == expect


def test_reverseBetween5():
  head = ListNode.stringToListNode("[1,2,3,4,5,6,7,8,9]")
  m = 1
  n = 5
  expect = "[5, 4, 3, 2, 1, 6, 7, 8, 9]"
  actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
  assert actual == expect
