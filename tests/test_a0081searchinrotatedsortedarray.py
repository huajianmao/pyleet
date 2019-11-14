from solutions.a0081searchinrotatedsortedarrayii import Solution

solution = Solution()


def test_search1():
  nums = [2, 5, 6, 0, 0, 1, 2]
  target = 0
  actual = solution.search(nums, target)
  assert actual


def test_search2():
  nums = [2, 5, 6, 0, 0, 1, 2]
  target = 3
  actual = solution.search(nums, target)
  assert not actual


def test_search3():
  nums = [0, 0, 6, -2, -1, 0, 0]
  target = 3
  actual = solution.search(nums, target)
  assert not actual


def test_search4():
  nums = [0, 0, 6, -2, -1, 0, 0]
  target = 6
  actual = solution.search(nums, target)
  assert actual


def test_search5():
  nums = [6, 6, 6, 0, 0, 1, 2]
  target = 6
  actual = solution.search(nums, target)
  assert actual


def test_search6():
  nums = [6, 6, 6, 6, 6, 6, 6]
  target = 6
  actual = solution.search(nums, target)
  assert actual


def test_search7():
  nums = [6, 6, 6, 6, 6, 6, 6]
  target = 5
  actual = solution.search(nums, target)
  assert not actual


def test_search8():
  nums = [2, 5, 6, 0, 0, 1, 2]
  target = 1
  actual = solution.search(nums, target)
  assert actual
