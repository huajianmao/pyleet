from solutions.a0165compareversionnumbers import Solution

solution = Solution()


def test_compareVersion1():
  version1 = "0.1"
  version2 = "1.1"
  expect = -1
  actual = solution.compareVersion(version1, version2)
  assert actual == expect


def test_compareVersion2():
  version1 = "1.0.1"
  version2 = "1"
  expect = 1
  actual = solution.compareVersion(version1, version2)
  assert actual == expect


def test_compareVersion3():
  version1 = "7.5.2.4"
  version2 = "7.5.3"
  expect = -1
  actual = solution.compareVersion(version1, version2)
  assert actual == expect


def test_compareVersion4():
  version1 = "1.01"
  version2 = "1.001"
  expect = 0
  actual = solution.compareVersion(version1, version2)
  assert actual == expect


def test_compareVersion5():
  version1 = "1.0"
  version2 = "1.0.0"
  expect = 0
  actual = solution.compareVersion(version1, version2)
  assert actual == expect


def test_compareVersion6():
  version1 = "1.0.0"
  version2 = "1.0.0"
  expect = 0
  actual = solution.compareVersion(version1, version2)
  assert actual == expect
