from __future__ import print_function
import sys

counter = 0
for line in sys.stdin:
    counter += 1
    if counter <= 10:
       print(line.strip())

