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
