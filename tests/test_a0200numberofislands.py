from solutions.a0200numberofislands import Solution

solution = Solution()


def test_numIslands1():
  grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
  ]
  expect = 1
  actual = solution.numIslands(grid)
  assert actual == expect


def test_numIslands2():
  grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
  ]
  expect = 3
  actual = solution.numIslands(grid)
  assert actual == expect
