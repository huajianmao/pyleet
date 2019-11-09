# -*- coding: utf-8 -*-

import os
import fnmatch
import fileinput
import json
import re
import urllib.request

dirpath = "solutions"
pattern = "a*[!0000blank].py"
done = len(fnmatch.filter(os.listdir(dirpath), pattern))

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
total = obj['num_total']

if total > 1000:
  print("Progress: " + str(done) + " / " + str(total))
  ratio = done / total
  if ratio > 0.8:
    color = 'success'
  elif ratio > 0.5:
    color = 'important'
  else:
    color = 'critical'

  newStatus = 'progress-' + str(done) + '%2F' + str(total) + '-' + color + '.svg'
  with fileinput.FileInput('README.md', inplace=True) as file:
    for line in file:
      line = re.sub(r"progress\-\d+\%2F\d+\-.+\.svg", newStatus, line)
      print(line, end='')
else:
  print("FIXME: some error occurs!!!")
