from collections import defaultdict 
from collections import deque 
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

    def isSameTree(self, p, q):
        def preorder(p,q):
            if p is None or q is None:
                return (p==q)
            return (p.val==q.val) and preorder(p.right,q.right) and preorder(p.left,q.left)
        return preorder(p,q)



    def zigzagLevelOrder(self, root):
        #iterative method
        #we will take a current node and iterate, we add the next which is childerns list
        #when we reach a level even we reverse the current node list and apped with the list
        res=[] #result
        if not root:
            return res
        curr=[root]
        nxt=[] #to hold the childerns 
        level=1

        while curr:
            for i in curr:
                if i.left:#since we start with zig zag left
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)

            if level%2==0:
                curr.reverse()
            res.append([i.val for i in curr])
            curr=nxt #to set the childern for next flow
            if nxt:
                level+=1
            nxt=[]
        return res
    def traverseBoundary(root):
        #we need to first traverse through left till exculding
        # we need to inorder and without the root for the leaf nodes
        # we need to right boundary starting from the base print the first bottom root right then left 
        res=[]
        #left traversal
        def printleft(root,res):
            if root:
                if root.left:
                    res.append(root.data)
                    printleft(root.left,res)
                else:
                    print(root.data)
                    printleft(root.right,res)
        def printleaf(root,res):
            if(root):
                printleaf(root.left,res) 
                if root.left is None and root.right is None:
                    res.append(root.data)
                printleaf(root.right,res)

        def printRightbottom(root,res):
            if root:
                if root.right:
                    printRightbottom(root.right,res)
                    res.append(root.data)
                elif(root.left):
                    printRightbottom(root.left,res)
                    res.append(root.data)
        def printBoundary(root,res):
            if (root):
                res.append(root.data) #base root
                printleft(root.left,res)
                printleaf(root.left,res)
                printleaf(root.right,res)
                printRightbottom(root.right,res)
        printBoundary(root,res)
            

    def verticalTraversal(self, root):
        # we maintain a que
        # since we go vertical line colunm will is negative we go with that as key
        # we keep adding the left right que in the correct dic key values [right,node value]
        q=deque()
        d=defaultdict(list)
        q.append([root,0,0])
        while q:
            node,c,r=q.popleft()
            d[c].append([r,node.val])
            if node.left:
                q.append([node.left,c-1,r+1])
            if node.right:
                q.append([node.right,c+1,r+1])
        ans=[]
        #since we do have a mutiple list of list
        for i in sorted(d):
            temp=d[i]
            temp.sort()# sorting by their values
            t=[]
            for j in temp:
                t.append(j[1]) 
            ans.append(t)
        return ans
    def topView(self,root):
        q=deque()
        ans=[]
        d=defaultdict(list)
        q.append([root,0])
        while q:
            node,line=q.popleft()
            if line not in d:
                d[line]=node.val
            if node.left:
                q.append([node.left,line-1])
            if node.right:
                q.append([node.right,line+1])
        print(d)
        #since we do have a mutiple list of list
        for i in sorted(d):
            ans.append(d[i])
        print(ans)
        return ans
    
    def bottomView(root):
        q=deque()
        d=defaultdict(list)
        q.append([root,0])
        while q:
            node,line=q.popleft()
            #since we take the bottom we just replace the existing value so that it will take the 
            #latest value that leaf node
            d[line]=node.data
            if node.left:
                q.append([node.left,line-1])
            if node.right:
                q.append([node.right,line+1])
        res=[]
        #since we do have a mutiple list of list
        for i in sorted(d):
            res.append(d[i])
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        #when we attain the size level it means that is first node of the level and we append the right
        def inordertravesal(root,res,level):
            if root is None:
                return
            if len(res)==level:
                res.append(root.val)
            inordertravesal(root.right,res,level+1)
            inordertravesal(root.left,res,level+1)

        inordertravesal(root,res,0)
        return res
        
#[1, '(', 2, '(', 4,')',')', '(', 3, ')']



t=Traversal()
root = Node(1)
root.right=Node(2)
root.right.right=Node(3)
root.left=Node(5)
root.left.left=Node(9)
coins = [100000]
target = 100000
print(t.topView(root))
    


        