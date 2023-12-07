class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
    
class Traversal:
    # preorderTraversal
    def preorderTraversal(self, root):
        res=[]
        self.preorder(res,root)
        return res
    
    def preorder(self,res,root):
        if root is None:
            return
        res.append(root.data) 
        self.preorder(res,root.left)
        self.preorder(res,root.right)
    #inorderTraversal
    def inorderTraversal(self, root):
        res=[]
        self.inorder(res,root)
        return res
    
    def inorder(self,res,root):
        if root is None:
            return
        self.inorder(res,root.left)
        res.append(root.data)
        self.inorder(res,root.right)  

    #postorderTraversal 
    def postorderTraversal(self, root):
        res=[]
        self.postorder(res,root)
        return res
    
    def postorder(self,res,root):
        if root is None:
            return
        self.postorder(res,root.left)
        self.postorder(res,root.right)  
        res.append(root.data)
    

    #iterative way#
    #Left Subtree→ Root→ Right Subtree
    def inorder_traversal(self,root):
        #we need a stack to add the nodes .we always travel to left to reach the null (leaf)
        #once we reach it we just assign to result list
        #travel back to right and append that 
        currentNode=root
        stack=[]
        res=[]
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode=currentNode.left
            currentNode=stack.pop()
            res.append(currentNode.data)
            currentNode=currentNode.right
        return res
    #preorder
    # Root-->left--> right
    def preorder_traversal(self,root):
        res=[]
        if not root:
            return res
        stack=[root]
        while stack:
            currentNode=stack.pop()
            #since we push in stack we push it first right and left then pop left first
            res.append(currentNode.data)
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)
        return res
    def postorder_traversal(self,root):
        if root is None: 
            return
        ans=[]
        stack=[]
        #one stack iterative method
        currentNode=root
        while(True): 
            while (root): 
                # Push root's right child and then root to stack 
                if root.right is not None: 
                    stack.append(root.right) 
                stack.append(root) 
    
                # Set root as root's left child 
                root = root.left 
            
            # Pop an item from stack and set it as root 
            root = stack.pop() 
    
            # If the popped item has a right child and the 
            # right child is not processed yet, then make sure 
            # right child is processed before root 
            if stack and  (root.right is not None and
                stack[-1] == root.right): 
                stack.pop() # Remove right child from stack 
                stack.append(root) # Push root back to stack 
                root = root.right # change root so that the 
                                # right childis processed next 
    
            # Else print root's data and set root as None 
            else: 
                ans.append(root.val) 
                root = None
    
            if (len(stack) <= 0): 
                    return ans 
    #LEVEL ORDER TRAVERSAL 
    #FIND THE HEIGHT
    def levelOrder(self, root):
        def find_height(node):
            #base case to break the recursion
            if node is None:
                return 0
            else:
                lheight=find_height(node.left)
                rheight=find_height(node.right)

                if lheight>rheight:
                    return lheight+1
                else:
                    return rheight+1   
       
        def printCurrentLevel(root, level,ans):

            if root is None:
                return 
            if level == 1:
                ans.append(root.val)
            elif level>1:
                printCurrentLevel(root.left,level-1,ans)
                printCurrentLevel(root.right ,level-1,ans)
        
        h=find_height(root)
        z=[]
        for i in range(1,h+1,1):
            ans=[]
            printCurrentLevel(root,i,ans)
            z.append(ans)
        return z 
            
    






t=Traversal()
root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(9)
coins = [100000]
target = 100000
print(t.postorder_traversal3(root))
    


        