from solutions.a0138copylistwithrandompointer import Solution, Node

solution = Solution()


def test_copyRandomList1():
  node2 = Node(2, None, None)
  node2.random = node2
  head = Node(1, node2, node2)
  actual = solution.copyRandomList(head)


def test_copyRandomList2():
  head = None
  actual = solution.copyRandomList(head)
  assert actual == head


def test_copyRandomList3():
  node2 = Node(2, None, None)
  node2.random = node2
  head = Node(1, node2, None)
  actual = solution.copyRandomList(head)
