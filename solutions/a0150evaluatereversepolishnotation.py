# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# DESC:
# =====
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid.
# That means the expression would always evaluate to a result and there won't be any divide by zero operation.
#
# Example 1:
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
################################################
from typing import List


class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = -1
    for i in range(len(tokens)):
      if tokens[i] == '+':
        tokens[stack - 1] += tokens[stack]
        stack -= 1
      elif tokens[i] == '-':
        tokens[stack - 1] -= tokens[stack]
        stack -= 1
      elif tokens[i] == '*':
        tokens[stack - 1] *= tokens[stack]
        stack -= 1
      elif tokens[i] == '/':
        tokens[stack - 1] = int(float(tokens[stack - 1]) / tokens[stack])
        stack -= 1
      else:
        stack += 1
        tokens[stack] = int(tokens[i])
    return tokens[stack]
