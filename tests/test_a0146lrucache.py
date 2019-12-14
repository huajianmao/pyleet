from solutions.a0146lrucache import LRUCache


def test_lrucache1():
  cache = LRUCache(2)
  cache.put(1, 1)
  cache.put(2, 2)
  assert cache.get(1) == 1
  cache.put(3, 3)
  assert cache.get(2) == -1
  cache.put(4, 4)
  assert cache.get(1) == -1
  assert cache.get(3) == 3
  assert cache.get(4) == 4


def test_lrucache2():
  cache = LRUCache(2)
  assert cache.get(2) == -1
  cache.put(2, 6)
  assert cache.get(1) == -1
  cache.put(1, 5)
  cache.put(1, 2)
  assert cache.get(1) == 2
  assert cache.get(2) == 6


def test_lrucache2():
  cache = LRUCache(2)
  cache.put(2, 1)
  cache.put(1, 1)
  cache.put(2, 3)
  cache.put(4, 1)
  assert cache.get(1) == -1
  assert cache.get(2) == 3
