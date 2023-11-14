import heapq
from collections import Counter
from collections import deque 
class maxHeap:
    def __init__(self,max_size):
        self.max_size=max_size
        self.heap=[0]*(max_size+1) # heap array
        self.size=0 #to maintain the size (tracking)
        self.heap[0]=9999999
        self.front=1
    
    def parent(self,pos):
        return pos//2
    
    def leftchild(self,pos):
        return 2*pos +1
    
    def rightchild(self,pos):
        return 2* pos
    
    def swap_(self,startpos,endpos):#to swap the elements 
        self.heap[startpos],self.heap[endpos]=self.heap[endpos], self.heap[startpos]

    def isLeaf(self, pos): # to check whether the current pos is a leaf so it should be greater than the parent
        #and lesser than the size
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False 

    #heap insertion
    # we always insert the element at the last
    def heap_insert(self,element):
        if self.size>=self.max_size:
            #we have reached the limit
            return
        print(self.heap)
        print(self.size)
        self.size+=1

        self.heap[self.size]=element
        current=self.size
        while self.heap[current]>self.heap[self.parent(current)]:#we swap the element
            self.swap_(current,self.parent(current))
            current=self.parent(current)
    
    #before deleting we need to implement a maxheap to main the struture
    def max_heap(self,pos):
        # to check whether the current pos is a leaf so it should be greater than the parent
        #and lesser than the size
        if not self.isLeaf(pos):
            if (self.heap[pos] < self.heap[self.leftchild(pos)] or
                self.heap[pos] < self.heap[self.rightchild(pos)]):
                # which means we are not following the strutture 
                if (self.heap[self.leftchild(pos)] > 
                    self.heap[self.rightchild(pos)]):
                    self.swap_(pos, self.leftchild(pos))
                    self.max_heap(self.leftchild(pos)) # to keep on checking the branch
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap_(pos, self.rightchild(pos))
                    self.max_heap(self.rightchild(pos))

    def max_element(self): #delete
        pop=self.heap[self.front]
        self.heap[self.front]=self.heap[self.size] # we swap the last element to the starting
        self.heap[self.size]=pop
        self.size-=1
        self.max_heap(self.front) # we maintain the order

        return pop

    def Print(self):
        print(self.heap)
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))

    

# mh = maxHeap(7)
# mh.heap_insert(5)
# mh.heap_insert(2)
# mh.heap_insert(4)
# mh.heap_insert(1)
# mh.heap_insert(3)
# mh.heap_insert(6)
# mh.heap_insert(0)
# print(str(mh.Print()))


class minheap:
    def __init__(self,max_size):
        self.max_size=max_size
        self.heap=[0]*(max_size+1) # heap array
        self.size=0 #to maintain the size (tracking)
        self.heap[0]=-9999
        self.front=1
    
    def parent(self,pos):
        return pos//2
    
    def leftchild(self,pos):
        return 2*pos +1
    
    def rightchild(self,pos):
        return 2* pos
    
    def swap_(self,startpos,endpos):#to swap the elements 
        self.heap[startpos],self.heap[endpos]=self.heap[endpos], self.heap[startpos]

    def isLeaf(self, pos): # to check whether the current pos is a leaf so it should be greater than the parent
        #and lesser than the size
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False 

    #heap insertion
    # we always insert the element at the last
    def heap_insert(self,element):
        if self.size>=self.max_size:
            #we have reached the limit
            return
        self.size+=1
        self.heap[self.size]=element
        current=self.size
        while self.heap[current]<self.heap[self.parent(current)]:#we swap the element
            self.swap_(current,self.parent(current))
            current=self.parent(current)
    
    #before deleting we need to implement a minheap to main the struture
    def min_heap(self,pos):
        # to check whether the current pos is a leaf so it should be min than the parent
        #and lesser than the size
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftchild(pos)] or
                self.heap[pos] > self.heap[self.rightchild(pos)]):
                # which means we are not following the strutture 
                if (self.heap[self.leftchild(pos)] < 
                    self.heap[self.rightchild(pos)]):
                    self.swap_(pos, self.leftchild(pos))
                    self.min_heap(self.leftchild(pos)) # to keep on checking the branch
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap_(pos, self.rightchild(pos))
                    self.min_heap(self.rightchild(pos))

    def min_element_get(self): #delete
        pop=self.heap[self.front]
        self.heap[self.front]=self.heap[self.size] # we swap the last element to the starting
        self.size-=1
        self.minHeap_all() # we maintain the order
        return pop
    
    def minHeap_all(self): 
        for pos in range(self.size//2, 0, -1): 
            self.min_heap(pos) 
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))

    #to chek whether the heap is valid
    def validheap(self,heap,n,i):
        #base case of recursion
        if(i>=int((n-1)/2)):
            return True 

        if(heap[i]>=heap[2*i+1] and heap[i]>=heap[2*i+2] and self.validheap(heap,n,2*i+1)
            and  self.validheap(heap,n,2*i+2) ):
                return True
        else:
            return False




