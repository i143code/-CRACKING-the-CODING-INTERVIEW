class Stack(object):
  def __init__(self):
    self.list = []
    self.min = []
  
  # push 
  def push(self,data):
    # append the data
      self.list.append(data)
      if len(self.min) ==0 or data <= self.min[-1]:
        self.min.append(data)
  
  # pop 
  def pop(self):
    if len(self.list)==0:
      return None
    data = self.list.pop()
    if data == self.min[-1]:
      self.min.pop()
    return data
    
  # min
  def minimum(self):
    if len(self.min)==0:return None
    data = self.min[-1]
    return data
    
  # PRINT 
  def printAll(self):
    return self.list

s1 = Stack()
s1.push(1) 
s1.push(2) 
s1.push(3) 
s1.push(4) 
s1.push(5) 
# s1.push(n for n in range(1,10))
print(s1.minimum())
print(s1.printAll())