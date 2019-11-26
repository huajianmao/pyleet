from solutions.a0103binarytreezigzaglevelordertraversal import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_generateTrees1():
  root = TreeNode.stringToTreeNode("[3,9,20,null,null,15,7]")
  expect = [
    [3],
    [20, 9],
    [15, 7]
  ]
  actual = solution.zigzagLevelOrder(root)
  assert actual == expect


def test_generateTrees2():
  root = TreeNode.stringToTreeNode("[]")
  expect = []
  actual = solution.zigzagLevelOrder(root)
  assert actual == expect


def test_generateTrees3():
  root = TreeNode.stringToTreeNode("[1,2,3,4,null,null,5]")
  expect = [[1], [3, 2], [4, 5]]
  actual = solution.zigzagLevelOrder(root)
  assert actual == expect
