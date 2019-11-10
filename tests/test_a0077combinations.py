from solutions.a0077combinations import Solution

solution = Solution()


def sortCombine(items):
  items.sort()
  for it in items:
    it.sort()


def test_combine():
  n = 4
  k = 2
  expect = [
    [2, 4],
    [3, 4],
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 4],
  ]
  acutal = solution.combine(n, k)
  sortCombine(expect)
  sortCombine(acutal)
  assert acutal == expect
