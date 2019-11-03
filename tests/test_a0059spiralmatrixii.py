from solutions.a0059spiralmatrixii import Solution

solution = Solution()


def test_generateMatrix1():
  n = 3
  expect = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]
  actual = solution.generateMatrix(n)
  assert actual == expect


def test_generateMatrix2():
  n = 2
  expect = [
    [1, 2],
    [4, 3]
  ]
  actual = solution.generateMatrix(n)
  assert actual == expect
