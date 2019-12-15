from solutions.a0147insertionsortlist import Solution
from utils.list.ListNode import ListNode

solution = Solution()


def test_insertionsortlist1():
  head = ListNode.stringToListNode("[4,2,1,3]")
  expexct = ListNode.stringToListNode("[1,2,3,4]")
  actual = solution.insertionSortList(head)
  assert ListNode.listNodeToString(actual) == ListNode.listNodeToString(expexct)
