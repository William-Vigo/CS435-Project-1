class Node:
    def __init__(self,value):
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
            current.left = Node(value)
        else:
            current.right = Node(value)
            
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
values = [10, 5, 15, 4, 13, 18, 12, 14, 16, 19]
for i in values:
    tree.insert(i)

print(tree.root.left.value)
print(tree.root.value)

print(tree.findMinIter(tree.root))
print(tree.findMaxIter(tree.root))

tree.delete(4)
print(tree.root.right.value)

