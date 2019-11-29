from solutions.a0109convertsortedlisttobinarysearchtree import Solution
from utils.list.ListNode import ListNode
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_buildTree1():
  head = ListNode.stringToListNode("[-10,-3,0,5,9]")
  expect = TreeNode.stringToTreeNode("[0,-3,9,-10,null,5]")
  actual = solution.sortedListToBST(head)
  assert TreeNode.isSame(actual, expect)
