class Graph:
    def __init__(self):
        self.Nodes = None


class Node:
    def __init__(self):
        self.Name = ''
        self.Children = None
        self.Visited = False

    def __str__(self):
        return 'Name: ' + self.Name + ', was visited: ' + str(self.Visited)


def search(root):
    if root is None:
        return

    print root
    root.Visited = True

    for node in root.Children:
        if node.Visited is False:
            search(node)


def exist_path_between(nodeA, nodeB):
    if nodeA is None:
        return False
    if nodeA == nodeB:
        return True

    print nodeA
    nodeA.Visited = True

    for node in nodeA.Children:
        if node.Visited is False:
            return exist_path_between(node, nodeB)


a = Node()
a.Name = 'A'

b = Node()
b.Name = 'B'

c = Node()
c.Name = 'C'

d = Node()
d.Name = 'D'

a.Children = [b]
b.Children = [c]
c.Children = [d]
d.Children = [b]

# search(b)

print exist_path_between(a,d)

