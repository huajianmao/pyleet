from solutions.a0079wordsearch import Solution

solution = Solution()


def test_exist1():
  board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  assert solution.exist(board, "ABCCED")
  assert solution.exist(board, "SEE")
  assert not solution.exist(board, "ABCB")


def test_exist2():
  board = []
  assert not solution.exist(board, "ABCCED")
