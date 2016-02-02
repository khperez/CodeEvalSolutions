fname = raw_input("Enter file name:")
if (len(fname) < 1):
    fname = "testcases_large.txt"

test_cases = open(fname)

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
            if count == 0 or count < minCount:
                minCount = count
    print minCount
