"""
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        l = {}
        
        def dist(x, level):
            if level in l:
                l[level].append(x.val)
            else:
                l[level] = [x.val]
            if x.left is not None:
                dist(x.left, level+1)
            if x.right is not None:
                dist(x.right, level+1)
                
        dist(A, 0)
        return l.values()
