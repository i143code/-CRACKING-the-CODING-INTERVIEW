# Floyd’s Cycle-Finding Algorithm:
class Node(object):
  def __init__(self,data):
    self.data = data
    self.nextNode = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
    
  # push data 
  def push(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head= self.tail = new_node
    else:
      new_node.nextNode = self.head
      self.head = new_node
  
  # print data
  def printAll(self):
    current = self.head 
    while current:
      print(current.data)
      current = current.nextNode
  
  # detect 
  def detectLoop(self):
    p1 = self.head
    p2 = self.head
    
    while p1 != None and p1.nextNode != None:
      p1 = p1.nextNode.nextNode
      p2 = p2.nextNode
      
      if p1 == p2:
        print(p1.data)
        return True
        
    return False

# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
# Create a loop for testing
llist.head.nextNode.nextNode.nextNode.nextNode = llist.head
print(llist.detectLoop())
# print(llist.printAll())
