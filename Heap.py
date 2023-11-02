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
        self.size-=1
        self.max_heap(self.front) # we maintain the order

        return pop

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))
    
    


# mh = maxHeap(15)
# mh.heap_insert(5)
# mh.heap_insert(3)
# mh.heap_insert(17)
# mh.heap_insert(10)
# mh.heap_insert(84)
# mh.heap_insert(19)
# mh.heap_insert(6)
# mh.heap_insert(22)
# mh.heap_insert(9)
# print("The Max val is " + str(mh.max_element()))
# print("The Max val is " + str(mh.max_element()))


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


print('The minHeap is ') 
minh = minheap(15) 
minh.heap_insert(5) 
minh.heap_insert(3) 
minh.heap_insert(17) 
minh.heap_insert(10) 
minh.heap_insert(84) 
minh.heap_insert(19) 
minh.heap_insert(6) 
minh.heap_insert(22) 
minh.heap_insert(9) 
minh.Print() 
print("The Min val is " + str(minh.min_element_get())) 
