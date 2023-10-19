import time
import math
from collections import deque 
class Stack:
    def __init__(self, capacity: int):
        self.stack=[0]*capacity
        self.tops=-1
        self.capacity=capacity

    def push(self, num: int) -> None:
        if(self.isFull()):
            return 
        self.tops+=1
        self.stack[self.tops]=num

    def pop(self) -> int:
        if(self.tops!=-1):
            self.tops-=1
            return self.stack[self.tops+1]
        else:
            return -1

    def top(self) -> int:
        if(self.tops!=-1):
            return self.stack[self.tops]
        else:
            return -1 
    
    def isEmpty(self) -> int:
        if(self.tops==-1):
            return 0
        else:
            return 1

    def isFull(self) -> int:
        if(self.tops==self.capacity-1):
            return 1
        else:
            return 0

    def stackSize(self):
        return self.tops

#NORMAL QUE IMPLEMENTAION 
class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr= [0] * 100001 # instead of n i took the size 
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        self.arr[self.rear%100001]=e
        self.rear+=1


    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if(self.arr[self.front]==-1):
            return -1
        elif(self.front==self.rear):
            return -1
        else:
            temp=self.arr[self.front]
            self.arr[self.front%100001]=-1
            self.front+=1
            return temp
        
##################################
#implemention of stack using 2 que
#################################
class MyStack:
    #2 que implemention of stack using que
    def __init__(self):
      self.q1 =deque()
      self.q2 =deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
       
    #adding element into q2
    #when it added first element which will be left out in stack
    #since we give len >1 that will remain still
    # we will pop it
    def pop(self) -> int:
      while(len(self.q1)>1):
        self.q2.append(self.q1.popleft())

      popped_element=self.q1.popleft()
      self.q1,self.q2=self.q2,self.q1
      return popped_element
    #since we give len >1 that will remain still
    # that will be out top
    def top(self) -> int:
        while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            
        top_element = self.q1[0]   
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
      if(len(self.q1)==0):
        return True
      else:
        return False 

##################################
#implemention of stack using 1 que
#################################
    def __init__(self):
        self.q1 =deque()
    #we just keep the values in top so till the size is there we pop and top
    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1) - 1):
            self.q1.append(self.q1.popleft())
       
    def pop(self) -> int:
      return self.q1.popleft()


    def top(self) -> int: 
        return self.q1[0] 

    def empty(self) -> bool:
      if(len(self.q1)==0):
        return True
      else:
        return False
##########################################
#implement que using stack
##########################################
from queue import LifoQueue
class MyQueue:
 # we declare 2 ques
    def __init__(self):
      self.input =LifoQueue()
      self.output =LifoQueue()
 # step1 to push we get the existing  records input and put in output
 # step2 then we insert x 
 # step3 then reverse of step 1 to follow the que [First in first out ]

    def push(self, x: int) -> None:
      while not self.input.empty():
        self.output.put(self.input.get())
      self.input.put(x)
      while not self.output.empty():
        self.input.put(self.output.get())

        
    def pop(self) -> int:
        if self.input.qsize() == 0:
          return -1
        val = self.input.get()
        return val
        
    def peek(self) -> int:
        if self.input.qsize() == 0:
          return -1
  
        return self.input.queue[-1]
        

    def empty(self) -> bool:
      if(self.input.qsize()==0):
        return True
      else:
        return False

#linked list using stack
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
        self.top=None
        self.size=0
 
    def getSize(self):
        return self.size

    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False
#we will create a node
#once the node is create we need to make that as top
#so we make our current new node next as the old top
#then we assign it to the top
    def push(self, data):
        node=Node(data,None)
        node.next=self.top
        self.top=node
        self.size+=1


    def pop(self):
        if(self.top==None):
            return -1
        else:
            topdata=self.top.data
            stackNode= self.top
            self.top=self.top.next
            self.size-=1
        return topdata

    def getTop(self):
        return self.top.data
  
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Que:
    def __init__(self):
        self.front=None
        self.rear=None
    def enque(self,val):
        if(self.rear==None):
            self.head=Node(val)
            self.rear=self.head
        else:
            self.rear=Node(val)
            self.rear=self.rear.next
    
    def deque(self):
        if self.front is None:
            return None
        else:
            temp = self.front.data
            self.front = self.front.next
            return temp
        
