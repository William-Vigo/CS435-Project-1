import BSTrecursive as recBST
import BSTiterative as iterBST
import BBST as BalanceBST
import Problem_3 as ArrayOfInts

randomArray = ArrayOfInts.getRandomArray(10000)

iterBST  = iterBST.BST()
recBST = recBST.BST()
iterBBST = BalanceBST.BBST()

#Problem 5a
for i in randomArray:
    recBST.insertRec(i)
    iterBBST.insertIter(i)

#Problem 5c
for x in randomArray:
    iterBST.insertIter(x)
    iterBBST.insertIter(x)