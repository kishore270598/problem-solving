import time
import math
class Recursion_problems:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        k=n
        if(k<0):
            n*=-1
        while(n<0):
            if(n==0):
                return 1
            if(n%2==0):
                ans=x*x
                n=n//2
            else:
                ans=ans*x
                n=n-1
        if(k<0):
            return 1.0/ans
        else:
            return ans
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        return self.myPow(x, n//2) * self.myPow(x, n//2) * self.myPow(x, n%2)
    #2^10-- > 2^5 * 2^5 
    # 2^5---> 2^(5//2) *2^(5//2) * 2^5%2

    def myAtoi(self, s: str) -> int:
        def rec_atoi(s,i,n,digitsStarted,ans):
            if i>=n:
                return ans
            if digitsStarted:    
                if s[i].isdigit():
                    ans = ans*10 + int(s[i])
                    return rec_atoi(s, i+1,n, True, ans)
                else:
                    return ans
            if s[i] == ' ':
                return rec_atoi(s, i+1,n, False, ans)
                
            if s[i] == '-':
                return -1 * rec_atoi(s, i+1,n, True, ans)

            if s[i] == '+':
                return rec_atoi(s, i+1,n, True, ans)
                        
            if s[i].isdigit():
                return rec_atoi(s, i+1, n, True, int(s[i]))
            return 0
                
        maxInt=2**31 - 1
        minInt=-2**31    
        ans=rec_atoi(s,0,len(s),False,0)
        if ((ans)>maxInt):
            return maxInt
        elif ((ans)<=minInt):
            return minInt
        return ans
        
    def countGoodNumbers_brute(self, n: int) -> int:
        count=1
        for i in range(0,n,1):
            if(i%2==0):
                count=count*5
            else:
                count=count*4

        return count 

    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        odd=n//2
        even=n//2+n%2
        return (self.binaryExp(5,even)%mod *self.binaryExp(4,odd)%mod)%mod
    
    def binaryExp(self, x, n):
        mod=1000000007
        if (n==0):
            return 1
        if (n<0):
            return 1/self.binaryExp(x, -n)
        if (n%2==0):
            return self.binaryExp((x*x)%mod, n//2)
        else:
            return x*self.binaryExp((x*x)%mod,(n-1)//2) 
    def sort_stack_brute(self,s):
        temp=[]
        #till we swap the main stack to empty stack
        while (len(s)!=0):
            tmp=self.top(s)
            s.pop()
            while(len(temp)!=0 and self.top(temp)<tmp):
                    #to compare the top of the temp stack is in correct order
                    #if not pop the wrong orders and put back in old stack and place the correct value
                    s.append(self.top(temp))
                    temp.pop()
            temp.append(tmp)
        return temp
    def top(self,stack):
        p=len(stack)
        return stack[p-1]
    
    def sortedInsert(self,stack, key):
    # base case: if the stack is empty or
    # the key is greater than all elements in the stack
        if not stack or key > self.top(stack):
            stack.append(key)
            return
        # remove the top element
        top = stack.pop()
        # recur for the remaining elements in the stack
        self.sortedInsert(stack, key)
    
        # insert the popped element back into the stack
        stack.append(top)
    # Recursive method to sort a stack
    def sortStack(self,stack):
        if not stack:
            return
        top = stack.pop()
        # recur for the remaining elements in the stack
        self.sortStack(stack)
        # insert the popped element back into the sorted stack
        self.sortedInsert(stack, top)
        return stack
    
    def reverseStack(self,stack) -> None:
        if not stack:
            return
        top = stack.pop()
        self.reverseStack(stack)
        self.add_stack(stack, top)
        return stack

    def add_stack(self,stack, key):
            if not stack :
                stack.append(key)
                return
            top = stack.pop()
            self.add_stack(stack, key)
            stack.append(top)
    def DecimalToBinary(self,num):
        ans='000'
        if(num>1):
            self.DecimalToBinary(num//2)
        ans+=str(num%2)
        print(ans)
    
    def binaryrange(self,n):
        ans='000'
        val=0
        for i in range (0,n+1,1):
            self.DecimalToBinary(i)
            print(end="-")

    def allbinary(self,n):
        arr=[0]*n
        self.genratebinary(arr)

    def countStrings(self,n, out='', last_digit=0):
        # if the number becomes n–digit, print it
        if n == 0:
            print(out, end=' ')
            return
    
        # append 0 to the result and recur with one less digit
        self.countStrings(n - 1, out + '0', 0)
    
        # append 1 to the result and recur with one less digit
        # only if the last digit is 0
        if last_digit == 0:
            self.countStrings(n - 1, out + '1', 1)
    def generateParenthesis(self, n: int):
    #if open barckets less then number you can add
    # if the closed brackets less then the open brackets we can close
    #if both the closed and open are equal we end
        def gen(left, right, s):
            if left==right==n:
                res.append(s)
                return 
            if left < n:
                gen(left + 1, right, s + '(')

            if right < left:
                gen(left, right + 1, s + ')')

        res = []
        gen(0, 0, '')
        return res
    ############################
    ############################
    ## IMPORTANT - POWERSET ####
    ############################
    ############################
    def subsets_brute(self, nums):
        sub=dict()
        z=set()
        for i in range(0,len(nums)+1,1):
            for j in range(0,i+1,1):
                a=[]
                for k in range(j,i,1):
                    a.append(nums[k])
    def subset(self,nums):#bit approch
        n=len(nums)
        k=set()
        print(n)
        for i in range(0,(1<<n),1):
            s=[]
            for j in range(0,n,1):
                if(i&(1<<j)==0):
                    s.append(nums[j])
                print(s)
    # def subset1(self,nums):
    #     ans=[]
    #     curr=[]
    #     def findPowerSet(main,cur,n,ans):
    #         #base case is when it hits last element we find one sub string
    #         if n==0:
    #             k=[]
    #             for i in cur:
    #                 k.append(i)
    #             ans.append(k)
    #             return 
    #         cur.append(main[n-1])
    #         #including last element
    #         findPowerSet(main,cur,n-1,ans)
    #         #not including last element just pop and keep on back tracking
    #         cur.pop()
    #         findPowerSet(main,cur,n-1,ans)
    #     findPowerSet(nums, curr, len(nums),[])
    #     return ans
    def subset_op(self,nums): # main codee
        ans=[]
        subset=[]      
        def findPowerSet(index):
            #base case is when it hits last element we find one sub string
            if index>=len(nums):
                ans.append(subset.copy())
                return
            #include the first element
            subset.append(nums[index])
            findPowerSet(index+1)
            #dont include first element
            subset.pop()
            findPowerSet(index+1)
        findPowerSet(0)
        return ans 
    #to find the distinct subsequence of 2 strings 
    #best approch
    def func(s: str, n: int) -> int:
        # Initializing 'count' with 1.
        count = 1

        # Creating a dictionary 'm1' to store character counts.
        m1 = {}

        # Calculating the number of distinct subsequences.
        for i in range(n):
            if s[i] not in m1:
                m1[s[i]] = count
                count *= 2
            else:
                temp = m1[s[i]]
                m1[s[i]] = count
                count *= 2
                count -= temp

        return count
    #optimal approch
    def moreSubsequence(self,n: int, m: int, a: str, b:str) -> str:
        n=set()
        def printAllSubsequence(input_str, output_str):
            if len(input_str) == 0:
                if(output_str not in n):
                    n.add(output_str)
                return
            printAllSubsequence(input_str[1:], output_str+input_str[0])
            printAllSubsequence(input_str[1:], output_str)
        printAllSubsequence(a,'')
        a_len=len(n)-1
        n=set()
        printAllSubsequence(b,'')
        b_len=len(n)-1
        if(a_len>b_len):
            return a
        elif(a_len<b_len):
            return b
        else:
            return a
    def subarraysWithSumK(self,a,k):
        ans=[]
        subset=[]
        def sub_rec(index,s):
            if(index>=len(a)):
                if(s==k):
                    ans.append(subset.copy())
                return 
            subset.append(a[index])
            s+=a[index]
            sub_rec(index+1,s)
            s-=a[index]
            subset.pop()
            sub_rec(index+1,s)
        sub_rec(0,0)
        return ans
    
    def combinationSum(self, candidates,target):
        ans=[]
        subset=[]
        def sub_rec(index,target):
            if(index==len(candidates)):
                if(target==0):
                    ans.append(subset.copy())
                return 
            #adding the mutiple time the same value and subtracting with the target 
            # before that checking its target value matches
            if(candidates[index]<=target):
                subset.append(candidates[index])
                sub_rec(index,target-candidates[index])
                subset.pop()
            sub_rec(index+1,target)
        sub_rec(0,target)
        return ans
    #combination sumb 2
    #we should'nt inculde again the value, plus to avoid the duplicates
    def combinationSum2(self, candidates,target):
        ans=[]
        subset=[]
        candidates.sort()
        def sub_rec(index,target):
            if(target==0):
                ans.append(subset.copy())
                return 
            #since starting for index to len(arr) we just traves 
            for i in range(index,len(candidates),1):
                if(i>index and candidates[i]==candidates[i-1]):
                    continue
                if(candidates[i]>target):
                    break
                #since the value is more confirm upcoming value wll be more
                #just break there
                subset.append(candidates[i])
                sub_rec(i+1,target-candidates[i])
                subset.pop()
        sub_rec(0,target)
        return ans
    
    def subsetSum(self,nums):
        ans=[]
        subset=[]      
        def findPowerSet(index):
            if index>=len(nums):
                ans.add(sum(subset))
                return
            subset.append(nums[index])
            findPowerSet(index+1)
            subset.pop()
            findPowerSet(index+1)
        findPowerSet(0)
        ans.sort()
        return ans
    #brute force for subset sum 2 case        
    def subsetsWithDup_brute(self, nums):
        ans=set()
        subset=[]
        def subset_rec(index):
            if(index>=len(nums)):
                subset.sort()
                ans.add(tuple(subset))
                return
            subset.append(nums[index])
            subset_rec(index+1)
            subset.pop()
            subset_rec(index+1)
        subset_rec(0)
        return ans 
    #subset sum2 find subset without duplicate
    def subsetsWithDup(self,nums):
        ans=[]
        subset=[]
        def subset_rec(index):
            #starting from empty set
            ans.append(subset.copy())
            for i in range(index,len(nums),1):
                if(i!=index and nums[i]==nums[i-1]):
                  #to remove the duplicates this check
                  #index and i make sure that we are not picking it again on the same index
                    continue
                subset.append(nums[i])
                subset_rec(i+1)
                subset.pop()
        nums.sort()
        subset_rec(0)
        return ans  
    
    def combinationSum3(self, n: int, target: int):
        ans=[]
        subset=[]
        candidates=[1,2,3,4,5,6,7,8,9] # with the space 
        def sub_rec(index,target):
            if(target==0 and len(subset)==n):
                ans.append(subset.copy())
                return 
            for i in range(index,len(candidates),1):
                subset.append(candidates[i])
                sub_rec(i+1,target-candidates[i])
                subset.pop()
        sub_rec(0,target)
        return ans
    def letterCombinations(self,digits):
        #dict to set the key and values
        #whenever the len of digits means.. the len of substring should be equal to number of button u click
        #we get the value from dict 
        #till the letters are avalaible we do the perumation 
        # we pop that particular value perumation which did and go for next one
        if len(digits) == 0:
            return []
        d={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",}
        def backtrack(index, substring):
            if len(substring) == len(digits):
                ans.append("".join(substring))
                return
            possible_letters = d[digits[index]]
            for letter in possible_letters:
                substring.append(letter)
                backtrack(index + 1, substring)
                substring.pop()
        ans = []
        backtrack(0, [])
        return ans

    def partition(self, strs):
        subset=[]
        ans=[]
        def rec_(index):
            if(index==len(strs)):
                ans.append(subset.copy())
                return
            for i in range(index,len(strs),1):
                #check palindrome then create the subset
                if(ispalindrome(strs,index,i)):
                    subset.append(strs[index:i + 1])
                    rec_(i+1)
                    subset.pop()
        def ispalindrome(s,start,end):
          while(start<=end):
            if(s[start]!=s[end]):
                return False
            start+=1
            end-=1
          return True
        rec_(0)
        return ans
    
    def exist(self, board):
        def backtrack(indexm,indexn, substring):
            if len(substring) == len(board):
                ans.append("".join(substring))
                return
            possible_letters = board[indexm][indexn]
            for letter in possible_letters:
                substring.append(letter)
                backtrack(indexm,indexn, substring)
                substring.pop()
            possible_letters = board[indexm][indexn]
            for letter in possible_letters:
                substring.append(letter)
                backtrack(indexm,indexn, substring)
                substring.pop()
        ans = []
        backtrack(0,0, [])
        return ans
    
    def exist(self, board, word):
        m=len(board)
        n=len(board[0])
        index=0
        #this to check our first letter matching the board then finding
        for i in range(0,m,1):
            for j in range(0,n,1):
                if(board[i][j]==word[index]):
                    if(self.findthepath(board,word,index,i,j,n,m)):
                        return True
        return False
    #this recursion function to find the full word is in the m*n board array
    def findthepath(self,board,word,index,row,col,n,m):
        #it means i have reached the index till the word len
        #we found the word is avalaible 
        if(index==len(word)):
            return True
        #Checking the boundaries if the character at which we are placed is not 
        #the required character
        if (row<0 or col<0 or row==m or col==n or board[row][col]!=word[index] or board[row][col]=='*'):
            return False
        #this is to prevent reusing of the same character we mark it as *
        c=board[row][col]
        board[row][col]='*'
        #we traverse top
        top=self.findthepath(board,word,index+1,row-1,col,n,m)
        #we traverse right
        right=self.findthepath(board,word,index+1,row,col+1,n,m)
        #we traverse bot
        bottom=self.findthepath(board,word,index+1,row+1,col,n,m)
        #we traverse left 
        left=self.findthepath(board,word,index+1,row,col-1,n,m)
        #then we reset it orginal
        board[row][col]=c
        return top,right,bottom,left
    

    def findthepath(self,board,word,index,row,col,n,m):
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r,c,idx):
        # if idx == len(word), then word has been found
            if idx == len(word):
                return True
        # out of bounds
        # OR current letter does not match letter on board
        # OR letter already visited
            if ( 
                r<0 or r>=ROWS 
                or c<0 or c>=COLS
                or word[idx] != board[r][c]
                or (r,c) in visited
            ):
                return False
        # to keep track of the letter already visited, add it's position to the set
        # after DFS we can remove it from the set.
            visited.add((r,c))
        # performing DFS 
            res = (
                dfs(r+1,c,idx+1) 
                or dfs(r-1,c,idx+1) 
                or dfs(r,c+1,idx+1) 
                or dfs(r,c-1,idx+1)
            )
            visited.remove((r,c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
    #*******************************************************
    #************ N Queen problem **************************
    #*******************************************************
    def solveNQueens(self, n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.traverse_board(0, board, ans, n)
        return ans
    def place(self,row,col,board,n):
        dupr=row
        dupc=col
        #three check is needed anti clock wise 45 angle to check
        while(row>=0 and col>=0):
            if(board[row][col]=='Q'):
                return False
            row-=1
            col-=1
        col=dupc
        row=dupr
        #check 90 degree angle column wise
        while(col>=0):
            if(board[row][col]=='Q'):
                return False
            col-=1
        col=dupc
        row=dupr
        #check 135 degree
        while(row<n and col>=0): 
            if(board[row][col]=='Q'):
                return False
            col-=1
            row+=1
        return True
    
    def traverse_board(self,col,board,ans,n):
        #base case when i reach the end of the board
        #i would have found the solution
        if(col==n):
            ans.append(list(board))
            return 
        #now we iterate till row 
        for row in range(0,n,1):
            if(self.place(row,col,board,n)):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.traverse_board(col+1,board,ans,n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    #rat maze problem
    def findPath(self, m, n):
        ans=[]
        vis=[[0 for _ in range(n)] for _ in range(n)]
        di=[+1, 0, 0, -1]# all directions of i,j
        dj=[0, -1, 1, 0]
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", vis, di, dj)
        return ans
    #this solve to find the correct path we are taking
    #base case is when we end n-1
    def solve(self, i: int, j: int, a, n, ans, move, vis, di, dj):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        #to go for the direction.
        dir="DLRU"
        for ind in range(4):#possible direction we make
            nexti=i+di[ind]
            nextj=j+dj[ind]
            if nexti>=0 and nextj>=0 and nexti<n and nextj<n and not vis[nexti][nextj] and a[nexti][nextj]==1:# boubdary conditions
                # if the direction we make is correct we mark it as visted
                vis[i][j]=1
                self.solve(nexti, nextj, a, n, ans,move+dir[ind], vis, di, dj)
                #if its wrong we just undo
                vis[i][j]=0

    def wordBreak(self, s, wordDict):
        checked={}
        def finddict(s,wordDict,checked):
            if (s in checked):#to check the string already there 
                return checked[s]
            if s== "":#means we have reached the end
                return True 
            for word in wordDict:
                if s.startswith(word):
                    suffix=s[len(word):]
                    #we send the suffix and check for the 
                    if finddict(suffix, wordDict,checked):
                      checked[s]=True
                      return True
            checked[s] = False 
            return False
        return finddict(s,wordDict,checked)
    
    def graphColoring(graph, m, n):
        #we try to place all colour in node
        color=[0]*n
        #color=[0,0,0,0]
        if(placeit(0,color,graph,m,n)):
            return True
        else:
            return False
    def placeit(node,color,graph,m,n):
        if(node==n):
            return True
        #we need to iterate for the color
        for i in range(1,m+1,1):
            if(safetoplace(node,color,graph,n,i)):
                color[node]=i
                #then we try next node maximum it true we return true
                if(placeit(node+1,color,graph,m,n)):
                    return True
                color[node] = 0

    def safetoplace(node, color, graph, n, col):
        for k in range(n):
            # it should'nt be same node,it should'nt be adj and already there is color 
            if k!=node and graph[k][node] == 1 and color[k] == col:
                return False
        return True
    #we need to traverse full board where there is possible to place a number
    #if its possible to place it,we send the board recursive to place other numbers
    #possible to place is a seperate function which need to be implemented
    def solveSudoku(self, board):
        self.solve(board)
        return board

    def solve(self,board):
            for i in range(0,len(board),1):
                for j in range(0,len(board[0]),1):
                    if(board[i][j]=='.'):
                        for c in "123456789":
                            if self.possible(board, i, j, c):
                                board[i][j] = c
                                if self.solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        
    #possible to check row wise,col wise
    # and inside the box wise
    def possible(self,board,row,col,c):
        for i in range(0,9,1):
            if(board[i][col]==c):
                return False
            if(board[row][i]==c):
                return False
            if(board[3*(row//3)+i//3][3*(col//3)+input%3]==c):
                return False
        return True
    

    def addOperators(self, s, target):
        ans=[]
        def findtheoperation(index,exp,Total,prevsum,s,target):
            if(index==len(s)):
                if(Total==target):
                    ans.append(exp)
                    return
            for j in range(index,len(s),1):
                if(j>index and str(s[index])=='0'):
                    break
                currentsum=int(s[index:j+1])
                if(index==0):
                    #for starting we send the starting value and set it exp
                    findtheoperation(j+1,exp+str(currentsum),currentsum,currentsum,s,target)
                else:
                    # then try all the combination  +,-
                    findtheoperation(j+1,exp+"+" +str(currentsum),Total+currentsum,currentsum,s,target)
                    findtheoperation(j+1,exp+"-" +str(currentsum),Total-currentsum,-currentsum,s,target)
                    #for * since we give importance to * first we calculate the total from current sum and subtract with the prevsum and add the prevsum *current sum
                    # 7 + 3 *2  -- > 10 -(3) + ( 3 *2 ) --- (7 +6)--13
                    findtheoperation(j+1,exp+"*" +str(currentsum),Total-prevsum +(prevsum*currentsum),prevsum*currentsum,s,target)
        findtheoperation(0,"",0,0,s,target)
        return ans 
    


r=Recursion_problems()
num =[1,2,3,4,5]
target = 6
s="leetcode"
c='efg'
ke=r.reverseStack(num)
print(ke)