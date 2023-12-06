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
        res=[]
        if not root:
            return res
        stack=[]
        currentNode=root
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode=currentNode.left
            currentNode=stack.pop() # we just assignthe last leaf
            res.append(currentNode.data)
            currentNode=currentNode.right # we go for next right

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
        res = []
        if not root:
            return res
        curr_node = root
        stack = []
        right_stack = []
        while stack or curr_node:
            if curr_node:
                if curr_node.right:
                    right_stack.append(curr_node.right)
                    print(right_stack)
                stack.append(curr_node)
                print(stack)
                curr_node = curr_node.left
            else:
                curr_node = stack[-1]
                if right_stack and curr_node.right == right_stack[-1]:
                    curr_node = right_stack.pop()
                else:
                    res.append(curr_node.data)
                    print(res)
                    print(stack)
                    stack.pop()
                    curr_node = None
            
        return res    
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
print(t.minimumAddedCoins(coins,target))
    


        