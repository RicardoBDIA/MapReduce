#!/usr/bin/python

import sys

maxSale = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    _, thisSale = data_mapped
    maxSale = max(maxSale, float(thisSale))

print("max"+"\t"+str(maxSale))
