from solutions.a0201bitwiseandofnumbersrange import Solution

solution = Solution()


def test_rangeBitwiseAnd1():
  m = 5
  n = 7
  expect = 4
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect


def test_rangeBitwiseAnd2():
  m = 0
  n = 1
  expect = 0
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect


def test_rangeBitwiseAnd3():
  m = 0
  n = 0
  expect = 0
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect


def test_rangeBitwiseAnd4():
  m = 1
  n = 2
  expect = 0
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect


def test_rangeBitwiseAnd5():
  m = 1
  n = 3
  expect = 0
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect


def test_rangeBitwiseAnd6():
  m = 2
  n = 4
  expect = 0
  actual = solution.rangeBitwiseAnd(m, n)
  assert actual == expect
