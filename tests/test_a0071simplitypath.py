from solutions.a0071simplitypath import Solution

solution = Solution()


def test_uniquePaths1():
  path = "/home/"
  expect = "/home"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths2():
  path = "/../"
  expect = "/"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths3():
  path = "/home//foo/"
  expect = "/home/foo"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths4():
  path = "/a/./b/../../c/"
  expect = "/c"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths5():
  path = "/a/../../b/../c//.//"
  expect = "/c"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths6():
  path = "/a//b////c/d//././/.."
  expect = "/a/b/c"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths7():
  path = "/"
  expect = "/"
  actual = solution.simplifyPath(path)
  assert actual == expect


def test_uniquePaths8():
  path = "/../../"
  expect = "/"
  actual = solution.simplifyPath(path)
  assert actual == expect
