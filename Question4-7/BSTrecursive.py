class Node:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

class BST:

    def __init__(self):
        self.root = None

    def insertRec(self, value):
        if(self.root == None):
            self.root = Node(value)
        self.__insertHelp(self.root, value)

    def __insertHelp(self, node: Node, value):
        if(node == None):
            node = Node(value)
        elif(value > node.value):
            rightChild = self.__insertHelp(node.right, value)
            node.right = rightChild
            rightChild.parent = node
        elif(value < node.value):
            leftChild = self.__insertHelp(node.left,value)
            node.left = leftChild
            leftChild.parent = node
        return node

    def deleteRec(self,value):
        self.__deleteHelp(self.root, value)

    def __deleteHelp(self, node: Node, value):
        if(node == None):
            return node
        if(value > node.value):
            node.right = self.__deleteHelp(node.right, value)
        elif(value < node.value):
            node.left = self.__deleteHelp(node.left, value)
        else:
            #case 1: node found was a leaf node
            if(node.left == None and node.right == None):
                node = None
            
            #case 2: node found has only 1 child
            elif(node.left == None):
                node = node.right
            
            elif(node.right == None):
                node = node.left
            
            #case 3: node found has 2 children
            else:
                node.value = self.findMinRec(node.right, node.right.value)
                node.right = self.__deleteHelp(node.right, node.value)

        return node
    
    def findNextRec(self, node: Node, value):
        if(node == None):
            return node
        if(value > node.value):
            return self.findNextRec(node.right, value)
        elif(value < node.value):
            return self.findNextRec(node.left, value)
        else:
            #case 1: target has right sub tree, find min in the subtree
            if(node.right != None):
                return self.findMinRec(node.right, node.right.value)
            #case 2: target has no parents ex: bst = [9,8,7,6] -> 9 has no parent
            while(node.parent):
                #check if current node is left most node from parent, loop until we are left most
                if(node.parent.left == node):
                    return node.parent.value
                node = node.parent
            return None

    def findPrevRec(self, node: Node, value):
        if(node == None):
            return node
        if(value > node.value):
            return self.findPrevRec(node.right, value)
        elif(value < node.value):
            return self.findPrevRec(node.left, value)
        else:
            #case 1: target has left sub tree
            if(node.left != None):
                return self.findMaxRec(node.left,node.left.value)
            #case 2: target has no parents ex: bst = [1,2,3,4,5] -> 1 has no parent
            while(node.parent):
                #check if current node is right most node from parent, loop until we are right most
                if(node.parent.right == node):
                    return node.parent.value
                node = node.parent
            return None
            


    def findMinRec(self, node: Node, min):
        if(node == None):
            return min
        min = node.value
        return self.findMinRec(node.left, min)

    def findMaxRec(self, node: Node, max):
        if(node == None):
            return max
        max = node.value
        return self.findMaxRec(node.right, max)

if __name__ == "__main__":
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
    print(tree.findPrevRec(tree.root, 12)) #10


            

