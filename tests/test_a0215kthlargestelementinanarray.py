from solutions.a0215kthlargestelementinanarray import Solution

solution = Solution()


def test_findKthLargest1():
  nums = [3, 2, 1, 5, 6, 4]
  k = 2
  expect = 5
  actual = solution.findKthLargest(nums, k)
  assert actual == expect


def test_findKthLargest2():
  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
  k = 4
  expect = 4
  actual = solution.findKthLargest(nums, k)
  assert actual == expect
