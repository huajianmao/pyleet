from solutions.a0098validatebinarysearchtree import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_isValidBST1():
  root = TreeNode.stringToTreeNode("[2,1,3]")
  actual = solution.isValidBST(root)
  assert actual


def test_isValidBST2():
  root = TreeNode.stringToTreeNode("[5,1,4,null,null,3,6]")
  actual = solution.isValidBST(root)
  assert not actual


def test_isValidBST3():
  root = TreeNode.stringToTreeNode("[1,1,1]")
  actual = solution.isValidBST(root)
  assert not actual


def test_isValidBST4():
  root = TreeNode.stringToTreeNode("[0,null,-1]")
  actual = solution.isValidBST(root)
  assert not actual


def test_isValidBST5():
  root = TreeNode.stringToTreeNode("[10,5,15,null,null,6,20]")
  actual = solution.isValidBST(root)
  assert not actual


def test_isValidBST6():
  root = TreeNode.stringToTreeNode("[]")
  actual = solution.isValidBST(root)
  assert actual
