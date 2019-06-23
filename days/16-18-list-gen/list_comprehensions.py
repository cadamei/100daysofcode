"""
Copied from here https://github.com/pybites/100DaysOfCode/blob/master/023/harry.py
"""

#!python3

from collections import Counter
from string import punctuation, whitespace
import calendar
import itertools
import random
import re
import requests
import sys
import nltk
from nltk.corpus import stopwords


resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))

print(f'Is the dash in words?: {"-" in words}')

words = [re.sub(r'\W+', r'', word) for word in words]
wordsp = [word.translate(str.maketrans('', '', punctuation)) for word in words]

print(wordsp[:5])
print(f'Is the dash in words?: {"-" in wordsp}')


words = [word for word in words if word.strip() and word not in stop_words]
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))
