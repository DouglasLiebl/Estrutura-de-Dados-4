import numpy as np

class NonOrdered:
  def __init__(self, capacity):
    self.capacity = capacity
    self.last_position = -1
    self.values = np.empty(self.capacity, dtype=int)
  
  def show(self):
    if self.last_position == -1:
      print("Empyt List")
      return
    
    for i in range(0, self.last_position + 1):
      print(f"{i} - {self.values[i]}")
  
  """
  def insert(self, value):
    if self.last_position == self.capacity -1: 
      print("Max length reached")
      return
    
    if value in self.values:
      print("Duplicate values aren't accepteds")
      return
    
    self.last_position += 1
    self.values[self.last_position] = value

  """
  def insert(self, value):
    if self.last_position == self.capacity -1: 
      print("Max length reached")
      return
    
    if value in self.values:
      self.exclude(value)
      print("Duplicate values aren't accepteds. Removing same value from list.")
      return
    
    self.last_position += 1
    self.values[self.last_position] = value


  def search(self, value):
    for i in range(0, self.last_position + 1):
      if value == self.values[i]: return i
    return -1

  def exclude(self, value):
    position = self.search(value)
    if position == -1: return -1
    else: 
      for i in range(position, self.last_position):
        self.values[i] = self.values[i + 1]
      
      self.last_position -= 1


list = NonOrdered(10)
list.insert(12)
list.insert(13)
list.insert(12)
list.insert(13)
list.insert(14)
list.search(12)
list.exclude(12)
list.show()