# -*- coding: utf-8 -*-

import os
import fnmatch
import fileinput
import json
import re
import urllib.request


def getTestsCount():
  testDir = "tests"
  testFilePattern = r'test_a*.py'
  count = 0
  for file in fnmatch.filter(os.listdir(testDir), testFilePattern):
    if file == 'test_a0000blank.py':
      continue
    testFile = os.path.join(testDir, file)
    text = open(testFile, "r")
    for line in text:
      if re.match("def test_*", line):
        count += 1
  return count


def getSolutionsCount():
  dirpath = "solutions"
  pattern = r'a*.py'
  solutions = [solution for solution in fnmatch.filter(os.listdir(dirpath), pattern) if solution != 'a0000blank.py']
  return len(solutions)


def getAlgorithmsCount():
  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/78.0.3904.97 Safari/537.366'
  }
  url = "https://leetcode.com/api/problems/algorithms/"
  request = urllib.request.Request(url=url, headers=headers)
  response = urllib.request.urlopen(request)
  obj = json.loads(response.read().decode('utf-8'))
  return obj['num_total']


def updateReadme(solutions, tests, total):
  file = "README.md"
  if total > 1000:
    print("Progress: " + str(solutions) + " / " + str(total))
    ratio = solutions / total
    if ratio > 0.8:
      color = 'success'
    elif ratio > 0.5:
      color = 'important'
    else:
      color = 'critical'

    newStatus = 'Progress-' + str(solutions) + '%2F' + str(total) + '-' + color + '.svg'
    testStatus = 'Tests-' + str(tests) + '-' + 'success.svg'
    with fileinput.FileInput(file, inplace=True) as file:
      for line in file:
        line = re.sub(r"Progress\-\d+\%2F\d+\-.+\.svg", newStatus, line)
        line = re.sub(r"Tests\-\d+\-.+\.svg", testStatus, line)
        print(line, end='')

  else:
    print("FIXME: some error occurs!!!")


tests = getTestsCount()
solutions = getSolutionsCount()
total = getAlgorithmsCount()
updateReadme(solutions, tests, total)
