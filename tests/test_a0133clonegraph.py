from solutions.a0133clonegraph import Solution, Node

solution = Solution()


def test_cloneGraph1():
  node1 = Node(1, [])
  node2 = Node(2, [])
  node3 = Node(3, [])
  node4 = Node(4, [])
  node1.neighbors.append(node2)
  node1.neighbors.append(node4)
  node2.neighbors.append(node1)
  node2.neighbors.append(node3)
  node3.neighbors.append(node2)
  node3.neighbors.append(node4)
  node4.neighbors.append(node3)
  node4.neighbors.append(node1)

  solution.cloneGraph(node1)
