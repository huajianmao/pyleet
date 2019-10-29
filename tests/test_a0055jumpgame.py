from solutions.a0055jumpgame import Solution

solution = Solution()


def test_canJump1():
  nums = [2, 3, 1, 1, 4]
  acutal = solution.canJump(nums)
  assert acutal


def test_canJump2():
  nums = [3, 2, 1, 0, 4]
  acutal = solution.canJump(nums)
  assert not acutal


def test_canJump3():
  nums = [1, 1, 1, 1]
  acutal = solution.canJump(nums)
  assert acutal


def test_canJump4():
  nums = [0]
  acutal = solution.canJump(nums)
  assert acutal
