class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

class Binary_search_tree:
    def isValidBST(self,order: [int]) -> bool:
        k=set()
        prev=0
        for element in order:
            if element not in k:
                if(element>prev):
                    k.add(element)
                    prev=element
                else:
                    return False
            else:
                return False
        return True
    def searchBST(self, root, val):
        while (root!=None and root.val!=val):
            if root.val>val:
                root=root.left
            else:
                root=root.right
        if root:
            return root
        else:
            return None
    def findCeil(root, x):
        ceil=-1
        while root:
            if root.data >x:
                ceil=root.data
                root=root.left# to find a near value if exits
            elif root.data<x:
                root=root.right
            else:
                ceil=root.data
                return ceil
        return ceil

    def findfloor(root, x):
        floor=-1
        while root:
            if root.val==x:
                floor=root.val
                return floor
            elif x>root.val:
                floor=root.val
                root=root.right
            else:
                root=root.left
        return floor
    
        