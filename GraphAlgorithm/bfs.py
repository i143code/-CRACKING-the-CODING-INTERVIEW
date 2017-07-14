class Node(object):
    def __init__(self,data):
        self.data = data
        self.adjacent = []
        self.visited = False

# BFS uses Queue
class BreadthFirstSearch(object):
    def bfs(self,Startnode):
        queue =[]
        queue.append(Startnode)
        Startnode.visited = True

        # loop until queue is empty
        while queue:
            # FIFO
            actual_data = queue.pop(0)
            print(actual_data.data)
            for n in actual_data.adjacent:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

node1.adjacent.append(node2)
node1.adjacent.append(node5)
node1.adjacent.append(node4)
node2.adjacent.append(node3)
node2.adjacent.append(node6)

bfs = BreadthFirstSearch()
bfs.bfs(node1)

