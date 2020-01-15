from solutions.a0213houserobberii import Solution

solution = Solution()


def test_rob1():
  nums = [2, 3, 2]
  expect = 3
  actual = solution.rob(nums)
  return actual == expect


def test_rob2():
  nums = [1, 2, 3, 1]
  expect = 4
  actual = solution.rob(nums)
  return actual == expect


def test_rob3():
  nums = [1]
  expect = 1
  actual = solution.rob(nums)
  return actual == expect
