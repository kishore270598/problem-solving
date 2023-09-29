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



