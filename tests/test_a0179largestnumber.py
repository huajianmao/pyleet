from solutions.a0179largestnumber import Solution

solution = Solution()


def test_largestNumber1():
  nums = [10, 2]
  expect = "210"
  actual = solution.largestNumber(nums)
  assert actual == expect


def test_largestNumber2():
  nums = [3, 30, 34, 5, 9]
  expect = "9534330"
  actual = solution.largestNumber(nums)
  assert actual == expect


def test_largestNumber3():
  nums = [3, 3330, 333, 2, 9]
  expect = "9333333302"
  actual = solution.largestNumber(nums)
  assert actual == expect


def test_largestNumber4():
  nums = [0, 0]
  expect = "0"
  actual = solution.largestNumber(nums)
  assert actual == expect
