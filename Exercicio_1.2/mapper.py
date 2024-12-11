#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6: #If it does not have all 6 elements, the line is discarded.
        continue
    _, _, _, item, cost, _ = data
    print(item+"\t"+cost)
