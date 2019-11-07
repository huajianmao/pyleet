from solutions.a0056mergeintervals import Solution

solution = Solution()


def test_merge1():
  intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
  expect = [[1, 6], [8, 10], [15, 18]]
  acutal = solution.merge(intervals)
  assert acutal == expect


def test_merge2():
  intervals = [[4, 5], [1, 4]]
  expect = [[1, 5]]
  acutal = solution.merge(intervals)
  assert acutal == expect


def test_merge3():
  intervals = [[1, 4], [2, 3]]
  expect = [[1, 4]]
  acutal = solution.merge(intervals)
  assert acutal == expect


def test_merge4():
  intervals = []
  expect = []
  acutal = solution.merge(intervals)
  assert acutal == expect
