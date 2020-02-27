class Node:
    def __init__(self,value):
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        self.root = None

    def getHeight(self, node: Node):
        if(node == None):
            return 0
        return node.height
    def rightRotate(self, node: Node):
        if(node.parent):
            parent = node.parent
        else:
            parent = None
        leftNode = node.left
        
        if(parent):
            parent.left = leftNode
            leftNode.parent = parent
        else:
            self.root = leftNode
            leftNode.parent = None
        node.left = leftNode.right
        if(leftNode.right):
            leftNode.right.parent = node
        node.parent = leftNode
        leftNode.right = node    

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        leftNode.height = 1 + max(self.getHeight(leftNode.left),self.getHeight(leftNode.right))

    def leftRotate(self, node: Node):
        rightNode = node.right
        node.right = rightNode.left
        if(rightNode.left):
            rightNode.left.parent = node
        if(node.parent):
            node.parent = rightNode
            rightNode.parent = node.parent
        else:
            node.parent = rightNode
            self.root = rightNode
            rightNode.parent = None
        rightNode.left = node  

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        rightNode.height = 1 + max(self.getHeight(rightNode.left),self.getHeight(rightNode.right))


    def getBalanceFactor(self, node: Node):
        if(not node):
            return 0
        
        return self.getHeight(node.left) - self.getHeight(node.right)
        
    def balance(self, node: Node):
        curr = node
        while(curr):
            BF = self.getBalanceFactor(curr)

            curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))

            if(abs(BF) <= 1):
                curr = curr.parent
                continue
            #left rotation
            if(BF > 0 and node.value < curr.left.value):
                self.rightRotate(curr)
                continue
                
            #right rotation
            elif(BF < 0 and node.value > curr.right.value):
                self.leftRotate(curr)
                continue

            #left right rotation
            elif(BF > 0 and node.value > curr.left.value):
                self.leftRotate(curr.left)
                self.rightRotate(curr)

            #right left rotation
            
            elif(BF < 0 and node.value < curr.right.value):
                self.rightRotate(curr.right)
                self.leftRotate(curr)
                continue
            

    def insertIter(self,value):
        root = self.root
        current = None
        while(root != None): 
            current = root             
            if(value < root.value):
                root.height += 1
                root = root.left
                
            elif(value > root.value):
                root.height += 1
                root = root.right
                
        if(current == None):
            self.root = Node(value)
            return
        elif(value < current.value):
            leftChild = Node(value)
            current.left = leftChild
            leftChild.parent = current
            current = current.left
        else:
            rightChild = Node(value)
            current.right = rightChild
            rightChild.parent = current
            current = current.right
        self.balance(current)

    def deleteIter(self,value):
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
    
    def inorder(self, node: Node):
        if(node == None):
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

tree = BST()
values = [5,4,3,2,1,0]
for i in values:
    tree.insertIter(i)

print(tree.root.left.left.value)
print(tree.root.left.value)
print(tree.root.value)
print(tree.root.right.left.value)
print(tree.root.right.value)
print(tree.root.right.right.value)