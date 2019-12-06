from solutions.a0131palindromepartitioning import Solution

solution = Solution()


def test_partition1():
  s = "aab"
  expect = [
    ["aa", "b"],
    ["a", "a", "b"]
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition2():
  s = ""
  expect = [
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition3():
  s = "ac"
  expect = [
    ['a', 'c']
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition4():
  s = "aa"
  expect = [
    ['a', 'a'],
    ['aa']
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition5():
  s = "aba"
  expect = [
    ['a', 'b', 'a'],
    ['aba']
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition6():
  s = "aaa"
  expect = [
    ['a', 'a', 'a'],
    ['a', 'aa'],
    ['aa', 'a'],
    ['aaa'],
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)


def test_partition7():
  s = "abcdeabba"
  expect = [
    ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'b', 'a'],
    ['a', 'b', 'c', 'd', 'e', 'a', 'bb', 'a'],
    ['a', 'b', 'c', 'd', 'e', 'abba']
  ]
  actual = solution.partition(s)
  assert sorted(actual) == sorted(expect)
