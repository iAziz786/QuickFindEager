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
  
  def root(self, node):
    while node != self.quick_list[node]:
      node = self.quick_list[node]
    return node

  def join(self, node1, node2):
    root_of_node1 = self.root(node1)
    root_of_node2 = self.root(node2)
    self.quick_list[root_of_node1] = self.quick_list[root_of_node2]
  
  def is_connected(self, first, second):
    """is_connected(first, second) -> bool"""
    return (self.root(first) == self.root(second))
