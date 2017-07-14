# oute Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
class Node(object):
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.adjacent = []

class BreadthFirstSearch(object):
    def bfs(self,node):
        queue = []
        queue.append(node)
        node.visited = True
        while queue:
            data = queue.pop(0)
            print(data.data)
            for n in data.adjacent:
                if not n.visited:
                    n.visited = True
                    queue.append(n)
        
    # solution 
    def bfssolution(self,node1,node2):
        queue=[]
        queue.append(node1)
        node1.visited= True
        # node2.visited = True

        while queue:
            data = queue.pop(0)
            if data == node2:
              print("There is a path from", node1.data,"to",node2.data)
              return True
            for n in data.adjacent:
                if n is node2:
                    n.visited = True
                    queue.append(n)
        print("There is no path from", node1.data,"to",node2.data)            
        return False

# Test
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

node1.adjacent.append(node2)
node1.adjacent.append(node3)
node1.adjacent.append(node4)
node2.adjacent.append(node5)
node2.adjacent.append(node6)

bfs = BreadthFirstSearch()
# bfs.bfs(node1)


print(bfs.bfssolution(node1,node6))