class MinStack:

    def __init__(self):
      self.stack=[]
      self.stack2=[]

     #stack 2 to calculate the min value tracking it
     #    
    def push(self, val: int) -> None:
      self.stack.append(val)
      if self.stack2:
        temp=min(val,self.stack2[len(self.stack2)-1])
        self.stack2.append(temp)
      else:
        self.stack2.append(val)
                 
    def pop(self) -> None:
      
        self.stack.pop()
        self.stack2.pop()


    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        
    def getMin(self) -> int:
      return self.stack2[len(self.stack2)-1]

    def infixToPostfix(self,exp):
        bodmas = {'^': 3,'*': 2,'/': 2,'+': 1,'-': 1,'(': 0,')': 0}
        result=''
        stack=[]
        for c in exp:
            if(c.isdigit() or c.isalpha()):
                #if its  numeric u add it
                result+=c
            elif(c=='('):
                stack.append(c)
            elif(c==')'):
                #when u reach a part of operation is completed
                # whatever u have stacked in stack u just append it
                while( stack[-1]!= '('):
                    result+=stack.pop()
                
                stack.pop()
            else:
                #if the current operator is lesser than the old one 
                # it means the current operator is lesser to old one.. that need to be closed
                while  len(stack) and bodmas[stack[-1]] >= bodmas[c]:
                    result+=stack.pop()
                stack.append(c)
        #to append all the operators left
        while (len(stack)):
            result+=stack.pop()
        return result

    #Prefix to Infix Conversion    
    def prefixToInfixConversion(self,s: str) -> str:
        stack=[]
        result=''
        bodmas = {'^': 3,'*': 2,'/': 2,'+': 1,'-': 1,'(': 0,')': 0}
        for c in s:
            if(c.isdigit() or c.isalpha()):
                ##check
                stack.append(c)
                while(len(stack)>=3  and stack[-1] not in bodmas and stack[-2] not in bodmas ):
                    op1=stack.pop()
                    op2=stack.pop()
                    op=stack.pop()  
                    result='('+op2+op+op1+')'
                    stack.append(result)
            else:
                stack.append(c)
        return stack[-1]
            
    #Convert Prefix to Postfix  
    # reverse and whenever u see the operator just pop the 2 tops of stack and create a combination 
    # and add to its stack 
    # then return the stack     
    def preToPost(self,s: str) -> str:
        stack=[]
        result=''
        bodmas = {'^': 3,'*': 2,'/': 2,'+': 1,'-': 1,'(': 0,')': 0}
        for i in range(len(s)-1,-1,-1):
            if (s[i].isalpha() or s[i].isdigit()):
                stack.append(s[i])
            else:
                a=stack.pop()
                b=stack.pop()
                result=a+b+s[i]
                stack.append(result)
        return stack[-1]
    #postfix to prefix
    #  ab+cd-* --- > *+ab-cd 
    # whenever u see digit or alpha just append to stack
    # whenever u see the  operator pop the top of the stack 2 operand 
    # add a temp as ( operator + second top + first top) then append into stack
    def postfixToPrefix(self,s: str) -> str:
        stack=[]
        result=''
        for c in s:
            if(c.isdigit() or c.isalpha()):
                stack.append(c)
            elif(len(stack)>=2):
                op2=stack.pop()
                op1=stack.pop()
                result=c+op1+op2
                stack.append(result)
        return stack[-1]

    def postToInfix(self,postfix: str) -> str:
        #ab+c+ to  ((a+b)+c)
        stack=[]
        resul=''
        for c in postfix:
            if(c.isdigit() or c.isalpha()):
                stack.append(c)
            elif(len(stack)>=2):
                op=c
                op1=stack.pop()
                op2=stack.pop()
                result='('+op2+op+op1+')'
                stack.append(result)
        return stack[-1]
    
    def infixToprifx(self,exp):
        #first infix to postfix
        #postfix to prefix
        bodmas = {'^': 3,'*': 2,'/': 2,'+': 1,'-': 1,'(': 0,')': 0}
        result=''
        stack=[]
        for c in exp:
            if(c.isdigit() or c.isalpha()):
                #if its  numeric u add it
                result+=c
            elif(c=='('):
                stack.append(c)
            elif(c==')'):
                #when u reach a part of operation is completed
                # whatever u have stacked in stack u just append it
                while( stack[-1]!= '('):
                    result+=stack.pop()
                
                stack.pop()
            else:
                #if the current operator is lesser than the old one 
                # it means the current operator is lesser to old one.. that need to be closed
                while  len(stack) and bodmas[stack[-1]] >= bodmas[c]:
                    result+=stack.pop()
                stack.append(c)
        #to append all the operators left
        while (len(stack)):
            result+=stack.pop()
        n=[]
        k=''
        print(result)
        for c in result:
            print('1')
            if(c.isdigit() or c.isalpha()):
                n.append(c)
            elif(len(n)>=2):
                op=c
                op1=n.pop()
                op2=n.pop()
                k='('+op2+op+op1+')'
                n.append(result)
        return n[-1]
    #Next Greater Element only right
    def nextGreaterElement_brute(self, nums1, nums2):
        result=[]
        flag=0
        for i in range(0,len(nums1),1):
            flag=0
            for j in range(i+1,len(nums2),1):
                if(nums1[i]<nums2[j]):
                    result.append(nums2[i])
                    flag=1
                    break
            if(flag==0):
                result.append(-1)
        return result
    #Next Greater Element only right
    def nextGreaterElement(self,nums2):
        #we create a stack
        #traverse from last element of array and compare with the stack 
        # if the stack top not greater than the current element then pop and find the other element
        # then once finding the greater element.  append the current array element 
        stack=[]
        result=[0]*(len(nums2))
        for i in range(len(nums2)-1,-1,-1):
            while(len(stack)!=0 and stack[-1]<=nums2[i]):
                stack.pop()
            if(len(stack)!=0):
                result[i]=stack[-1]
            else:
                result[i]=-1
            stack.append(nums2[i])  
        return result 
    #circle array type 2
    # we have to follow the first method but we need to run twice the array so
    # 2n-1 and to acces the index i%n
    def nextGreaterElements_2(self, nums):
        stack=[]
        n=len(nums)
        result=[0]*n
        for i in range(2*(n-1),-1,-1):
            while(len(stack)!=0 and stack[-1]<=nums[i%n]):
                stack.pop()
            if(i<n):
                if(len(stack)!=0):
                    result[i]=stack[-1]
                else:
                    result[i]=-1
            stack.append(nums[i%n])
        return result 
    
    def immediateSmaller(self,nums):
        stack=[]
        result=[0]*(len(nums))
        for i in range(len(nums)-1,-1,-1):
            if(len(stack)==0):
                stack.append(nums[i])
                result[i]=-1
            elif(nums[i]>stack[-1]):
                result[i]=stack[-1]
            else:
                result[i]=-1
            stack.pop()
            stack.append(nums[i])
        return result  
    #Trapping Rain Water
    # we need to take 2 pointers left ,right 
    # leftmax and right max
    # whenever u check the left height is less than right height 
    # you find the max of left , if its not max then calculate 
    # which means we have found the left max for the current index
    #when we see left element is greater than the right element we start find the right max as above steps
    def trap(self, height): 
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        rainstored=0
        while(left<=right):
            if(height[left]<=height[right]):
                if(height[left]>=leftmax):
                    leftmax=height[left]
                    #to make sure we are holding the max building
                else:
                    rainstored+=leftmax-height[left]
                    #to calculate the drop
                left+=1
            else:
                if(height[right]>=rightmax):
                    rightmax=height[right]
                else:
                    rainstored+=rightmax-height[right]
                right-=1
        return rainstored
    def sumSubarrayMins_brute(self, arr) -> int:
        sum_=0
        for i in range(0,len(arr),1):
            for j in range(i+1,len(arr)+1,1):
                sum_+=min(arr[i:j])
        print(sum_)

    def sumSubarrayMins(self, arr) -> int:
        stack=[]
        arr=[-math.inf] + arr + [-math.inf] 
        sum_=0
        for i in range(0,len(arr),1):
            while (len(stack)!=0 and arr[stack[-1]]>arr[i]):# increasing motonic stack
                mid=stack.pop()
                left=stack[-1] # this will give be holding last min element
                right=i#next smaller element 
                sum_+=arr[mid]*(mid-left) * (right-mid)
            stack.append(i)

        return sum_ 
    

    def asteroidCollision(self, asteroids):
        stack=[]
        # 10 2 -5 
        #collision condition when over asteroids is negative and stack is postive

        for element in asteroids:
            while len(stack)!=0 and element <0 and stack[-1]>0:
                if((element + stack[-1]) <0):
                    stack.pop()
                elif((element +stack[-1])>0):
                    element=0
                    #element is destoryed since postive
                else:
                  # both are equal so destory both
                    element=0
                    stack.pop()
            if (element!=0):
                stack.append(element)
        return stack
    def subArrayRanges_brute(self, arr):
        diff=0
        for i in range(0,len(arr),1):
            for j in range(i+1,len(arr)+1,1):
                diff+=max(arr[i:j])-min(arr[i:j])
        return diff
    def subArrayRanges(self, arr):
        stack=[]
        min_sum=0
        max_sum=0
        for next_smaller in range(0,len(arr)+1,1):
            while( len(stack)!=0 ) and  (next_smaller==len(arr) or arr[stack[-1]]>arr[next_smaller]):#increasing motonic stack
                mid=stack.pop()
                if(stack):
                    previous_smaller=stack[-1]
                else:
                    previous_smaller=-1 #before assignment it acts as - infinity
                min_sum+=arr[mid]*(mid-previous_smaller) * (next_smaller-mid)
            stack.append(next_smaller)
        stack=[]
        for next_larger in range(0,len(arr)+1,1):
            while( len(stack)!=0 ) and  (next_larger==len(arr) or arr[stack[-1]]<arr[next_larger]): #decreasing motonic stack
                mid=stack.pop()
                if(stack):
                    previous_larger=stack[-1]
                else:
                    previous_larger=-1#before assignment it acts as - infinity
                max_sum+=arr[mid]*(mid-previous_larger) * (next_larger-mid)
            stack.append(next_larger)    
        return max_sum-min_sum
    #increasing motonic stack
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for element in num:
            while k>0 and stack and  stack[-1]>element:
                stack.pop()
                k-=1
            if stack or element is not '0':
              stack.append(element)
        stack=stack[:len(stack)-k]
        res="".join(stack)
        if res:
            return res
        else:
            return "0"
    #Largest rectangle in a histogram    
    def largestRectangleArea(self, heights) -> int:
        stack=[]
        max_=0
        for i in range(0,len(heights)+1,1):# to include the last index to make sure we clear all the monotonic stack
            while len(stack)!=0 and (i==len(heights) or heights[stack[-1]]>=heights[i]) :
                #we have reached the boundary i th place
                # height will be the previous height 
                # i will be the right boundary
                # stack pop will hold the left min value of the height
                # we use the formula to find ( if stack is empty means there is no boundary height * width (i))
                # if stack is there  (i (left bounadry ) - stack.top which holds the min of left  -1 to index) 
                # this will provie width and  * height 
                hist=heights[stack[-1]]
                stack.pop()
                if len(stack)==0:
                    width =i
                else:
                    width= i - stack[-1] -1 
                max_=max(max_,width * hist)
            stack.append(i)
        return max_
    
    def maximalRectangle(self, matrix):
      #same as histogram problem we will store the montonic stack 
      # using boundaries we find the width and height
      # since its a matrix we keep adding the value 1 in the array height
      # using that height we will find the height and width for the current row
      #till we reach the end of the row we will be able to find the  max rectangle 
      if not matrix or not matrix[0]:
        return 0 
      stack=[]
      c= len(matrix)
      r=len(matrix[0])
      height=[0]*(r+1)
      width=0
      max_=0
      breath=0
      for row in matrix:
        for i in range(r):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack=[-1]
        for i in range(0,r+1,1):
          while height[i]<height[stack[-1]]:
            width=stack.pop()
            if stack:
              breath=i-stack[-1]-1
            else:
              breath=i
            max_=max(max_,height[width]* breath)
          stack.append(i)
      return max_
    
    
    def maxSlidingWindow(self, nums, k):
        dq=deque()
        ans=[]
        # Sliding Window Maximum
        # --------------------------
        # to hold a sub array of K we will use deque data structure
        # storing the element index in decreasing order element
        # whenever we reach a stack K sub array size
        # we pop the left most element that is front element
        # when the element contains the lesser value than 
        # the current index we pop the element and make sure we
        # just hold the maximum value .
        for i in range(0,len(nums),1):
            if (len(dq)!=0 and dq[0]== i-k):# to make sure we don't hold any index outside the K(subarray)
                dq.popleft()
            while len(dq)!=0 and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if(i>=k-1):#adding every subarray max
                ans.append(dq[0])
        return ans
    
