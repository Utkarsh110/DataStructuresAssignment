def findMaximumValue(file):

    inputFile = open(file, "r")
    lines = inputFile.readlines()

    intervalsInput = []

    for line in lines[1:]:
        intervalsSplitInput = line.split(' ')
        intervalsInput.append([int(intervalsSplitInput[0]), int(intervalsSplitInput[1])])

    #Sorting the intervals for easy finding of overlap
    intervalsInput.sort(key=lambda x: (x[0], x[1]))

    maxVal = 0
    for i in range(0,len(intervalsInput)):
        intervals = [intervalsI for intervalsI in intervalsInput]
        
        # Remove one guard and calculate the total shift, then take the maximum.
        intervals.pop(i)

        lastVal = 0
        for interval in intervals:
            if interval[0] > intervals[lastVal][1]:
                lastVal += 1
                intervals[lastVal] = interval
            else:
                intervals[lastVal] = (intervals[lastVal][0], interval[1])

        intervalsCoverage = [ intervalsCoverage[1] - intervalsCoverage[0] for intervalsCoverage in intervals[:lastVal+1]]
        
        maxVal = max(sum(intervalsCoverage),maxVal)

    #Write the maximum value in the file
    outputFile = file.replace('.in','.out')
    fw = open(outputFile, "w")
    fw.write(str(maxVal))
    fw.close()

for i in range(1,11):
    findMaximumValue(str(i)+'.in')







