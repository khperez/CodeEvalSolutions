fname = raw_input("Enter file name:")
if (len(fname) < 1):
    fname = "testcases.txt"

test_cases = open(fname)

dotCount = 0
testCount = 1

for test in test_cases:
    minCount = 10
    list = test.split(",")
    for item in list:
        dotCount = item.count('.')
        print dotCount
        if dotCount <= minCount :
            minCount = dotCount
    print ("Min Count for Test Case #%d = %d" % (testCount , minCount))

    print minCount

    print ("----End of Test Case #%d----" % testCount)

    testCount += 1
