from solutions.a0082removeduplicatesfromsortedlistii import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_deleteDuplicates1():
  head = ListNode.stringToListNode('[1, 2, 3, 3, 4, 4, 5]')
  expect = '[1, 2, 5]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates2():
  head = ListNode.stringToListNode('[1, 1, 1, 2, 3]')
  expect = '[2, 3]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates3():
  head = ListNode.stringToListNode('[1, 1, 1, 1]')
  expect = '[]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates4():
  head = ListNode.stringToListNode('[]')
  expect = '[]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates5():
  head = ListNode.stringToListNode('[1]')
  expect = '[1]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates6():
  head = ListNode.stringToListNode('[1, 1]')
  expect = '[]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates7():
  head = ListNode.stringToListNode('[1, 2]')
  expect = '[1, 2]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates7():
  head = ListNode.stringToListNode('[1, 2, 2]')
  expect = '[1]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect


def test_deleteDuplicates8():
  head = ListNode.stringToListNode('[1, 1, 2, 2]')
  expect = '[]'
  actual = ListNode.listNodeToString(solution.deleteDuplicates(head))
  assert actual == expect
