# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/fraction-to-recurring-decimal/
#
# DESC:
# =====
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
################################################


class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    sign = "" if ((numerator < 0) == (denominator < 0) or numerator == 0) else "-"
    numerator = abs(numerator)
    denominator = abs(denominator)

    integer = sign + str(numerator // denominator)
    remain = numerator % denominator
    if remain == 0:
      return str(integer)

    fraction = []
    remains = {remain: 0}
    while True:
      value = remain * 10
      while value < denominator:
        fraction.append('0')
        value *= 10
      fraction.append(str(value // denominator))
      remain = value % denominator
      if remain == 0:
        return integer + '.' + ''.join(fraction)
      elif remain in remains:
        index = remains[remain]
        fraction.insert(index, '(')
        return integer + '.' + ''.join(fraction) + ')'
      else:
        remains[remain] = len(fraction)
