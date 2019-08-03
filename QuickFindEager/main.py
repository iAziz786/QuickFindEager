class QuickFind():
  """
  We provide some list and QuickFind give us the answer
  whether they are connected or not.
  #### Example
  ```
    qks = QuickFind()
    qks.join(2, 4)
    qks.join(4, 8)
    qks.is_connected(2, 8) // True
  ```
  """
  def __init__(self, size):
    """
    @params size: Max size of the array
    """
    self.quick_list = [i for i in range(size)]

  def join(self, node1, node2):
    value = self.quick_list[node2]
    for i in range(len(self.quick_list)):
      if (self.quick_list[i] == value):
        self.quick_list[i] = self.quick_list[node1]
  
  def is_connected(self, first, second):
    """is_connected(first, second) -> bool"""
    return (self.quick_list[first] == self.quick_list[second])
