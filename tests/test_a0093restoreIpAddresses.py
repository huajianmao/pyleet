from solutions.a0093restoreipaddresses import Solution

solution = Solution()


def test_restoreIpAddresses1():
  s = "25525511135"
  expect = ["255.255.11.135", "255.255.111.35"]
  actual = solution.restoreIpAddresses(s)
  assert sorted(actual) == sorted(expect)


def test_restoreIpAddresses2():
  s = "255255255255"
  expect = ["255.255.255.255"]
  actual = solution.restoreIpAddresses(s)
  assert sorted(actual) == sorted(expect)


def test_restoreIpAddresses3():
  s = "255255255256"
  expect = []
  actual = solution.restoreIpAddresses(s)
  assert sorted(actual) == sorted(expect)


def test_restoreIpAddresses4():
  s = "555111111111"
  expect = []
  actual = solution.restoreIpAddresses(s)
  assert sorted(actual) == sorted(expect)


def test_restoreIpAddresses5():
  s = "0000"
  expect = ["0.0.0.0"]
  actual = solution.restoreIpAddresses(s)
  assert sorted(actual) == sorted(expect)
