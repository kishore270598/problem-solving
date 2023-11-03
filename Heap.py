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

    


# mh = maxHeap(6)
# mh.heap_insert(1)
# mh.heap_insert(2)
# mh.heap_insert(3)
# mh.heap_insert(6)
# mh.heap_insert(7)
# mh.heap_insert(8)
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
    
    def rearrange(self,arr,n):
        for i in range((n-2)//2,-1,-1):#to start from rightmost parent
            self.heapify(arr, i, n)
        print(arr)



   
s=sol()
arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
print(s.rearrange(arr,len(arr)))


        











print('The minHeap is ') 
minh = minheap(15) 
# minh.heap_insert(5) 
# minh.heap_insert(3) 
# minh.heap_insert(17) 
# minh.heap_insert(10) 
# minh.heap_insert(84) 
# minh.heap_insert(19) 
# minh.heap_insert(6) 
# minh.heap_insert(22) 
# minh.heap_insert(9) 
minh.Print() 
# print("The Min val is " + str(minh.min_element_get())) 


arr = [90, 100, 10, 7, 12, 2, 7, 3]  
n = len(arr) - 1

if minh.validheap(arr, n,0): 
    print("Yes") 
else: 
    print("No") 