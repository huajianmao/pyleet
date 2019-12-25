from solutions.a0152maximumproductsubarray import Solution

solution = Solution()


def test_maxProduct1():
  nums = [2, 3, -2, 4]
  expect = 6
  actual = solution.maxProduct(nums)
  assert actual == expect


def test_maxProduct1():
  nums = [-2, 0, -1]
  expect = 0
  actual = solution.maxProduct(nums)
  assert actual == expect
