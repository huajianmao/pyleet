from solutions.a0148sortlist import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_sortlist1():
  head = ListNode.stringToListNode("[4,2,1,3]")
  expect = ListNode.stringToListNode("[1,2,3,4]")
  actual = solution.sortList(head)
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expect)
