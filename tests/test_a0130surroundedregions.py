from solutions.a0130surroundedregions import Solution

solution = Solution()


def test_solve1():
  board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
  ]
  expect = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X']
  ]
  solution.solve(board)
  assert board == expect


def test_solve2():
  board = []
  expect = []
  solution.solve(board)
  assert board == expect
