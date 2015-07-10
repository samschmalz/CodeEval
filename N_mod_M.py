import sys
import math
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        continue
    else:
        items = test.split(",")
        n = int(items[0])
        m = int(items[1])
        mod = (n / float(m) - n / m) * m
        mod = math.floor(mod)
        print int(mod)

test_cases.close()
