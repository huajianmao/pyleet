from solutions.a0102binarytreelevelordertraversal import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_generateTrees1():
  root = TreeNode.stringToTreeNode("[3,9,20,null,null,15,7]")
  expect = [
    [3],
    [9, 20],
    [15, 7]
  ]
  actual = solution.levelOrder(root)
  assert actual == expect


def test_generateTrees2():
  root = TreeNode.stringToTreeNode("[]")
  expect = []
  actual = solution.levelOrder(root)
  assert actual == expect
