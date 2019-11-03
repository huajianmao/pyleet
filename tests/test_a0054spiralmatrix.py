from solutions.a0054spiralmatrix import Solution

solution = Solution()


def test_spiralOrder():
  matrix = [
      [1, 2, 3],
      [4, 5, 6]
  ]

  expect = [1, 2, 3, 5, 6, 4]
  acutal = solution.spiralOrder(matrix)
  assert acutal != expect
