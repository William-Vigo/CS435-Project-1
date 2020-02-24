class Node:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:

    def __init__(self,value):
        self.root = Node(value)

    def insertRec(self, value):
        self.__insertHelp(self.root, value)

    def __insertHelp(self, node: Node, value):
        if(node == None):
            node = Node(value)
        elif(value > node.value):
            node.right = self.__insertHelp(node.right, value)
        elif(value < node.value):
            node.left = self.__insertHelp(node.left,value)
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
    
    def findNextRec(self, node: Node, value, greatest):
        if(node == None):
            return node
        if(value > node.value):
            return self.findNextRec(node.right, value, node.value)
        elif(value < node.value):
            greatest = node.value
            return self.findNextRec(node.left, value, greatest)
        else:
            if(node.right == None):
                if(node.value > greatest):
                    return None
                else:
                    return greatest
            else:
                return self.findMinRec(node.right, node.right.value)



    def findPrevRec(self, node: Node, value, smallest):
        if(node == None):
            return node
        if(value > node.value):
            smallest = node.value
            return self.findPrevRec(node.right, value, smallest)
        elif(value < node.value):
            return self.findPrevRec(node.left, value, node.value)
        else:
            if(node.left == None):
                
                if(node.value < smallest):
                    return None
                else:
                    return smallest
            else:
                return self.findMaxRec(node.left, node.left.value)


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

tree = BST(2)
tree.insertRec(4)
tree.insertRec(0)
tree.insertRec(5)
tree.insertRec(3)

print(tree.findPrevRec(tree.root, 0, tree.root.value))

        

        


