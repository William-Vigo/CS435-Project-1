import BSTrecursive as BST
import BBST as BalanceBST
import Problem_3 as ArrayOfInts

randomArray = ArrayOfInts.getRandomArray(10000)

recBST = BST.BST()
iterBBST = BalanceBST.BBST()

#Problem 5a
for i in randomArray:
    recBST.insertRec(i)
    #iterBBST.insertIter(i)

#Problem 5c