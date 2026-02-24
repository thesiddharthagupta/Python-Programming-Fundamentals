import math

# List of response times
responseTimes = [245, 312, 189, 276, 298, 234, 389, 267, 301, 223]

# ----- MEAN -----
total = sum(responseTimes)          # add all numbers
count = len(responseTimes)          # how many values
mean = total / count               # average

# ----- STANDARD DEVIATION -----
sumSquare = 0

for t in responseTimes:
    diff = t - mean                # difference from mean
    sumSquare += diff ** 2             # square and add

std = math.sqrt(sumSquare / count)     # divide and square root

# ----- OUTPUT -----
print("Mean:", round(mean, 2))
print("Standard Deviation:", round(std, 2))     #for the round to 2nd dicimal point value
