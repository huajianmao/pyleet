from solutions.a0074search2dmatrix import Solution

solution = Solution()


def test_searchMatrix1():
  matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
  target = 3
  actual = solution.searchMatrix(matrix, target)
  assert actual


def test_searchMatrix2():
  matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
  target = 13
  actual = solution.searchMatrix(matrix, target)
  assert not actual


def test_searchMatrix3():
  matrix = [
    []
  ]
  target = 13
  actual = solution.searchMatrix(matrix, target)
  assert not actual


def test_searchMatrix4():
  matrix = [
    [1]
  ]
  target = 13
  actual = solution.searchMatrix(matrix, target)
  assert not actual


def test_searchMatrix5():
  matrix = [
    [1, 1]
  ]
  target = 2
  actual = solution.searchMatrix(matrix, target)
  assert not actual


def test_searchMatrix6():
  matrix = [
    [1]
  ]
  target = 1
  actual = solution.searchMatrix(matrix, target)
  assert actual
