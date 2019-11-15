from solutions.a0086partitionlist import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_partitionList1():
  head = ListNode.stringToListNode('[1, 4, 3, 2, 5, 2]')
  x = 3
  expect = '[1, 2, 2, 4, 3, 5]'
  actual = ListNode.listNodeToString(solution.partition(head, x))
  assert actual == expect


def test_partitionList2():
  head = ListNode.stringToListNode('[1, 4, 3, 2, 5, 2]')
  x = 4
  expect = '[1, 3, 2, 2, 4, 5]'
  actual = ListNode.listNodeToString(solution.partition(head, x))
  assert actual == expect
