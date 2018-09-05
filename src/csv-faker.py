import argparse
import csv
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rows', metavar='N', type=int, default=10, help='number of rows to generate')
args = parser.parse_args()

rowsWanted = args.rows

reader = csv.reader(sys.stdin, skipinitialspace=True)
headers = next(reader)
rows = list(reader)

newRows = [
    [
        rows[random.randrange(0, len(rows))][colNum]
        for colNum in range(len(headers))
    ]
    for _ in range(rowsWanted)
]

writer = csv.writer(sys.stdout)
writer.writerow(headers)
writer.writerows(newRows)
