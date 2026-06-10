# A QTreePartition is just a rectangle described by its center and its half extents
class QTreePartition:
    def __init__(self,x, y, w, h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;

class PointQTreeNode:
    def __init__(self, partition):
        self.children = [] # list of QTreeNodes
        self.level = 0
        self.partition = partition

    def subdivide(self):
        pass

def build_point_qtree(points):
    root = PointQTreeNode(QTreePartition(0,0,0,0))
    return root
