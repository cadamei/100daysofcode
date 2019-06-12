"""
Copied from here https://github.com/pybites/100DaysOfCode/blob/master/023/harry.py
"""

#!python3

from collections import Counter
from string import punctuation, whitespace
import sys

try:
    file = sys.argv[1]
except IndexError:
    file = 'words.txt'


with open(file) as f:
    s = f.read()
    words = s.lower().translate(str.maketrans('', '', punctuation))

    print(words)
