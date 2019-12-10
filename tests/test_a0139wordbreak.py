from solutions.a0139wordbreak import Solution

solution = Solution()


def test_wordBreak1():
  s = "leetcode"
  wordDict = ["leet", "code"]
  actual = solution.wordBreak(s, wordDict)
  assert actual


def test_wordBreak2():
  s = "applepenapple"
  wordDict = ["apple", "pen"]
  actual = solution.wordBreak(s, wordDict)
  assert actual


def test_wordBreak3():
  s = "catsandog"
  wordDict = ["cats", "dog", "sand", "and", "cat"]
  actual = solution.wordBreak(s, wordDict)
  assert not actual


def test_wordBreak4():
  s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
  wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
  actual = solution.wordBreak(s, wordDict)
  assert not actual
