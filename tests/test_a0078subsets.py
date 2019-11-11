from solutions.a0078subsets import Solution
from utils.listutil import ListUtil

solution = Solution()


def test_combine():
  nums = [1, 2, 3]
  expect = [
    [3],
    [1],
    [2],
    [1, 2, 3],
    [1, 3],
    [2, 3],
    [1, 2],
    []
  ]
  acutal = solution.subsets(nums)
  ListUtil.sortListOfLists(expect)
  ListUtil.sortListOfLists(acutal)
  assert acutal == expect
