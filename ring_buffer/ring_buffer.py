class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  """
  A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

  Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.
  """

  def append(self, item):
    # The list starts as a list of None * capacity, so it starts at the length of capacity
    
    # If the element in the current counter is None
      # Remove that element and insert the item in it's position
      # Increment the counter by 1
    # Else if current is equal to the capacity
      # Remove the first item in the list
      # Place the new item in its position
    if self.current == self.capacity:
      self.storage.pop(0)
      self.storage.insert(0, item)
      self.current = 1

    elif self.storage[self.current] is None:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1
    
    else:
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1

  def get(self):
    # Return everything in the buffer in a list
    return_array = list(filter(None, self.storage))
    
    return return_array
    # Does not return any None values that may be there.


# buffer = RingBuffer(5)
# print(f"LINE 39: {len(buffer.storage)}")
# print(f"LINE 35: {buffer.append('a')} - {buffer.current} - {buffer.storage}")
# print(f"LINE 36: {buffer.append('b')} - {buffer.current} - {buffer.storage}")
# print(f"LINE 37: {buffer.append('c')} - {buffer.current} - {buffer.storage}")
# print(f"LINE 38: {buffer.append('d')} - {buffer.current} - {buffer.storage}")
# print(f"LINE 39: {buffer.append('e')} - {buffer.current} - {buffer.storage}")
# print(f"LINE 40: {buffer.append('f')} - {buffer.current} - {buffer.storage}")
# print(buffer.storage)
# print(f"LINE 45: {len(buffer.storage)}")
# print(buffer.get())