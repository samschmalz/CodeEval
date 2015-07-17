import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split(" ")
    words.reverse()
    first = words[0]
    first = first[:-1]
    words[0] = first
    final = " ".join(words)
    print final
