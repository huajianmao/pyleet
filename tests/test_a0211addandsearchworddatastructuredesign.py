from solutions.a0211addandsearchworddatastructuredesign import WordDictionary


def test_wordDictionary1():
  dictionary = WordDictionary()
  dictionary.addWord("bad")
  dictionary.addWord("bcd")
  dictionary.addWord("dad")
  dictionary.addWord("dcd")
  dictionary.addWord("mad")
  assert not dictionary.search("pad")
  assert dictionary.search("bad")
  assert dictionary.search(".ad")
  assert dictionary.search("b..")
  assert not dictionary.search("..c")
  assert dictionary.search(".cd")
