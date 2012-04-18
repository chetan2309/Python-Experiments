'''
Created on Apr 17, 2012

@author: chetan.sharma
'''

class TreeNode(object):
    left, right, data = None, None, 0

    def __init__(self, data=data):
        self.data =  data
        self.right = None
        self.left = None
    
class Tree(object):
    
    def __init__(self):
        self.root = None
    
    def addNode(self, data):
        return TreeNode(data)
    
    def insert(self, root, data):
        if not root:
            return self.addNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    
    def lookup(self, root, data):
        if root == None:
            return  0
        else:
            if root.data == data:
                return 1
            else:
                if data > root.data:
                    return self.lookup(root.right, data)
                else:
                    return self.lookup(root.left, data)
    
    def printTree(self, root):
        # prints the tree path
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print root.data,
            self.printTree(root.right)
            
    def TreeSize(self, root):
        if root == None:
            return 0
        else:
            return self.TreeSize(root.right) + self.TreeSize(root.left) + 1
        
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            # computes the two depths
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            # returns the appropriate depth
            return max(ldepth, rdepth) + 1
        
        
if __name__ == '__main__':
    # create the binary tree
    BTree = Tree()
    # add the root node
    root = BTree.addNode(0)
    # ask the user to insert values
    for i in range(0, 5):
        data = int(raw_input("insert the node value nr %d: " % i))
        # insert values
        BTree.insert(root, data)
    print
    
    BTree.printTree(root)
    print

    print BTree.TreeSize(root)
    print
    
    print BTree.lookup(root, 13)
    print BTree.lookup(root, 5)