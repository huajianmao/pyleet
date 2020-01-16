from solutions.a0216combinationsumiii import Solution

solution = Solution()


def test_combinationSum31():
  k = 3
  n = 7
  expect = [[1, 2, 4]]
  actual = solution.combinationSum3(k, n)
  assert actual == expect


def test_combinationSum32():
  k = 3
  n = 9
  expect = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
  actual = solution.combinationSum3(k, n)
  assert actual == expect
