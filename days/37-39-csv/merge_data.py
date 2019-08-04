#!python3

import os
import csv
import re


def merge_data():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'data')
    print(file_path)
    with open('merged_data.csv', 'a', encoding='utf-8') as merged:
        for i, filename in enumerate(os.listdir(file_path), 1):
            with open(os.path.join(file_path, filename), 'r', encoding='utf-8') as fin:
                header = fin.readline()
                if i == 1:
                    merged.write(header)
                    merged.write(fin.read())
                else:
                    for line in fin.read():
                        if line.startswith(header):
                            continue
                        else:
                            merged.write(line)


if __name__ == '__main__':
    merge_data()
