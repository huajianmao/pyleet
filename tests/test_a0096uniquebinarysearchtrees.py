from solutions.a0096uniquebinarysearchtrees import Solution

solution = Solution()


def test_numTrees1():
  n = 3
  expect = 5
  actual = solution.numTrees(n)
  assert actual == expect
