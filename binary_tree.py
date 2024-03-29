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
        max_path = float("- ")
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
    
    def rightSideView(self, root):
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

        #Root to Node Path in Binary Tree
    def roottopath(self,root,x):
        arr=[]
        def inorder(root,arr,x):
            if root is None:
                return False
            #we add the element
            arr.append(root.data)
            #we check its correct or not
            if root.data==x:
                return True
            #if its wrong it will be poped and below check will not happen
            if inorder(root.left,arr,x) or inorder(root.right,arr,x):
                return True
            arr.pop()
            return False
        inorder(root,arr,x)
        return arr
    

    def lowestCommonAncestor(self, root, p, q):
        #we need traverse till we reach p and q
        # return the p and q their roots in recursive manner
        # when any side we notice the null we take the value of the root 
        #if both we receive it means the root is the ancestor

        def traverse(root,p,q):
            #base case
            if root is None or root==p or root==q:
                return root
            left=traverse(root.left,p,q)
            right=traverse(root.right,p,q)
            #right check
            if right is None:
                return left
            #left check
            elif left is None:
                return right
            else:
                return root
        return traverse(root,p,q)    
    
    def widthOfBinaryTree(self, root):
        #we need to index the each node
        # with the formula left(2*i +1) and right(2*i+2)
        #to overflow stack issue we take the min of the first element and sub then we find the left and right index
        # in a dict set you will hold a maximum and minum of the level ( we need to do  a level order traversal)
        dict_=dict()
        self.max_diff = 0
        def level_order(root,index_,level,dict_):
            if root is None:
                return None
            dict_.setdefault(level, [index_, index_])
            #min
            dict_[level][0]=min(dict_[level][0],index_)
            #max
            dict_[level][1]=max(dict_[level][1],index_)
            self.max_diff=max(self.max_diff,dict_[level][1]-dict_[level][0])
            level_order(root.right,2*index_,level+1,dict_)
            level_order(root.left,2*index_+1,level+1,dict_)
            

        level_order(root,0,0,dict_)
        return self.max_diff+1
    def reverseTraversal(root):
        # we go by reverse method
        # we start from root and check the child if less then assigin the root val to childs
        # same is followed till leaf node
        #then we update the root after that 
        def reverse(root):
            if root is None:
                return 
            child=0
            if root.left!=None:
                child+=root.left.data
            if root.right!=None:
                child+=root.right.data
            
            if child>=root.val:
                root.data=child
            else:
                if(root.right!=None):
                    root.right.val=root.data
                elif(root.left!=None):
                    root.left.val=root.data
            reverse(root.left)
            reverse(root.right)
            tot=0
            if root.left!=None:
                tot+=root.left.data
            if root.right!=None:
                tot+=root.right.data
            if (root.left!=None or root.right!=None):
                root.data=tot
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #first we need to map the child with its parent node
        # we need 2 hash maps to store visted and parent node
        # once marked till we reach the K we check the length
        parent=dict()
        self.markparents(root,parent)
        visted=dict()
        q=deque([target])
        visted[target]=True
        curr=0 #to send the level a distance
        while q:
            size=len(q)
            # which means we attained the k length
            if curr==k:
                break
            #in three directions we move
            for _ in range(size):
                node=q.popleft()
                if node.left and node.left not in visted:
                    q.append(node.left)
                    visted[node.left]=True
                if node.right and node.right not in visted:
                    q.append(node.right)
                    visted[node.right]=True
                if node in parent and parent[node] not in visted:
                    q.append(parent[node])
                    visted[parent[node]]=True
            curr+=1
        
        return [node.val for node in q]


    def markparents(self,root,parent):
        queue=deque([root])
        #TO SET THE CHILD PARENT LINK
        while queue:
            curr=queue.popleft()
            if curr.left:
                parent[curr.left]=curr
                queue.append(curr.left)
            if curr.right:
                parent[curr.right]=curr
                queue.append(curr.right)   
    def countNodes(self, root):
        #using the formula (2*h +1)  
        def gettheheight_left(root):
            curr=0
            while root:
                curr+=1
                root=root.left
            return curr
        def gettheheight_right(root):
            curr=0
            while root:
                curr+=1
                root=root.right
            return curr
        
        if root is None:
            return 0
        lheight=gettheheight_left(root)
        rheight=gettheheight_right(root)

        if lheight==rheight:
            return 2**rheight-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #with the help of preorder, inorder we take inorder(root) reference
        #traverse through the preorder data
        #we need to create a hashmap for inorder with the index
        inorder_map=dict()
        for i ,val in enumerate(inorder):
            inorder_map[val]=i
        
        def printbinary(preorder_start,preorder_end,inorder_start,inorder_end):
            if preorder_start > preorder_end:
                return None
            # Create a new node using the first element in the preorder list  
            root_val= preorder[preorder_start]
            root=TreeNode(root_val)#we take the root from preorder[0]
            # Find the index of the root element in the inorder list
            inroot=inorder_map[root_val] #we take that inorder index
            numsLeft = inroot - inorder_start # we subtract with the 
            root.left=printbinary(preorder_start+1,preorder_start+numsLeft,inorder_start,inroot-1)
            root.right=printbinary(preorder_start+numsLeft+1,preorder_end,inroot+1,inorder_end)
            return root
        return printbinary(0,len(preorder)-1,0,len(inorder)-1)    
    
    def buildTree(self, inorder, postorder):
        #with the help of preorder, inorder we take inorder(root) reference
        #traverse through the preorder data
        #we need to create a hashmap for inorder with the index
        inorder_map=dict()
        for i ,val in enumerate(inorder):
            inorder_map[val]=i
        
        def printbinary(postorder_start,postorder_end,inorder_start,inorder_end):
            if postorder_start > postorder_end:
                return None
            # Create a new node using the first element in the preorder list  
            root_val= postorder[postorder_end]
            root=TreeNode(root_val)#we take the root from preorder[0]
            # Find the index of the root element in the inorder list
            inroot=inorder_map[root_val] #we take that inorder index
            numsLeft = inroot - inorder_start # we subtract with the 
            #post order [ left (0+numLEFT-1) ,right, root ]
            root.left=printbinary(postorder_start,postorder_start+numsLeft-1,inorder_start,inroot-1)
            root.right=printbinary(postorder_start+numsLeft,postorder_end-1,inroot+1,inorder_end)
            return root
        return printbinary(0,len(postorder)-1,0,len(inorder)-1)  
    


    def serialize(self, root):
        #level order traversal 
        # we need to convert a tree into a string
        res=[]
        def DFS(root):
            if root is None:
                res.append('N')
                return
            res.append(str(root.val))
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return ",".join(res)

    def deserialize(self, data):
        #SPLIT THE VALUES
        values=data.split(",")
        self.index=0
        def DFS():
            if values[self.index]=='N':
                self.index+=1
                return
            root=TreeNode(int(values[self.index]))
            self.index+=1
            root.left=DFS()
            root.right=DFS()
            return root
        return DFS()
    def inorder_traversal_Morris(self,root):
        res=[]
        curr=root
        while(curr!=None):
            #first case if left has null then move to right and print it
            if curr.left==None:
                res.append(curr.val)
                curr=curr.right
            else:
                #if we have left find the right most and link with the root 
                #since its inorder we check the right most of left (left - root - right)
                # so we link the right most to the root thread
                prev=curr.left
                #checking already a thread is linked
                while (prev.right and prev.right!=curr):
                    prev=prev.right
                #this above while to check the rightmost
                if prev.right==None:
                    prev.right=curr
                    curr=curr.left
                #if there is no link form a link

                else:#maybe there is a link
                    #visting again so cut the link
                    prev.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res
    def preorder_traversal_Morris(self,root):
        #root left right
        res=[]
        curr=root
        #since we start with the root we add to resultant array/list
        while (curr!=None):
            res.append(curr)
            #edge case left is not avalaible
            if curr.left==None:
                res.append(curr.val)
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if root==None:
                return root
            leftTail=dfs(root.left)
            rightTail=dfs(root.right)
            if leftTail:
                #end of leaf node root
                leftTail.right=root.right
                root.right=root.left
                root.left=None
            return rightTail or leftTail or root
        return dfs(root)         
            
     
    














#[1, '(', 2, '(', 4,')',')', '(', 3, ')']



t=Traversal()
root = Node(1)
root.right=Node(2)
root.right.right=Node(3)
root.left=Node(5)
root.left.left=Node(9)
coins = [100000]
target = 100000
print(t.roottopath(root,9))
    


        