class sol:
    #to main a heap we need heapify
    #converting Min to max
    # we start from right most botton of the parent and keep checking its maintaing a max heap , else we swap and keep in track
    def heapify(self,heap,pos,n):
        leftchild=2*pos+1
        rightchild=2*pos+2
        largest=pos #assumption
        
        if leftchild< n and heap[largest] <heap[leftchild]:
            largest=leftchild
        if rightchild <n and heap[largest] <heap[rightchild]:
            largest=rightchild
        if largest!=pos:
         # we have found a parent lesser than child
            heap[pos],heap[largest]=heap[largest],heap[pos]
            self.heapify(heap, largest, n)
  
# s=sol()
# arr = [3,2,3,1,2,4,5,5,6]
# print(s.rearrange(arr,len(arr)))

class Mproblems_heap:   
    def rearrange(self,arr,n):
        for i in range((n-2)//2,-1,-1):#to start from rightmost parent
            self.heapify(arr, i, n)
        print(arr)

    def findKthLargest(self, nums, k):
        #heap_insert
        heap=[0]*(len(nums)+1)
        heap[0]=9999999
        n=len(nums)
        size=0
        def insert_heap(nums,element,n,heap,size):
            if size>=n:
                #we have reached the limit
                return
            heap[size]=element
            current=size
            while heap[current]>heap[current//2]:#we swap the element
                heap[current],heap[current//2]=heap[current//2],heap[current]
                current=current//2
        for element in nums:
            size+=1
            insert_heap(nums,element,n,heap,size)
        print(heap)
        heap.pop(0)
        print(heap,size)
        pos1=len(nums)
        def isLeaf(pos,n): # to check whether the current pos is a leaf so it should be greater than the parent
        #and lesser than the size
            if pos >= (n//2) and pos <= n:
                return True
            return False 
        #--------------------------------------------------------
        def max_heap(pos,heap,n):
            # to check whether the current pos is a leaf so it should be greater than the parent
            #and lesser than the size
            leftchild=2*pos+1
            rightchild=2*pos+2
            if not isLeaf(pos,n):
                if (heap[pos] < heap[leftchild] or
                    heap[pos] < heap[rightchild]):
                    # which means we are not following the strutture 
                    if (heap[leftchild] > 
                        heap[rightchild]):
                        heap[pos],heap[leftchild]=heap[leftchild],heap[pos]
                        max_heap(leftchild,heap,n) # to keep on checking the branch

                    # Swap with the right child and heapify
                    # the right child
                    else:
                        heap[pos],heap[rightchild]=heap[rightchild],heap[pos]
                        max_heap(rightchild,heap,n)
        #--------------------------------------------------------
        size=-1
        while (pos1>0):
            pop=heap[0]
            heap[0]=heap[size] # we swap the last element to the starting
            heap[size]=pop
            size-=1
            max_heap(0,heap,n) # we maintain the order
            pos1-=1
        print(heap)
        

class heapsort:
    #to main a heap we need heapify
    #converting Min to max
    # we start from right most botton of the parent and keep checking its maintaing a max heap , else we swap and keep in track
    def heapify(self,heap,pos,n):
        leftchild=2*pos+1
        rightchild=2*pos+2
        largest=pos #assumption
        
        if leftchild< n and heap[largest] <heap[leftchild]:
            largest=leftchild
        if rightchild <n and heap[largest] <heap[rightchild]:
            largest=rightchild
        if largest!=pos:
         # we have found a parent lesser than child
            heap[pos],heap[largest]=heap[largest],heap[pos]
            self.heapify(heap, largest, n)
    
    def element_insert_heap(self,arr):
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr,i,n)
        #first we just heapify the array by checking the each pos from bot right node to the parent and we make it as max heap
        # then we take position from right most leaf and swap to the element first element since the max element is first we swap with the last to make a increasing 
        #array (heap sort )
        for i in range(n-1,-1,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,0,i)
        return arr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    

class Solution:
    def mergeKLists(self, lists):
        a=[]
        n=len(lists)
        for i in range(n):
            head=lists[i]
            while(head!=None):
                a.append(head.val)
                head=head.next
        a=self.element_insert_heap(a)
        root = None
        for i in range(0, len(a), 1): 
            root = self.insert(root, a[i]) 
        
        return root 

    def insert(self,root, item): 
        temp = ListNode(item,None) 
        
        if (root == None): 
            root = temp 
        else : 
            ptr = root 
            while (ptr.next != None): 
                ptr = ptr.next
            ptr.next = temp 
        
        return root 

        
    def heapify(self,heap,pos,n):
        leftchild=2*pos+1
        rightchild=2*pos+2
        largest=pos #assumption
        
        if leftchild< n and heap[largest] <heap[leftchild]:
            largest=leftchild
        if rightchild <n and heap[largest] <heap[rightchild]:
            largest=rightchild
        if largest!=pos:
         # we have found a parent lesser than child
            heap[pos],heap[largest]=heap[largest],heap[pos]
            self.heapify(heap, largest, n)
    
    def element_insert_heap(self,arr):
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr,i,n)
        #first we just heapify the array by checking the each pos from bot right node to the parent and we make it as max heap
        # then we take position from right most leaf and swap to the element first element since the max element is first we swap with the last to make a increasing 
        #array (heap sort )
        for i in range(n-1,-1,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,0,i)
        return arr
        

#Replace Each Element Of Array With Its Corresponding Rank
class Rank:
    def heapify(self,heap,pos,n):
        leftchild=2*pos+1
        rightchild=2*pos+2
        largest=pos #assumption
        
        if leftchild< n and heap[largest] <heap[leftchild]:
            largest=leftchild
        if rightchild <n and heap[largest] <heap[rightchild]:
            largest=rightchild
        if largest!=pos:
         # we have found a parent lesser than child
            heap[pos],heap[largest]=heap[largest],heap[pos]
            self.heapify(heap, largest, n)
    
    def element_insert_heap(self,arr):
        temp_arr=[]
        temp_arr=arr
        for i in range(0,len(arr),1):
            temp_arr[i]=arr[i]
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr,i,n)
        #first we just heapify the array by checking the each pos from bot right node to the parent and we make it as max heap
        # then we take position from right most leaf and swap to the element first element since the max element is first we swap with the last to make a increasing 
        #array (heap sort )
        for i in range(n-1,-1,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,0,i)
        
        ranks={}
        temp=1
        for i in range(0,len(arr),1):
            if(arr[i] not in ranks):
                ranks[arr[i]]=temp
                temp+=1
        k=[]
        for i in range(0,len(temp_arr),1):
            if temp_arr[i] in ranks:
                k.append(ranks[temp_arr[i]])

        print(k)
        

# r=Rank()
# lists = [4,7,2,90,90]
# print(r.element_insert_heap(lists))






# m=Mproblems_heap()   
# nums=[3,2,3,1,2,4,5,5,6]
# k =4
# print(m.findKthLargest(nums,k))



# print('The minHeap is ') 
# minh = minheap(15) 
# # minh.heap_insert(5) 
# # minh.heap_insert(3) 
# # minh.heap_insert(17) 
# # minh.heap_insert(10) 
# # minh.heap_insert(84) 
# # minh.heap_insert(19) 
# # minh.heap_insert(6) 
# # minh.heap_insert(22) 
# # minh.heap_insert(9) 
# minh.Print() 
# # print("The Min val is " + str(minh.min_element_get())) 


class Hand:
    #we need to check whether the len is divisible to create as group size
    #sine its should be consecutive we use a hashmap to do a count 
    # we need a heap min 
    def isNStraightHand(self, hand, groupSize):
        if(len(hand)%groupSize!=0):
            return False
        count={}
        for element in hand:
            count[element]=1 +count.get(element,0)
        minH=list(count.keys())
        heapq.heapify(minH)
        while minH:
            first=minH[0]
            for i in range(first,first+groupSize,1):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    #THIS will be break the condition where we miss the min value with the consecutive values
                    # always we need to pop the minheap 0 index value
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

    def leastInterval(self, tasks, n):
        #Input: tasks = ["A","A","A","B","B","B"], n = 2
        # Output: 8
        # Explanation: 
        # A -> B -> idle -> A -> B -> idle -> A -> B
        # There is at least 2 units of time between any two same tasks.
        #INT WE NEED TO TAKE THE MAXIMUM VALUE AND FILL WITH THE OTHER TASK
        #we required a maxheap,a que to hold the time and the count
        #the count of characters hashmap
        count={}
        
        time=0 #to maintain when we can add another task 
        time_c=deque() #[2 valuescount which holds the used task ,time when it can be avalaible to add]
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        while maxHeap or time_c:
            time+=1
            if maxHeap:
                cnt=1+ heapq.heappop(maxHeap) # since we are taking negatvie we are decrementing 
                if cnt!=0:
                    time_c.append([cnt,time+n])
            if time_c and time_c[0][1]==time: #possible to add the task in our 
                heapq.heappush(maxHeap,time_c.popleft()[0])
                
        return time
    
    def topKFrequent(self, nums, k):
        #we will be holding a each freq of len size that is maximum freq of a digit can occur
        # in that freq index we will be holding the list
        #************bucket sort******************
        count={}
        freq=[[] for i in range(0,len(nums)+1,1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        print(count.items())
        #dict_items([(1, 3), (2, 2), (3, 2)])
        #nums = [1,1,1,2,2,3,3] for the below line so for frq we will be holding the values
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(nums),-1,-1):
            for n in freq[i]:#for each freq it contains a list
                res.append(n)
                if(len(res)==k):
                    return res
class Solution:
    def solveA(self, A, B, c):
        maxHeap_a=[-element for element in A]
        maxHeap_b=[-element for element in B]
        heapq.heapify(maxHeap_a)
        heapq.heapify(maxHeap_b)
        a=0
        z=[]
        for i in range(0,len(A),1):
            for j in range(0,len(B),1):
                z.append(-(maxHeap_a[i]+maxHeap_b[j]))
        z=sorted(z)
        z=z[::-1]
        print(z)
        return z[0:c]
    def solve(self, A, B, K):
        n=len(A)
        ans = []
        A.sort()
        B.sort()
        pq = []
        index = set()
        #conifrm last 2 elements are must be highest combination so we add it and add it in set 
        #in this set we hold the index
        heapq.heappush(pq, (A[-1] + B[-1], (n - 1, n - 1)))
        index.add((n - 1, n - 1))
    
        while K > 0:
            p = heapq.heappop(pq)
            sum_val, (i, j) = p
            ans.append(sum_val)
            #checking the diagonals to check the sum and maintaing the heap
            if (i - 1, j) not in index:
                heapq.heappush(pq, (A[i - 1] + B[j], (i - 1, j)))
                index.add((i - 1, j))
    
            if (i, j - 1) not in index:
                heapq.heappush(pq, (A[i] + B[j - 1], (i, j - 1)))
                index.add((i, j - 1))
    
            K -= 1
    
        return ans
class codeninja:
    def ropes(self,arr):
        #we hold as stack and put inside the heap and add to it
        #Connect `n` ropes with minimal cost
        minHeap=[element for element in arr]
        first=0
        second=0
        heapq.heapify(minHeap)
        print(minHeap)
        res=0
        while (len(minHeap)>1):
            first=heapq.heappop(minHeap)
            second=heapq.heappop(minHeap)
            res+=first+second
            heapq.heappush(minHeap,first+second)
        return res
    
class MedianFinder:

    def __init__(self):
        #large,small heap  min heap,max heap
        #we need to maintian 
        self.large,self.small=[],[] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1 * num)
        #to maintain the small heap will hold always the value less the the large heap
        # since 0 index holds max value and min value 
        if(self.small and self.large and (-1 * self.small[0] >self.large[0])):
            val=-1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        #if the len has more
        if len(self.small) >len(self.large)+1 :
            val=-1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small)+1 :
            val= heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
    
    def findMedian(self) -> float:
        if (len(self.small) > len(self.large)):
            return -1 *self.small[0]
        if (len(self.large) > len(self.small)):
            return self.large[0]
        return (-1* self.small[0] +self.large[0])/2



r=MedianFinder()
A = [4,3,2,6]
print(r.median(A))

