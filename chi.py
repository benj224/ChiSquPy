from scipy.stats import chisquare

rows = int(input("input the number of rows"))
cols = int(input("input the number of columns"))

data = []
for i in range(rows):
    row = []
    for j in range(cols):
        inputStr = "input data for row ", i, " column ", j, ":"
        entry = float(input(inputStr))
        row.append(entry)
    data.append(row)
print(data)

rowTotals = []
for i in range(rows):
    rowToat = 0
    for j in range(cols):
        rowToat += data[i][j]
    rowTotals.append(rowToat)

colTotals = []
for j in range(cols):
    colToat = 0
    for i in range(rows):
        colToat += data[i][j]
    colTotals.append(colToat)

totalSum = 0
for i in rowTotals:
    totalSum += i

##print(len(rowTotals))
##print(len(rowTotals))
expectedData = []
for i in range(rows):
    newExpectedDataRow = []
    for j in range(cols):
        print(j)
        newData = (rowTotals[i]*colTotals[j])/totalSum
        newExpectedDataRow.append(newData)
    expectedData.append(newExpectedDataRow)

if rows == 2 and cols == 2:
    chiData = []
    chiSqu = 0
    for i in range(rows):
        for j in range(cols):
            chi1 = data[i][j] - expectedData[i][j]
            if chi1 < 0:
                chi1 = chi1*-1
            chiData[i][j] = ((chi1-0.5)**2)/expectedData[i][j]
            chiSqu += chiData[i][j]

else:
    chiData = []
    chiSqu = 0
    for i in range(rows):
        chiRow = []
        for j in range(cols):
            chi1 = data[i][j] - expectedData[i][j]
            chiRow.append((chi1**2)/expectedData[i][j])
            chiSqu += (chi1**2)/expectedData[i][j]
        chiData.append(chiRow)




print(chiData)
print(chiSqu)