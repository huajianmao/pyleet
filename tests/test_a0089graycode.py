from solutions.a0089graycode import Solution
import math

solution = Solution()


def isGrayCode(nums, n):
  if len(nums) == pow(2, n) and len(set(nums)) == len(nums):
    for i in range(1, len(nums)):
      value = math.log2(nums[i] ^ nums[i - 1])
      if value != round(value):
        return False
    return True
  else:
    return False


def test_grayCode1():
  for n in range(10):
    actual = solution.grayCode(n)
    assert isGrayCode(actual, n)
