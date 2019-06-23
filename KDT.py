import operator
from operator import itemgetter
from Point import Point
from KDNode import KDNode

# Class name: KDT
# Instance Variables: root (the root of the KDT)
#                     numDim (number of features of nodes in KDT)
#                     k (number of nearest neighbors to find)
#                     threshold (current worst distance to query)
#                     isize (number of nodes in KDT)
#                     iheight (height of KDT)
#                     kNearest (vector holding k nearest neighbors)
# Description: Implements a KDT
# Methods: constructor, build, buildSubtree, findKNearestNeighbors,
#          findKNNHelper, updateKNN, display

class KDT:
    def __init__(self):
        self.root = None
        self.numDim = 0
        self.k = 0
        self.threshold = float('inf')
        self.isize = 0
        self.iheight = 0
        self.kNearest = []

    # Build the KD tree from the given vector of Point references
    # Calls buildSubtree. Sets size of tree

    def build(self, points):
        if points != []:
            self.root = self.buildSubtree(points, 0,
                self.iheight)
            self.isize = len(points)

    # Helper method to recursively build the subtree of KD tree.
    # Sort points. Find median. Construct new KDNode and set
    # left and right children to nullptr. If new KDNode is a leaf,
    # incremement height. Otherwise, call buildSubtree recursively
    # on left and right child as appropriate

    def buildSubtree(self, points, d, height):
        sortedPoints = sorted(points, key=lambda Point:
            Point.featuresList[d])
        mid = len(sortedPoints)//2

        p = KDNode(sortedPoints[mid])
        p.left = None
        p.right = None

        if len(sortedPoints) == 1:
            if height > self.iheight:
                self.iheight = height

        else:
            d = (d + 1) % (p.point).numDim
            if 0 < mid:
                p.left = self.buildSubtree(sortedPoints[0:mid],
                    d, height+1)
            if mid+1 < len(sortedPoints):
                p.right = self.buildSubtree(sortedPoints[mid+1:len(sortedPoints)], d, height+1)

        return p

    # Used for printing a KDT

    def display(self):
        self.inorder(self.root)

    # Recursive inorder traversal 'helper' function
    # If current node is null, return.
    # Recursively traverse left subtree
    # Print current node data
    # Recursively traverse right subtree

    def inorder(self, working):
        if working != None:
            self.inorder(working.left)
            print(working.point.featuresList)
            self.inorder(working.right)

    def findKNearestNeighbors(self, queryPoint, k):
        self.kNearest = []
        self.k = k
        self.threshold = float('inf')
        self.findKNNHelper(self.root, queryPoint, 0)
        return self.kNearest

    # Helper method to recursively find the K nearest neighbors
    # If current node is nullptr, return. Otherwise, set the
    # square distance to query point. If square distance is less
    # than threshold, call updateKNN to see if point should be
    # inserted into kNearest. Find square distance from node to
    # query along current dimension. If this distance is greater
    # than 0, explore the left child, otherwise explore the right
    # child. If square distance is at least the threshold, do not
    # explore other child. Otherwise, explore other child.

    def findKNNHelper(self, node, queryPoint, d):
        if node != None:
            (node.point).setSquareDistToQuery(queryPoint)
            distPQ = (node.point).squareDistToQuery
            if distPQ < self.threshold:
                self.updateKNN(node.point, distPQ)
            dx = (node.point).featuresList[d] - queryPoint.featuresList[d]
            dx2 = dx**2
            d = (d+1) % (node.point).numDim
            self.findKNNHelper(node.left if dx > 0 else node.right, queryPoint, d)
            if dx2 < self.threshold:
                self.findKNNHelper(node.right if dx > 0 else node.left, queryPoint, d)

    # Helper method to update your data structure storing KNN using
    # the given point. If kNearest has size less than k, insert point
    # and its distance into kNearest. Otherwise, find the point in
    # kNearest with maximum distance from the query point
    # and set threshold equal to this distance. If point has distance
    # less than threshold to query, then insert this point into
    # kNearest and remove the point with the maximum distance. Update
    # threshold.

    def updateKNN(self, myPoint, distPQ):
        if len(self.kNearest) < self.k:
            self.kNearest.append( (myPoint,distPQ) )
        else:
            self.kNearest.sort(key=itemgetter(1))
            self.threshold = self.kNearest[-1][1]
            if distPQ < self.threshold:
                self.kNearest.pop(-1)
                self.kNearest.append( (myPoint, distPQ) )
                self.kNearest.sort(key=itemgetter(1))
                self.threshold = self.kNearest[-1][1]
