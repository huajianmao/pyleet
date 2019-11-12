from solutions.a0080removeduplicatesfromsortedarrayii import Solution

solution = Solution()


def test_removeDuplicates1():
  nums = [1, 1, 1, 2, 2, 3]
  expect = 5
  actual = solution.removeDuplicates(nums)
  assert actual == expect


def test_removeDuplicates2():
  nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
  expect = 7
  actual = solution.removeDuplicates(nums)
  assert actual == expect


def test_removeDuplicates3():
  nums = []
  expect = 0
  actual = solution.removeDuplicates(nums)
  assert actual == expect


def test_removeDuplicates4():
  nums = [1]
  expect = 1
  actual = solution.removeDuplicates(nums)
  assert actual == expect


def test_removeDuplicates5():
  nums = [1, 1]
  expect = 2
  actual = solution.removeDuplicates(nums)
  assert actual == expect


def test_removeDuplicates6():
  nums = [1, 2]
  expect = 2
  actual = solution.removeDuplicates(nums)
  assert actual == expect
