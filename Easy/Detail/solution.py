import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    minCount = 10
    list = test.split(",")
    for item in list:
        XY_Pos = item.find("XY")
        if XY_Pos >= 0:
            minCount = 0
        else:
            lastXPos = item.find("X.")
            firstYPos = item.find("Y")
            count = (firstYPos - lastXPos) - 1
            if count < minCount:
                minCount = count
    print minCount

test_cases.close()
