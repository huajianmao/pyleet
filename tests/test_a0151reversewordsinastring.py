from solutions.a0151reversewordsinastring import Solution

solution = Solution()


def test_reverseword1():
  s = "the sky is blue"
  expect = "blue is sky the"
  actual = solution.reverseWords(s)
  assert actual == expect


def test_reverseword2():
  s = "  hello world!  "
  expect = "world! hello"
  actual = solution.reverseWords(s)
  assert actual == expect


def test_reverseword3():
  s = "a good   example"
  expect = "example good a"
  actual = solution.reverseWords(s)
  assert actual == expect
