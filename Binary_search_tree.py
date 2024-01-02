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
    def minVal(self,root):
        prev=0
        if root:
            while root.left:
                root=root.left
            return root.data
        else:
            return -1
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
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #check the nearest value
        if root is None:
            node=TreeNode(val,None,None)
            return node
        main_root=root
        while root:
            if root.val >val:
                #what if the node leaf are empty
                if root.left:
                    root=root.left
                else:
                    #set a new node and link it
                    node=TreeNode(val,None,None)
                    root.left=node
                    break
            elif root.val<val:
                if root.right:
                    root=root.right
                else:
                    node=TreeNode(val,None,None)
                    root.right=node
                    break
        return main_root
    
    def helper(self,root):
        # below are the edge cases
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        rightNode=root.right#taking the full right
        leftNodelastright=self.findthelast(root.left)
        #THE LINK
        leftNodelastright.right=rightNode

        return root.left
    
    def findthelast(self,root):
        if root.right is None:
            return root
        return self.findthelast(root.right)
   

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        main_root=root
        if root is None:
            return None

        if root.val==key:
            return self.helper(root)
        #we find the root first
        # the right node if there is a link of the key right
        # we take that right and keep a link to the last right to maintain the bst
        while root:
            if root.val>key:
                if (root.left!=None and root.left.val==key):
                    root.left=self.helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right!=None and root.right.val==key:
                    root.right=self.helper(root.right)
                    break
                else:
                    root=root.right
        return main_root


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(res,root):
            if root is None:
                return
            inorder(res,root.left)
            res.append(root.val)
            inorder(res,root.right)  
        res=[]
        inorder(res,root)
        return res[k-1]
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(res,root):
            if root is None:
                return
            inorder(res,root.left)
            res.append(root.val)
            inorder(res,root.right)  
        res=[]
        inorder(res,root,prev)
        for i in range(1,len(res),1):
            if res[i]<=res[i-1]:
                return False
        
        return True     
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def traverse(root,p,q):
        #     #base case
        #     if root is None or root==p or root==q:
        #         return root
        #     left=traverse(root.left,p,q)
        #     right=traverse(root.right,p,q)
        #     #right check
        #     if right is None:
        #         return left
        #     #left check
        #     elif left is None:
        #         return right
        #     else:
        #         return root
        # return traverse(root,p,q)

        if root is None:
            return None
        cur=root.val
        #means if the value is greater its there in right means go right
        if cur<p.val and cur <q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if cur>p.val and cur >q.val:
            return self.lowestCommonAncestor(root.left ,p,q)
        return root
       






        
        