import os
import csv
from collections import defaultdict, namedtuple, Counter, deque

data = []

Record = namedtuple(
    'Record',
    'nature,type,suburb'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'merged_data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    record = Record(
        **row
    )

    return record


def safest_suburbs():
    suburbs = []
    for record in data:
        suburbs.append(record.suburb)

    return Counter(suburbs).most_common()[:-5-1:-1]


def sickest_suburbs():
    suburbs = []
    for record in data:
        suburbs.append(record.suburb)

    return Counter(suburbs).most_common(5)
