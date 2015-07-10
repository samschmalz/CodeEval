import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        continue
    else:
        sum = 0
        test = int(test)
        while test != 0:
            sum += test % 10
            test /= 10
        print sum

test_cases.close()
