import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split(" ")
    words = words[::-1]
    final = " ".join(words)
    print final
