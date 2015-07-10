import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        continue
    else:
        sum = 0
        for letter in test:
            num = int(letter)
            sum += num
        print sum

test_cases.close()
