# Class name: Point
# Instance Variables: featuresList (list of features of data point)
#                     classification (label of data point)
#                     numDim (number of features)
#                     squareDistToQuery (square Euclidean distance to query)
# Description: Implements Point class
# Methods: constructor, setSquareDistToQuery

class Point:
    def __init__(self, features, label):
        self.featuresList = features
        self.classification = label
        self.numDim = len(features)
        self.squareDistToQuery = 0

    def getClassification(self):
        return self.classification
        
    def setSquareDistToQuery(self, queryPoint):
        squareDistToQuery = 0
        for i in range(self.numDim):
            squareDistToQuery = squareDistToQuery + (self.featuresList[i] - queryPoint.featuresList[i])**2
        self.squareDistToQuery = squareDistToQuery

