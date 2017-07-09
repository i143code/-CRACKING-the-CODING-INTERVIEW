# Walk one pointer n nodes from the head, this will be the right_point
# Put the other pointer at the head, this will be the left_point
# Walk/traverse the block (both pointers) towards the tail, one node at a time, keeping a distance n between them.
# Once the right_point has hit the tail, we know that the left point is at the target.
  # remove mplement an algorithm to find the kth to last element of a singly linked list.
    def kth_to_last(linkedlist, k):
      p1 = self.head
      p2 = self.head 
      
      for i in range(k-1):
        p1 = p1.nextNode
      
      while p1.nextNode != None:
        p2 = p2.nextNode
        p1 = p1.nextNode
      return p2