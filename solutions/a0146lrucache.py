# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/lru-cache/
#
# DESC:
# =====
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
################################################


class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.entries = {}
    self.head = Node()
    self.tail = Node(prev=self.head)
    self.head.next = self.tail

  def get(self, key: int) -> int:
    if key in self.entries:
      entry = self.entries.get(key)
      self.__remove(entry)

      entry.prev = self.head
      entry.next = self.head.next
      entry.prev.next = entry
      entry.next.prev = entry
      return entry.value
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    entry = None
    if key not in self.entries:
      if len(self.entries) + 1 > self.capacity:
        last = self.tail.prev
        self.__remove(last)
        self.entries.pop(last.key)
      entry = Node(key=key, value=value, prev=self.head, next=self.head.next)
      self.entries[key] = entry
    else:
      entry = self.entries.get(key)
      entry.value = value
      self.__remove(entry)
    entry.prev = self.head
    entry.next = self.head.next
    entry.prev.next = entry
    entry.next.prev = entry

  def __remove(self, entry):
    prev = entry.prev
    next = entry.next
    prev.next = next
    next.prev = prev
    entry.next = None
    entry.prev = None


class Node:
  def __init__(self, key=None, value=None, prev=None, next=None):
    self.key = key
    self.value = value
    self.prev = prev
    self.next = next
