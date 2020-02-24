class Node:
    def __init__(self,value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        root = self.root
        current = None
        while(root != None): 
            current = root             
            if(value < root.value):
                root = root.left
            elif(value > root.value):
                root = root.right
        if(current == None):
            self.root = Node(value)
        elif(value < current.value):
            leftChild = Node(value)
            current.left = leftChild
            leftChild.parent = current
        else:
            rightChild = Node(value)
            current.right = rightChild
            rightChild.parent = current
            
    def delete(self,value):
        root = self.root
        duplicateExist = False
        while(root != None): 
            if(value < root.value):
                root = root.left
            elif(value > root.value):
                root = root.right 
            else:
                #node found is a leaf
                if(root.left == None and root.right == None):
                    root = None
                #node has 1 child
                elif(root.left == None):
                    root = root.right
                elif(root.right == None):
                    root = root.left

                else:
                    duplicateExist = True
                    min = self.findMinIter(root.right)
                    root.value = min
                    root = root.right
                break

        if(duplicateExist):
            duplicate = root.value
            while(root != None):
                if(duplicate < root.value):
                    root = root.left
                else:
                    root = None
                    
    def findNextIter(self, node: Node, value):
        while(node != None): 
            if(value < node.value):
                node = node.left
            elif(value > node.value):
                node = node.right 
            else:
                #case 1: target has right sub tree, find min in the subtree
                if(node.right != None):
                    return self.findMinIter(node.right)
                #case 2: target has no parents ex: bst = [9,8,7,6] -> 9 has no parent
                while(node.parent):
                    #check if current node is left most node from parent, loop until we are left most
                    if(node.parent.left == node):
                        return node.parent.value
                    node = node.parent
                return None
    def findPrevIter(self, node: Node, value):
        while(node != None): 
            if(value < node.value):
                node = node.left
            elif(value > node.value):
                node = node.right 
            else:
                #case 1: target has right sub tree, find min in the subtree
                if(node.left != None):
                    return self.findMaxIter(node.left)
                #case 2: target has no parents ex: bst = [1,2,3,4,5] -> 1 has no parent
                while(node.parent):
                    #check if current node is right most node from parent, loop until we are right most
                    if(node.parent.right == node):
                        return node.parent.value
                    node = node.parent
                return node
    def findMinIter(self, node: Node):
        smallest = node.value
        while(node != None):
            smallest = node.value
            node = node.left
        return smallest

    def findMaxIter(self, node: Node):
        max = node.value
        while(node != None):
            max = node.value
            node = node.right
        return max
    

tree = BST()
valuesToAdd = [10, 5, 15, 4, 13, 18, 12, 14, 16, 19]
#insertRec
for i in valuesToAdd:
    tree.insertRec(i)
#
"""
                       10
                   /        \
                 5           15
                /         /      \  
              4         13        18
                      /    \     /   \
                    12     14   16    19
"""
#deleteRec
print(tree.root.right.value) #15
tree.deleteRec(15)
print(tree.root.right.value) #16
"""
                       10
                   /        \
                 5           16
                /         /     \  
              4         13       18
                      /    \       \
                    12      14      19
"""
#findMinRec
print(tree.findMinRec(tree.root, tree.root.value)) #4

#findMaxRec
print(tree.findMaxRec(tree.root, tree.root.value)) #19

#findNextRec
print(tree.findNextRec(tree.root, 12)) #13

#findPrevRec
print(tree.findPrevRec(tree.root, 12)) #4
