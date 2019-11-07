from solutions.a0063uniquepathsii import Solution
import json

solution = Solution()


def test_uniquePaths1():
  obstacleGrid = json.loads("""
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
  """)
  expect = 2
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths2():
  obstacleGrid = json.loads("""
    [
      [0,0],
      [0,1],
      [0,0]
    ]
  """)
  expect = 1
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths3():
  obstacleGrid = json.loads("""
    [
      [1]
    ]
  """)
  expect = 0
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths4():
  obstacleGrid = json.loads("""
    [
      [1,0]
    ]
  """)
  expect = 0
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths5():
  obstacleGrid = json.loads("""
    [
      [1],
      [0]
    ]
  """)
  expect = 0
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths6():
  obstacleGrid = json.loads("""
    [
    ]
  """)
  expect = 0
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect


def test_uniquePaths7():
  obstacleGrid = json.loads("""
    [
      []
    ]
  """)
  expect = 0
  actual = solution.uniquePathsWithObstacles(obstacleGrid)
  assert actual == expect
