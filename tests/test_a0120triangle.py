from solutions.a0120triangle import Solution

solution = Solution()


def test_minimumTotal1():
  triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
  ]
  expect = 11
  actual = solution.minimumTotal(triangle)
  assert actual == expect


def test_minimumTotal2():
  triangle = [
    [1]
  ]
  expect = 1
  actual = solution.minimumTotal(triangle)
  assert actual == expect
