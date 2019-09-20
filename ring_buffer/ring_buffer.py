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
    # If the current amount of items is the capacity
    if self.current == self.capacity:
      # Delete the oldest item in the buffer
      self.storage.pop(0)
      # Decrement the counter by 1
      self.current -= 1

      self.storage.insert(0, item)
      return
    # Add the new element to the storage
    self.storage.append(item)
    # Increment the counter by 1
    self.current += 1

  def get(self):
    # Return everything in the buffer in a list
    return_array = []
    for item in self.storage:
      print(item)
      if item is not None:
        return_array.append(item)
    
    return return_array
    # Does not return any None values that may be there.