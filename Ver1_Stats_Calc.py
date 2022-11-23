numPoints = int(input("# of data points: "))
print()
set1 = []

for i in range(1, numPoints+1):
    if i == 1:
        set1.append(float(input(f"{i}st x-value: "))) 
    elif i == 2:
        set1.append(float(input(f"{i}nd x-value: ")))
    elif i == 3:
        set1.append(float(input(f"{i}rd x-value: ")))
    else:
        set1.append(float(input(f"{i}th x-value: ")))
print()

mean_x = sum(set1)/numPoints
set2 = []

for i in range(1, numPoints+1):
    if i == 1:
        set2.append(float(input(f"{i}st y-value: "))) 
    elif i == 2:
        set2.append(float(input(f"{i}nd y-value: ")))
    elif i == 3:
        set2.append(float(input(f"{i}rd y-value: ")))
    else:
        set2.append(float(input(f"{i}th y-value: ")))

mean_y = sum(set2)/numPoints
meansDiff = 0
xMeanSq = 0

for i in range(numPoints):
    meansDiff += (set1[i]-mean_x)*(set2[i]-mean_y)
    xMeanSq += (set1[i]-mean_x)**2

lineSlope = meansDiff/xMeanSq
lineIntercept = mean_y-lineSlope*mean_x

def lbfVal(inp):
    return lineSlope*inp + lineIntercept

varCount = 0
avgDiffSq = 0
yMeanSq = 0

for i in range(numPoints):
    avgDiffSq += (set2[i]-lbfVal(set1[i]))**2
    yMeanSq += (set2[i]-mean_y)**2

corrCoeff = meansDiff/((xMeanSq*yMeanSq)**0.5)
rSquared = 1 - avgDiffSq/yMeanSq
rmse = (meansDiff/numPoints)**0.5

print()
print(f"Correlation coefficient: {corrCoeff}")
print(f"Line of best fit: \x1B[3my\x1B[0m = {lineSlope}\x1B[3mx\x1B[0m + {lineIntercept}")
print(f"R squared: {rSquared}")
print(f"RMSE: {rmse}")


