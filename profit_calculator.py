#!/usr/bin/env python

import sys

rate = float(sys.argv[1])
end = int(sys.argv[2])
increment = int(sys.argv[3])

for capital in range(0, end, increment):
    balance = capital * rate
    profit = balance - capital
    print "Profit = %s (Capital = %s)" % (profit, capital)
