from solutions.a0113pathsumii import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_generateTrees1():
  root = TreeNode.stringToTreeNode("[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]")
  sum = 22
  expect = [
    [5, 8, 4, 5],
    [5, 4, 11, 2]
  ]
  actual = solution.pathSum(root, sum)
  assert sorted(actual) == sorted(expect)
