from solutions.a0077combinations import Solution
from utils.listutil import ListUtil

solution = Solution()


def test_combine():
  n = 4
  k = 2
  expect = [
    [2, 4],
    [3, 4],
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 4],
  ]
  acutal = solution.combine(n, k)
  ListUtil.sortListOfLists(expect)
  ListUtil.sortListOfLists(acutal)
  assert acutal == expect
