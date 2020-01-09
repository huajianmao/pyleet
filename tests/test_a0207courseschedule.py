from solutions.a0207courseschedule import Solution

solution = Solution()


def test_canFinish1():
  numCourses = 2
  prerequisites = [[1, 0]]
  actual = solution.canFinish(numCourses, prerequisites)
  assert actual


def test_canFinish2():
  numCourses = 2
  prerequisites = [[1, 0], [0, 1]]
  actual = solution.canFinish(numCourses, prerequisites)
  assert not actual


def test_canFinish3():
  numCourses = 4
  prerequisites = [[1, 0], [0, 1], [1, 2], [1, 3]]
  actual = solution.canFinish(numCourses, prerequisites)
  assert not actual
