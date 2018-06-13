#!/usr/bin/env python

import sys
import argparse

#TODO: add argsparse module
# parser = argparse.ArgumentParser()
# parser.add_argument("a")
# args = parser.parse_args()

capital = int(sys.argv[1])
rate = float(sys.argv[2])
end = int(sys.argv[3])
increment = int(sys.argv[4])

for capital in range(0, end, increment):
    balance = capital * rate
    profit = balance - capital
    print "Profit = %s (Capital = %s)" % (profit, capital)
