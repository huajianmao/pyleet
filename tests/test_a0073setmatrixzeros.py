from solutions.a0073setmatrixzeros import Solution
import json


solution = Solution()


def test_setZeros1():
  matrix = json.loads("""
  [
    [1,1,1],
    [1,0,1],
    [1,1,1]
  ]
  """)
  expect = json.loads("""
  [
    [1,0,1],
    [0,0,0],
    [1,0,1]
  ]
  """)
  solution.setZeroes(matrix)
  assert matrix == expect


def test_setZeros2():
  matrix = json.loads("""
  [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
  ]
  """)
  expect = json.loads("""
  [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
  ]
  """)
  solution.setZeroes(matrix)
  assert matrix == expect
