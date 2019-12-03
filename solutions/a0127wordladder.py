# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/word-ladder/
#
# DESC:
# =====
# Given two words (beginWord and endWord), and a dictionary's word list,
# find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
################################################
import collections
import string
from typing import List


class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    queue = collections.deque([(beginWord, 1)])
    visited = set()
    alphabet = string.ascii_lowercase
    while queue:
      word, length = queue.popleft()
      if word == endWord:
        return length

      for i in range(len(word)):
        for ch in alphabet:
          newWord = word[:i] + ch + word[i + 1:]
          if newWord in wordList and newWord not in visited:
            queue.append((newWord, length + 1))
            visited.add(newWord)
    return 0
