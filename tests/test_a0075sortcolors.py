from solutions.a0075sortcolors import Solution

solution = Solution()


def test_sortColors1():
  nums = [2, 0, 2, 1, 1, 0]
  expect = [0, 0, 1, 1, 2, 2]
  solution.sortColors(nums)
  assert nums == expect
