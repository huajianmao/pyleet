from solutions.a0150evaluatereversepolishnotation import Solution

solution = Solution()


def test_evalRPN1():
  tokens = ["2", "1", "+", "3", "*"]
  expect = 9
  actual = solution.evalRPN(tokens)
  assert actual == expect


def test_evalRPN2():
  tokens = ["4", "13", "5", "/", "+"]
  expect = 6
  actual = solution.evalRPN(tokens)
  assert actual == expect


def test_evalRPN3():
  tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
  expect = 22
  actual = solution.evalRPN(tokens)
  assert actual == expect


def test_evalRPN4():
  tokens = ["10", "6", "-"]
  expect = 4
  actual = solution.evalRPN(tokens)
  assert actual == expect
