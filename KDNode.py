# Class name: KDNode
# Instance Variables: left (left child of node)
#                     right (right child of node)
#                     parent (parent of node)
#                     point (Point stored at node)
# Description: Implements KDNode class
# Methods: constructor taking in point parameter

class KDNode:
    def __init__(self, NodePoint):
        self.left = None
        self.right = None
        self.parent = None
        self.point = NodePoint
