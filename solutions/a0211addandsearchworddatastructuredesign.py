# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/add-and-search-word-data-structure-design/
#
# DESC:
# =====
# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.
#
# Example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
# Note:
# You may assume that all words are consist of lowercase letters a-z..
################################################


class Node:
  def __init__(self):
    self.isWord = False
    self.children = {}


class WordDictionary:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = Node()

  def addWord(self, word: str) -> None:
    """
    Adds a word into the data structure.
    """
    node = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = Node()
      node = node.children[c]
    node.isWord = True

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the data structure.
    A word could contain the dot character '.' to represent any one letter.
    """
    return self.find(self.root, word)

  def find(self, node, word):
    if len(word) == 0:
      return node.isWord
    else:
      if word[0] == '.':
        for child in node.children:
          if self.find(node.children[child], word[1:]):
            return True
      elif word[0] in node.children:
        return self.find(node.children[word[0]], word[1:])
      else:
        return False
      return False
