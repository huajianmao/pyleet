from solutions.a0210coursescheduleii import Solution

solution = Solution()


def test_canFinish1():
  numCourses = 2
  prerequisites = [[1, 0]]
  expect = [[0, 1]]
  actual = solution.findOrder(numCourses, prerequisites)
  assert actual in expect


def test_canFinish2():
  numCourses = 4
  prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
  expect = [[0, 1, 2, 3], [0, 2, 1, 3]]
  actual = solution.findOrder(numCourses, prerequisites)
  assert actual in expect


def test_canFinish3():
  numCourses = 4
  prerequisites = [[1, 0]]
  expect = [[2, 3, 0, 1], [0, 2, 3, 1], [3, 0, 2, 1]]
  actual = solution.findOrder(numCourses, prerequisites)
  assert actual in expect


def test_canFinish4():
  numCourses = 2
  prerequisites = [[1, 0], [0, 1]]
  expect = [[]]
  actual = solution.findOrder(numCourses, prerequisites)
  assert actual in expect
