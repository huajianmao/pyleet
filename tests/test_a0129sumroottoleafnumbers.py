from solutions.a0129sumroottoleafnumbers import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_sumNumbers1():
  root = TreeNode.stringToTreeNode('[1,2,3]')
  expect = 25
  actual = solution.sumNumbers(root)
  assert actual == expect


def test_sumNumbers2():
  root = TreeNode.stringToTreeNode('[4,9,0,5,1]')
  expect = 1026
  actual = solution.sumNumbers(root)
  assert actual == expect


def test_sumNumbers3():
  root = TreeNode.stringToTreeNode('[]')
  expect = 0
  actual = solution.sumNumbers(root)
  assert actual == expect


def test_sumNumbers4():
  root = TreeNode.stringToTreeNode('[1, null, 2]')
  expect = 12
  actual = solution.sumNumbers(root)
  assert actual == expect


def test_sumNumbers5():
  root = TreeNode.stringToTreeNode('[1, 2]')
  expect = 12
  actual = solution.sumNumbers(root)
  assert actual == expect
