from solutions.a0114flattenbinarytreetolinkedlist import Solution
from utils.tree.TreeNode import TreeNode

solution = Solution()


def test_buildTree1():
  root = TreeNode.stringToTreeNode("[1,2,5,3,4,null,6]")
  expect = TreeNode.stringToTreeNode("[1,null,2,null,3,null,4,null,5,null,6]")
  solution.flatten(root)
  assert TreeNode.isSame(root, expect)


def test_buildTree2():
  root = TreeNode.stringToTreeNode("[]")
  expect = TreeNode.stringToTreeNode("[]")
  solution.flatten(root)
  assert TreeNode.isSame(root, expect)
