from solutions.a0187repeateddnasequences import Solution

solution = Solution()


def test_findRepeatedDnaSequences1():
  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  expect = ["AAAAACCCCC", "CCCCCAAAAA"]
  actual = solution.findRepeatedDnaSequences(s)
  assert sorted(actual) == sorted(expect)


def test_findRepeatedDnaSequences2():
  s = "AAAAAAAAAAA"
  expect = ["AAAAAAAAAA"]
  actual = solution.findRepeatedDnaSequences(s)
  assert sorted(actual) == sorted(expect)
