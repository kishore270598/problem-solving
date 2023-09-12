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
    def printAllSubsequence(self,input_str, output_str):
        if len(input_str) == 0:
            print(output_str, end="\n")
            return
        self.printAllSubsequence(input_str[1:], output_str+input_str[0])
        self.printAllSubsequence(input_str[1:], output_str)


r=Recursion_problems()
k="abc"
ans=r.printAllSubsequence(k,"")
print(ans)