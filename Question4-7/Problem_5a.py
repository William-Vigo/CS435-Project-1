import BSTrecursive as BST
import BBST as BalanceBST
import Problem_3 as ArrayOfInts

randomArray = ArrayOfInts.getRandomArray(10000)

recBST = BST.BST()
iterBBST = BalanceBST.BBST()

for i in randomArray:
    recBST.insertRec(i)
    iterBBST.insertIter(i)

