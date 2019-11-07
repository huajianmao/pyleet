from solutions.a0064minimumpathsum import Solution
import json

solution = Solution()


def test_uniquePaths1():
  grid = json.loads("""
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
  """)
  expect = 7
  actual = solution.minPathSum(grid)
  assert actual == expect


def test_uniquePaths2():
  grid = json.loads("""
    [
      [1]
    ]
  """)
  expect = 1
  actual = solution.minPathSum(grid)
  assert actual == expect
