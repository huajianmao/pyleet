from solutions.a0153findminimuminrotatedsortedarray import Solution

solution = Solution()


def test_findMin1():
  nums = [3, 4, 5, 1, 2]
  expect = 1
  actual = solution.findMin(nums)
  assert actual == expect


def test_findMin2():
  nums = [4, 5, 6, 7, 0, 1, 2]
  expect = 0
  actual = solution.findMin(nums)
  assert actual == expect


def test_findMin3():
  nums = [num for num in range(100)]
  expect = 0
  for i in range(100):
    temp = nums[i:100] + nums[:i]
    actual = solution.findMin(temp)
    assert actual == expect
