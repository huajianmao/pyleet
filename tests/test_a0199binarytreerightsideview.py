from solutions.a0199binarytreerightsideview import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_rightSideView1():
  root = TreeNode.stringToTreeNode("[1,2,3,null,5,null,4]")
  expect = [1, 3, 4]
  actual = solution.rightSideView(root)
  assert actual == expect
