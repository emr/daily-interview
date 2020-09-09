class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(node, k, floor=None, ceil=None):
  if node.value == k - 1:
    floor = k - 1
  if node.value == k:
    ceil = k
  if node.value == k + 1:
    ceil = k + 1
  if node.left != None:
    (floor, ceil) = findCeilingFloor(node.left, k, floor, ceil)
  if node.right != None:
    (floor, ceil) = findCeilingFloor(node.right, k, floor, ceil)
 
  return [floor, ceil]

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
print(findCeilingFloor(root, 11))
# (10, 12)
