#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')
contry = "Paris"
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
     # parse the input we got from mapperQ4.py
    words = line.split(',')
    if words[4] == contry:
        print(words[0])