# -*- coding: utf-8 -*-

################################################
#
# URL:
# =====
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# DESC:
# =====
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
#
# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node, just like in Figure B.
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
#
# Constraints:
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000
#
################################################


class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if not root:
      return None

    cur = root
    next = root.left
    while cur.left:
      cur.left.next = cur.right
      if cur.next:
        cur.right.next = cur.next.left
        cur = cur.next
      else:
        cur = next
        next = cur.left

    return root
