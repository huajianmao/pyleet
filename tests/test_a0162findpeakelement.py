from solutions.a0162findpeakelement import Solution

solution = Solution()


def test_findPeakElement1():
  nums = [1, 2, 3, 1]
  expect = [2]
  actual = solution.findPeakElement(nums)
  assert actual in expect


def test_findPeakElement2():
  nums = [1, 2, 1, 3, 5, 6, 4]
  expect = [1, 5]
  actual = solution.findPeakElement(nums)
  assert actual in expect
