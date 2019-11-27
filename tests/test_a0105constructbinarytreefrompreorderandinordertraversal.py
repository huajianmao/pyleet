from solutions.a0105constructbinarytreefrompreorderandinordertraversal import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_buildTree1():
  preorder = [3, 9, 20, 15, 7]
  inorder = [9, 3, 15, 20, 7]
  expect = TreeNode.stringToTreeNode("[3,9,20,null,null,15,7]")
  actual = solution.buildTree(preorder, inorder)
  assert TreeNode.isSame(actual, expect)


def test_buildTree2():
  preorder = []
  inorder = [9]
  expect = TreeNode.stringToTreeNode("[]")
  actual = solution.buildTree(preorder, inorder)
  assert TreeNode.isSame(actual, expect)
