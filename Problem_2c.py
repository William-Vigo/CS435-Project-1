class Node:
    def __init__(self,value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insertIter(self,value):
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

    def sort(self):
        node = self.root
        sortedList = []
        stack = []
        while(True):
            if(node != None):
                stack.append(node)
                node = node.left
                
            elif(stack):
                node = stack.pop()
                sortedList.append(node.value)
                node = node.right
            else:
                break
        return sortedList

tree = BST()
values = [10,5,20,6,12,7,11,16,19,18,17]
for i in values:
    tree.insertIter(i)

print(tree.sort())