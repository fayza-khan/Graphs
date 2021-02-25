"""
Given 2 Arrays of Inorder and preorder traversal. Construct a tree and print the Postorder traversal. 

Example 1:

Input:
N = 4
inorder[] = {1 6 8 7}
preorder[] = {1 6 7 8}
Output: 8 7 6 1
Example 2:

Input:
N = 6
inorder[] = {3 1 4 0 5 2}
preorder[] = {0 1 3 4 2 5}
Output: 3 4 1 5 2 0
Explanation: The tree will look like
       0
    /     \
   1       2
 /   \    /
3    4   5
Your Task:
Your task is to complete the function buildTree() which takes 3 arguments(inorder traversal array, 
preorder traversal array, and size of tree n) and returns the postorder of the tree constructed. 

Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(N).

Constraints:
1<=Number of Nodes<=1000
"""


'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
def postorder(node, res):
    if node:
        postorder(node.left, res)
        postorder(node.right, res)
        res.append(node.data)
    
def buildtree(inorder, preorder, n):
    # code here
    # build tree and return root node
    # inorder -> left > root > right
    # preorder -> root > left > right
    # postorder -> left > right > root
    
    def buildutil(ino, pre):
        if not pre or not ino: return None
        if len(pre) == 1: 
            return Node(pre[0])
        r = pre.pop(0)
        root = Node(r)
        ind = ino.index(r)
        root.left = buildutil(ino[:ind],pre)
        root.right = buildutil(ino[ind+1:],pre)
        return root
    head = buildutil(inorder, preorder)
    result = []
    postorder(head, result)
    return result
  
  
    
    
            
    
    

