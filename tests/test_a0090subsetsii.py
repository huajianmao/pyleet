from solutions.a0090subsetsii import Solution

solution = Solution()


def test_subsetsWithDup():
  nums = [1, 2, 2]
  expect = [
    [2],
    [1],
    [1, 2, 2],
    [2, 2],
    [1, 2],
    []
  ]
  actual = solution.subsetsWithDup(nums)
  assert sorted(actual) == sorted(expect)
