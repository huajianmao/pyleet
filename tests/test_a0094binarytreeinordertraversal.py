from solutions.a0094binarytreeinordertraversal import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_inorderTraversal1():
  root = TreeNode.stringToTreeNode("[1,null,2,3]")
  expect = [1, 3, 2]
  actual = solution.inorderTraversal(root)
  assert actual == expect


def test_inorderTraversal2():
  root = TreeNode.stringToTreeNode("[1,2,3]")
  expect = [2, 1, 3]
  actual = solution.inorderTraversal(root)
  assert actual == expect
