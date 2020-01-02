from solutions.a0166fractiontorecurringdecimal import Solution

solution = Solution()


def test_fractionToDecimal1():
  numerator = 1
  denominator = 2
  expect = "0.5"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal2():
  numerator = 2
  denominator = 1
  expect = "2"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal3():
  numerator = 2
  denominator = 3
  expect = "0.(6)"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal4():
  numerator = 1
  denominator = 8
  expect = "0.125"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal5():
  numerator = 1
  denominator = 16
  expect = "0.0625"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal6():
  numerator = 1
  denominator = 13
  expect = "0.(076923)"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal7():
  numerator = 1
  denominator = 6
  expect = "0.1(6)"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect


def test_fractionToDecimal8():
  numerator = 1
  denominator = 12
  expect = "0.08(3)"
  actual = solution.fractionToDecimal(numerator, denominator)
  assert actual == expect
