from solutions.a0134gasstation import Solution

solution = Solution()


def test_canCompleteCircuit1():
  gas = [1, 2, 3, 4, 5]
  cost = [3, 4, 5, 1, 2]
  expect = 3
  actual = solution.canCompleteCircuit(gas, cost)
  assert actual == expect


def test_canCompleteCircuit2():
  gas = [2, 3, 4]
  cost = [3, 4, 3]
  expect = -1
  actual = solution.canCompleteCircuit(gas, cost)
  assert actual == expect