class StockSpanner:

    def __init__(self):
        self.stack=[] # stack= (Price,span)
        #montonic stack and if current value is less the stack  we just keep that lesser value and add their span to maintain montonic decreasing stack
        
    def next(self, price: int) -> int:
        span=1
        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))

        return span
    
    
# '''
#     This is signature of helper function 'knows'.
#     You should not implement it, or speculate about its implementation.

#     def knows(int A, int B); 
#     Function 'knows(A, B)' will returns "true" if the person having
#     id 'A' knows the person having id 'B' in the party, "false" otherwise.
# '''

# def findCelebrity(n, knows):
#         stack=[]
#         potentialCelebrity=0
#         for i in range(0,n,1):
#             stack.append(i)
#         print(stack)
#         while(len(stack)=>2):
#             a=stack.pop()
#             b=stack.pop()
#             if(knows(a,b)==1):
#                 stack.append(b)
#             else:
#                 stack.append(a)

#         potentialCelebrity=stack.pop()
#         flag=True
#         for i in range(0,n,1):
#             if(i!=potentialCelebrity):
#                 if(knows(potentialCelebrity,i)==1 or knows(i,potentialCelebrity)==0):
#                     flag=false
#                     break
        
#         if(flag==True):
#             return potentialCelebrity
#         else:
#             return -1 


class lruCache:
        def __init__(self,capacity):
            self.capacity=capacity #size
            self.cache = deque() # to acces back and front
            self.dicty = {} #holds a address

        def get(self, key: int) -> int:
            if key not in self.dicty:
                return -1
            else:
                self.cache.remove(key)
                self.cache.appendleft(key)# to make it recent
                val=self.dicty[key]
            return val
        
        def put(self, key, value):
            if key not in self.dicty:
                if(len(self.cache)==self.capacity):# to check whether we have crossed the capacity
                    oldest=self.cache.pop() # right most will be least used
                    del self.dicty[oldest] # delete from address 
                    self.dicty[key]=value # add into first to make it recently used
                    self.cache.appendleft(key)
                else:
                    self.dicty[key] = value
                    self.cache.appendleft(key)
            else:
                self.cache.remove(key)  #remove the old 
                self.dicty[key] = value 
                self.cache.appendleft(key) #make it as recently used
        




   


    





    
         



            

                  
m=MinStack()
a='a+b*(c^d-e)^(f+g*h)-i'
nums1 = [2,4]
nums2 = [4 ,7 ,8 ,2, 3, 1]
ans=m.findCelebrity(1,2)
print(ans)



             

        

                

            
