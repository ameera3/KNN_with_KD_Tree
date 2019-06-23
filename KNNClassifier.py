# This program takes in 4 command line arguments and outputs a file called
# "result.txt". The first command line argument is the choice of k in KNN
# (number of nearest neighbors). The second is the name of the training
# data file. The third is the name of input data file. The fourth is a
# flag which is either "validation" or "test".
# Usage: python3 KNNClassifier.py -k 3 -t ./training -i ./input -m test

import argparse
from Point import Point
from KDT import KDT

# Read the data from file and convert them to vector of points.
# Each line of the file contains data in each dimension of the
# features (and potentially label) of one data point.
# The boolean withLabel indicates if the last value in a line
# is a label of the data point.

def readData(fileName, withLabel):

    f = open(fileName, 'r')

    # read the data and convert them to data points
    result = []
    for line in f:
        features = []
        for t in line.split():
            try:
                features.append(float(t))
            except ValueError:
                pass
        if features == []:
            continue
        if withLabel:
            label = features.pop()
        else:
            label = 0
        linePoint = Point(features, label)
        result.append(linePoint)

    f.close()
    return result

# Find the most frequent label in the given set of points
# Scan through the vector once searching for the max and
# min labels. Scan through the vector again incrementing
# the count of each label. Scan through the vector again
# to find the label with the maximum count.

def mostFreqLabel(points : [Point]):

    minLabel = float("inf")
    maxLabel = float("-inf")

    for i in range(len(points)):
        if (points[i]).classification < minLabel:
            minLabel = int((points[i]).classification)
        if (points[i]).classification > maxLabel:
            maxLabel = int((points[i]).classification)

    histSize = int(maxLabel - minLabel + 1)
    histogram = [0 for i in range(histSize)]

    for i in range(len(points)):
        histogram[int((points[i]).classification - minLabel)] += 1

    maxCount = 0
    maxIndex = 0
    for i in range(histSize):
        if histogram[i] > maxCount:
            maxCount = histogram[i]
            maxIndex = i

    return int(maxIndex+minLabel)


# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--k", help="number of nearest neighbors")
ap.add_argument("-t", "--training", help="name of training data file")
ap.add_argument("-i", "--input", help="input data file")
ap.add_argument("-m", "--mode", help="validation or test mode")
args = vars(ap.parse_args())

k = int(args["k"])
training = args["training"]
inputData = args["input"]
mode = args["mode"]

# read the training data file and build the KDT
trainingList = readData(training, True)
tree = KDT()
tree.build(trainingList)

# If the fourth parameter is validation, the input data file should
# have the same format as training data file. In this case we are trying
# to use input data file as validation data and find the validation error.
# We predict a label for a point by using the most frequent label of its
# k nearest neighbors. We count the number of times our classifier has
# made a "label mismatch" mistake. "Label mismatch" mistake means that
# after training the classifier using training data file, our predicted
# label for a point is different from the actual label for this point
# from the input data file. Validation error value is the number of
# label mismatch mistakes divided by the size of data input.

if mode == "validation":
    errorCount = 0
    inputList = readData(inputData, True)
    for i in range(len(inputList)):
        queryPoint = inputList[i]
        kNearest = tree.findKNearestNeighbors(queryPoint, k)
        kNearestPoints = [kNearest[i][0] for i in range(len(kNearest))]
        label = mostFreqLabel( kNearestPoints )
        if label != queryPoint.classification:
            errorCount += 1
    errorPercent = errorCount/len(inputList)

    # Your output file should contain the value of K and its corresponding
    # validation error. */
    out = open("./result.txt", "a")
    out.write("K: " + str(k) +  ", Validation Error: " + str(errorPercent) + "\n")
    out.close()

# If the fourth argument is test, each line of the input data file should
# contain only the features of this data, no label following. In this case
# we are trying to use input data file as test data and find the k nearest
# neighbors of data in each line of the input file. The predicted label is
# the most frequent label of the k nearest neighbors.

if mode == "test":
    inputList = readData(inputData, False)
    out = open("./result.txt", "a")

    # Each line of your output file should contain the predicted label for
    # the data in the corresponding line of input data file.
    for i in range(len(inputList)):
        queryPoint = inputList[i]
        kNearest = tree.findKNearestNeighbors(queryPoint, k)
        kNearestPoints = [kNearest[j][0] for j in range(len(kNearest))]
        label = mostFreqLabel( kNearestPoints )
        out.write(str(label) + '\n')

    out.close()

