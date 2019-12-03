from solutions.a0127wordladder import Solution

solution = Solution()


def test_ladderLength1():
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
  expect = 5
  actual = solution.ladderLength(beginWord, endWord, wordList)
  assert actual == expect


def test_ladderLength2():
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot", "dot", "dog", "lot", "log"]
  expect = 0
  actual = solution.ladderLength(beginWord, endWord, wordList)
  assert actual == expect
