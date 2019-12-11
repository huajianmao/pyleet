from solutions.a0142linkedlistcycleii import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_detectCycle1():
  head = ListNode.stringToListNode("[3,2,0,-4]")
  expect = head.next
  expect.next.next.next = expect
  actual = solution.detectCycle(head)
  assert actual == expect


def test_detectCycle2():
  head = ListNode.stringToListNode("[1, 2]")
  expect = head
  expect.next.next = expect
  actual = solution.detectCycle(head)
  assert actual == expect


def test_detectCycle3():
  head = ListNode.stringToListNode("[1]")
  expect = None
  actual = solution.detectCycle(head)
  assert actual == expect


def test_detectCycle4():
  head = ListNode.stringToListNode("[1, 2, 3, 4]")
  expect = None
  actual = solution.detectCycle(head)
  assert actual == expect
