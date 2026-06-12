# A QTreePartition is just a rectangle described by its top left corner and its size
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
        self.points = []
    
    def contains_point(self, point):
        x_max = self.partition.x + self.partition.w
        x_min = self.partition.x
        y_max = self.partition.y + self.partition.h
        y_min = self.partition.y
        contains_x = point[0] < x_max and point[0] >= x_min
        contains_y = point[1] < y_max and point[1] >= y_min
        return contains_x and contains_y

    def insert(self, point):
        if self.contains_point(point):
            self.points.append(point)
            if len(self.children) == 0:
                self.subdivide()
            for child in self.children:
                if child.contains_point(point):
                    child.insert(point)

    def subdivide(self):
        north_west_partition = QTreePartition(self.partition.x, self.partition.y, self.partition.w / 2, self.partition.h / 2)
        self.children.append(PointQTreeNode(north_west_partition))

        south_west_partition = QTreePartition(self.partition.x, self.partition.y + self.partition.h / 2, self.partition.w / 2, self.partition.h / 2)
        self.children.append(PointQTreeNode(south_west_partition))

        south_east_partition = QTreePartition(self.partition.x + self.partition.w / 2, self.partition.y + self.partition.h / 2, self.partition.w / 2, self.partition.h / 2)
        self.children.append(PointQTreeNode(south_east_partition))

        north_east_partition = QTreePartition(self.partition.x + self.partition.w / 2, self.partition.y, self.partition.w / 2, self.partition.h / 2)
        self.children.append(PointQTreeNode(north_east_partition))
