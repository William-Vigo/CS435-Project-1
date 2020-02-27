class Node:
    def __init__(self,value):
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


class BBST:
    def __init__(self):
        self.root = None
    def adjustCurrentNodeWeights(self, node: Node):
        if(not node.left and not node.right):
            return 1
        if(not node.left):
            return node.right.height + 1
        if(not node.right): 
            return node.left.height + 1
        
        return max(node.left.height, node.right.height) + 1
    def adjustWeights(self,node: Node):
        curr = node
        while(curr):
            curr.height = self.adjustCurrentNodeWeights(curr)
            curr = curr.parent 

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
            if(node.value < parent.value):
                parent.left = leftNode
                leftNode.parent = parent
                
            else:
                parent.right = leftNode
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
        if(node.parent):
            parent = node.parent
        else:
            parent = None
        rightNode = node.right
        
        if(parent):
            if(node.value > parent.value):
                parent.right = rightNode
                rightNode.parent = parent
                
            else:
                parent.left = rightNode
                rightNode.parent = parent
        else:
            self.root = rightNode
            rightNode.parent = None
        node.right = rightNode.left
        if(rightNode.left):
            rightNode.left.parent = node
        node.parent = rightNode
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
            leftBF = self.getBalanceFactor(curr.left)
            rightBF = self.getBalanceFactor(curr.right)

            curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))

            if(abs(BF) <= 1):
                curr = curr.parent
                continue
            #right rotation
            if(BF > 0 and leftBF >= 0):
                self.rightRotate(curr)
                continue
                
            #left rotation
            elif(BF < 0 and rightBF <= 0):
                self.leftRotate(curr)
                continue

            #left right rotation
            elif(BF > 0 and leftBF < 0):
                self.leftRotate(curr.left)
                self.rightRotate(curr)

            #right left rotation
            
            elif(BF < 0 and rightBF > 0):
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
                    if(not root.parent):
                        self.root = None
                        return
                    if(root.parent.left == root):
                        root.parent.left = None
                    else:
                        root.parent.right = None
                    self.adjustWeights(root.parent)
                    self.balance(root.parent)
                #node has 1 child
                elif(root.left == None):
                    root.value = root.right.value
                    root.right = None 
                    self.balance(root)
                elif(root.right == None):
                    root.value = root.left.value
                    root.left = None
                    self.adjustWeights(root)
                    self.balance(root)
                else:
                    duplicateExist = True
                    min = self.findMinIter(root.right)
                    root.value = min
                break

        if(duplicateExist):
            duplicate = root.value
            root = root.right
            while(root != None):
                if(duplicate < root.value):
                    root = root.left
                    continue
                if(root.parent.left.value == duplicate):
                    if(root.right):
                        root.right.parent = root.parent
                        root.parent.left = root.right
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
                        root = None
                    elif(root.left):
                        root.left.parent = root.parent
                        root.parent.left = root.left
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
                        root = None
                    else:
                        root.parent.left = None
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
                        root = None
                      
                elif(root.parent.right.value == duplicate):
                    if(root.left):
                        root.left.parent = root.parent
                        root.parent.right = root.left
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
                        root = None
                    elif(root.right):
                        root.right.parent = root.parent
                        root.parent.right = root.right
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
                        root = None
                    else:
                        root.parent.right = None
                        self.adjustWeights(root.parent)
                        self.balance(root.parent)
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

tree = BBST()
values = [10,5,15,4,8,11,18,1,6,9,19,7]
for i in values:
    tree.insertIter(i)

#print(tree.inorder(tree.root))
tree.deleteIter(18)
tree.deleteIter(8)
tree.deleteIter(1)

print()
print(tree.inorder(tree.root))

