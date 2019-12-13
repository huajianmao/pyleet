from solutions.a0144binarytreepreordertraversal import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_preorderTraversal1():
  root = TreeNode.stringToTreeNode("[1,null,2,3]")
  expect = [1, 2, 3]
  actual = solution.preorderTraversal(root)
  assert actual == expect


def test_preorderTraversal2():
  root = TreeNode.stringToTreeNode("[1]")
  expect = [1]
  actual = solution.preorderTraversal(root)
  assert actual == expect


def test_preorderTraversal3():
  root = TreeNode.stringToTreeNode("[]")
  expect = []
  actual = solution.preorderTraversal(root)
  assert actual == expect


def test_preorderTraversal4():
  root = TreeNode.stringToTreeNode("[1,4,3,2]")
  expect = [1, 4, 2, 3]
  actual = solution.preorderTraversal(root)
  assert actual == expect
