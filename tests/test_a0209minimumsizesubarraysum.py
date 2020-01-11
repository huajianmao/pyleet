from solutions.a0209minimumsizesubarraysum import Solution

solution = Solution()


def test_minSubArrayLen1():
  s = 7
  nums = [2, 3, 1, 2, 4, 3]
  expect = 2
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen2():
  s = 3
  nums = [2, 3, 1, 2, 4, 3]
  expect = 1
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen3():
  s = 4
  nums = [2, 3, 1, 2, 4, 3]
  expect = 1
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen4():
  s = 6
  nums = [2, 3, 1, 2, 4, 3]
  expect = 2
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen5():
  s = 9
  nums = [2, 3, 1, 2, 4, 3]
  expect = 3
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen6():
  s = 900
  nums = [2, 3, 1, 2, 4, 3]
  expect = 0
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect


def test_minSubArrayLen7():
  s = 15
  nums = [1, 2, 3, 4, 5]
  expect = 5
  actual = solution.minSubArrayLen(s, nums)
  assert actual == expect
