from solutions.a0095uniquebinarysearchtreesii import Solution
from utils.tree.TreeNode import TreeNode

import json

solution = Solution()


# def test_generateTrees1():
#   n = 3
#   expect = sorted([TreeNode.integerListToString(nums) for nums in [
#     [1, None, 3, 2],
#     [3, 2, None, 1],
#     [3, 1, None, None, 2],
#     [2, 1, 3],
#     [1, None, 2, None, 3]
#   ]])
#   actual = solution.generateTrees(n)
#   assert len(actual) == len(expect)
#   actual = sorted([TreeNode.integerListToString(nums) for nums in [TreeNode.treeToList(node) for node in actual]])
#   assert actual == expect


def test_generateTrees2():
  n = 0
  expect = []
  actual = solution.generateTrees(n)
  assert len(actual) == len(expect)
  assert actual == expect


def test_generateTrees3():
  n = 1
  expect = sorted([TreeNode.integerListToString(nums) for nums in [[1]]])
  actual = solution.generateTrees(n)
  assert len(actual) == len(expect)
  actual = sorted([TreeNode.integerListToString(nums) for nums in [TreeNode.treeToList(node) for node in actual]])
  assert actual == expect


def test_generateTrees4():
  n = 2
  expect = sorted([TreeNode.integerListToString(nums) for nums in [[2, 1], [1, None, 2]]])
  actual = solution.generateTrees(n)
  assert len(actual) == len(expect)
  actual = sorted([TreeNode.integerListToString(nums) for nums in [TreeNode.treeToList(node) for node in actual]])
  assert actual == expect
