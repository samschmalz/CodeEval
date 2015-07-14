import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split(" ")
    words = words[::-1]
    final = ""
    for item in words:
        final += item
        final += " "
    final = final[:-1]
    print final
