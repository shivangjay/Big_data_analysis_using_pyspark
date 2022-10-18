# Print tree in a diagonal form

# We use the distance of slope from the rightmost slope as key 
# in a dict and then proceed

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonal_print_util(root, d, diagonal_map):
    if root is None:
        return

    try:
        diagonal_map[d].append(root.val)
    except:
        diagonal_map[d] = [root.val]

    # Increase vertical distance if left child
    diagonal_print_util(root.left, d+1, diagonal_map)

    # Vertical distance remains same for the right child
    diagonal_print_util(root.right, d, diagonal_map)


def diagonal_print(root):
    diagonal_map = dict()

    diagonal_print_util(root, 0, diagonal_map)
    
    for i in diagonal_map:
        for j in diagonal_map[i]:
            print(j, end=" ")
        print('')
        
        
        
#Python program for diagonal traversal of binary tree
#importing binarytree module for creating binary tree
from binarytree import Node
#function to print diagonal elements
def diagtrav(r):
#empty list to store diagonal elements
    d=[]
#Node to signal end of diagonal
    s=Node(-10)
#extracting the first diagonal
    while r:
        d.append(r)
        r=r.right
#appending signal node
    d.append(s)
#printing diagonals and side by side appending the next diagonal and printing till all diagonals are printed 
    while len(d)!=1:
        f=d.pop(0)
        if f!=s:
            print(f.value,end=' ')
            n=f.left
            while n:
                d.append(n)
                n=n.right
        else:
            d.append(s)
            print()
