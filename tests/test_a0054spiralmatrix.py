from solutions.a0054spiralmatrix import Solution

solution = Solution()


def test_spiralOrder1():
  matrix = [
      [1, 2, 3],
      [4, 5, 6]
  ]

  expect = [1, 2, 3, 6, 5, 4]
  acutal = solution.spiralOrder(matrix)
  assert acutal == expect


def test_spiralOrder2():
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  expect = [1, 2, 3, 6, 9, 8, 7, 4, 5]
  acutal = solution.spiralOrder(matrix)
  assert acutal == expect


def test_spiralOrder3():
  matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
  ]

  expect = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
  acutal = solution.spiralOrder(matrix)
  assert acutal == expect
