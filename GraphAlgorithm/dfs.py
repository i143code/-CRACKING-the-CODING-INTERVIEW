class Node(object):
    def __init__(self,data):
        self.data = data
        self.adjacent = []
        self.visited = False

class DeapthFirstSearch(object):
    # recursive
    def dfs(self,node):
        node.visited = True
        print(node.data)

        for n in node.adjacent:
            if not n.visited:
                self.dfs(n)
    # without recursion
    def dfsNoRecursion(self,startData):
        stack =[]
        stack.insert(startData)
        startData.visited = True

        while stack:
            # pop
            actual_data = stack.pop()
            for n in actual_data.adjacent:
                if not n.visited:
                    n.visited = True
                    stack.insert(n)




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

dfs = DeapthFirstSearch()
dfs.dfs(node1)

