from solutions.a0062uniquepaths import Solution

solution = Solution()


def test_uniquePaths1():
  m, n = 3, 2
  expect = 3
  actual = solution.uniquePaths(m, n)
  assert actual == expect


def test_uniquePaths2():
  m, n = 7, 3
  expect = 28
  actual = solution.uniquePaths(m, n)
  assert actual == expect


def test_uniquePaths3():
  m, n = 23, 12
  expect = 193536720
  actual = solution.uniquePaths(m, n)
  assert actual == expect
