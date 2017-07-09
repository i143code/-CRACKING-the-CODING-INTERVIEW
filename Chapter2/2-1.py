class Node(object):
  def __init__(self,data):
    self.data = data
    self.nextNode = None  

class LinkedList(object):
  head = None
  tail = None
  
  # insert at end
  def InsertAtEnd(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      self.tail.nextNode = new_node
      self.tail = new_node
  
  # print 
  def traverse(self):
    current = self.head
    
    while current != None:
      print(current.data)
      current = current.nextNode
  
  # 2.1 remove duplicates
  
  def deleteDups(self):
    if self.head  != None:
      current = self.head
      seen = {current.data :True}
      while current.nextNode != None:
        # data seen in hash 
        if current.nextNode.data in seen:
          current.nextNode = current.nextNode.nextNode
        
        # else data not seen in hash
        else:
          seen[current.nextNode.data] = True
          current = current.nextNode
      


      
a = LinkedList()
a.InsertAtEnd(1)
a.InsertAtEnd(1)
a.InsertAtEnd(3)
a.InsertAtEnd(4)
print(a.traverse())
# a.deleteDups()
a.deleteDups()
print(a.traverse())