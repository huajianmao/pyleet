from solutions.a0091decodeways import Solution

solution = Solution()


def test_subsetsWithDup1():
  s = "12"
  expect = 2
  actual = solution.numDecodings(s)
  assert actual == expect


def test_subsetsWithDup2():
  s = "226"
  expect = 3
  actual = solution.numDecodings(s)
  assert actual == expect


def test_subsetsWithDup3():
  s = "2"
  expect = 1
  actual = solution.numDecodings(s)
  assert actual == expect


def test_subsetsWithDup4():
  s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
  expect = 3981312
  actual = solution.numDecodings(s)
  assert actual == expect


def test_subsetsWithDup5():
  s = "2303030"
  expect = 0
  actual = solution.numDecodings(s)
  assert actual == expect
