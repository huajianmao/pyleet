from solutions.a0173binarysearchtreeiterator import BSTIterator
from utils.tree.TreeNode import TreeNode


def test_iterator():
  root = TreeNode.stringToTreeNode("[7,3,15,null,null,9,20]")
  iterator = BSTIterator(root)
  assert iterator.next() == 3
  assert iterator.next() == 7
  assert iterator.hasNext()
  assert iterator.next() == 9
  assert iterator.hasNext()
  assert iterator.next() == 15
  assert iterator.hasNext()
  assert iterator.next() == 20
  assert not iterator.hasNext()
