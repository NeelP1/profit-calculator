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

originalCapital = capital

print "Original Capital: $%s" % capital

for x in range(0, end, increment):
    capital = capital * rate
    profit = capital - originalCapital
    print "Profit = %s (capital = %s)" % (profit, capital)
