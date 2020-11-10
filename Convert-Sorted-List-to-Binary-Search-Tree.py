"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

 A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Example :


Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        arr = []
        while A:
            arr.append(A.val)
            A = A.next
        
        def sortedArrayToBST(nums):
            if not nums:
                return None
            mid= (len(nums))//2
            root = TreeNode(nums[mid])
            root.left= sortedArrayToBST(nums[:mid])
            root.right= sortedArrayToBST(nums[mid+1:])
            return root
        return sortedArrayToBST(arr)
        
