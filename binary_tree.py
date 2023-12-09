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
    def getTreeTraversal(self,root):
        res=[]
        def preorder(res,root):
            if root is None:
                return
            res.append(root.data) 
            preorder(res,root.left)
            preorder(res,root.right)
        preorder(res,root)
        print(res)
        res=[]
        def inorder(res,root):
            if root is None:
                return
            inorder(res,root.left)
            res.append(root.data)
            inorder(res,root.right)  
        inorder(res,root)
        print(res)
    #postorderTraversal 
        res=[]
        def postorder(res,root):
            if root is None:
                return
            postorder(res,root.left)
            postorder(res,root.right)  
            res.append(root.data)
        postorder(res,root)
        print(res)
            
    

    #find the height
    def maxDepth(self, root):
        def find_height(node):
            if node is None:
                return 0
            else:
                rheight=find_height(node.right)
                lheight=find_height(node.left)
                print(rheight,lheight)
                if(rheight >lheight):
                    return rheight+1
                else:
                    return lheight+1
               
        h=find_height(root)
        return h 
    
    def isBalanced(self, root) -> bool:

        def find_height(node):
            if node is None:
                return 0
            else:
                #we track the level by level
                rheight=find_height(node.right)
                if(rheight==-1):
                    return -1
                lheight=find_height(node.left)
                if(lheight==-1):
                    return -1
                if abs(lheight-rheight)>1:
                    #it means its not a balanced tree (height tree)
                    return -1
                
                return max(lheight,rheight)+1




        if(find_height(root)!=-1):
            return True
        else:
            return False

    def diameterOfBinaryTree(self, root):
        diameter=[0]
        def find_height(node):
            if node is None:
                return 0
            else:
                lheight=find_height(node.left)
                rheight=find_height(node.right)
                diameter[0]=max(diameter[0],lheight+rheight)
                return max(lheight, rheight)+1
        find_height(root)
        return diameter[0]

    def maxPathSum(self, root):
        max_path = float("-inf")
        if root.left is None and root.right is None:
            return root.val
        def find_path(root):
            nonlocal max_path
            if root is None:
                return 0
            #to avoid the negative so we negalte with 0
            leftpath_sum=max(0,find_path(root.left))
            rightpath_sum=max(0,find_path(root.right))
            max_path=max(max_path,leftpath_sum+rightpath_sum+root.val)
            return root.val+max(leftpath_sum,rightpath_sum)
        find_path(root)
        return max_path



        
#[1, '(', 2, '(', 4,')',')', '(', 3, ')']



t=Traversal()
root = Node(1)
root.right=Node(2)
root.right.right=Node(3)
coins = [100000]
target = 100000
print(t.isBalanced(root))
    


        