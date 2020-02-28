import BSTrecursive as recBST
import BSTiterative as iterBST
import BBST as BalanceBST
import Problem_3 as ArrayOfInts

#Problem 6b
randomArray = ArrayOfInts.getRandomArray(10000)
BST = iterBST.BST()
AVL = BalanceBST.BBST()
BSTtraversal = 0
AVLtraversal = 0
for i in randomArray:
    BSTtraversal += BST.insertIter(i)
    AVLtraversal += AVL.insertIter(i)

print("BST traversal: " + str(BSTtraversal))
print("AVL traversal: " + str(AVLtraversal))

#Problem 6c
sortedArray = ArrayOfInts.getSortedArray(10000)
BST = iterBST.BST()
AVL = BalanceBST.BBST()

BSTtraversal = 0
AVLtraversal = 0

for x in sortedArray:
    BSTtraversal += BST.insertIter(x)
    AVLtraversal += AVL.insertIter(x)
print()

print("BST traversal: " + str(BSTtraversal))
print("AVL traversal: " + str(AVLtraversal))