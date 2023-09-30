import time
import math
from collections import que
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
  
        


