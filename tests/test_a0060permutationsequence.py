from solutions.a0060permutationsequence import Solution

solution = Solution()


def test_getPermutation1():
  n = 3
  k = 3
  expect = "213"
  actual = solution.getPermutation(n, k)
  assert actual == expect


def test_getPermutation2():
  n = 4
  k = 9
  expect = "2314"
  actual = solution.getPermutation(n, k)
  assert actual == expect


def test_getPermutation3():
  n = 4
  k = 6
  expect = "1432"
  actual = solution.getPermutation(n, k)
  assert actual == expect


def test_getPermutation4():
  n = 3
  k = 1
  expect = "123"
  actual = solution.getPermutation(n, k)
  assert actual == expect
