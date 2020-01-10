from solutions.a0208implementtrieprefixtree import Trie


def test_trie1():
  trie = Trie()
  trie.insert("apple")
  assert trie.search("apple")
  assert not trie.search("app")
  assert trie.startsWith("app")
  trie.insert("app")
  assert trie.search("app")
  assert not trie.search("b")
  trie.insert("b")
  assert trie.search("b")
  assert not trie.startsWith("c")
