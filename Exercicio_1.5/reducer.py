#!/usr/bin/python

import sys

totalSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    _, thisSale = data_mapped
    totalSales += float(thisSale)

print("total"+"\t"+str(totalSales))
