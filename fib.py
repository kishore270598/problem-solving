import time
class Recursion:
    def fib(self,n):
        firstterm=1
        secondterm=1
        z=[]
        if(n<=0):
            return z
        z.append(firstterm)
        if(n<=1):
            return z
        z.append(secondterm)
        n=n-2
        while(n>0):
            n-=1
            nextterm=firstterm+secondterm
            firstterm=secondterm
            secondterm=nextterm
            z.append(nextterm)
        return z
    def fibrec(self,n):
        if(n<=0):
            return []
        if(n<=1):
            return [1]
        return self.fibrec1(1,1,[1,1],n-2)
    def fibrec1(self,first,second,arr,n):
        if(n==0):
            return arr
        next = first+second
        arr.append(next)
        return self.fibrec1(second,next,arr,n-1)
    def palindrome():
        pass

class Hashing:
    def findcounts(self, arr, queries):
        z=[]
        for i in range (0,len(queries),1):
            z.append(self.findnum(arr,queries[i]))
        return z
        

    def findnum(self, arr,tofind):
        count=0
        for i in range (0,len(arr),1):
            if(arr[i]==tofind):
                count+=1
        return count

    def findcounthasing(self,arr,queries):
        hash = [0]
        hash = hash * 256
        # pre-processing
        for i in range (0,len(arr),1):
            hash[ord(arr[i])]+=1
        # finding            
        z = []
        for i in range (0,len(queries),1):
           char = queries[i] #a b E
           z.append(hash[ord(char)])            
        return z
    def findcountsdic(self,arr,queries):
        count={}
        # pre-processing
        for key in arr:
            # if value present in dictionary , add 1 to it
            if key in count:
                count[key] = count[key] + 1
            # if value not present, put key,value(key, 1) in dictionary
            else:
                count[key] = 1
        # finding   
        z=[]
        for tofind in queries:
            #quereis value==dic check
            #dic key check (tofind)
            if tofind in count:
                z.append(count[tofind])
            else:
                z.append(0)  
        return z  
    def find_counts_string(self, word):
        z={}
        for key in word:
            if (key==' '):
                continue
            if key in z:
                z[key]=z[key]+1
            else:
                z[key]=1
        print(z)
        for key,value in z.items():
            print('char:',key,' count:',value)
    def findcounttopk(self,nums,k):
        count={}
        z=[]
        for key in nums:
            if key in count:
                count[key] = count[key]  + 1
            else:
                count[key] = 1
        for key,value in count.items():
            z.append((value,key))
        sorted_z = sorted(z, reverse=True)
        res = []
        for i in range (0,k,1):
            sorted_pair = sorted_z[i] #(3, 1)
            res.append(sorted_pair[1])
        return res

class Sorting:
    def selectsort(self,arr):  #O(n**2) #O(1)
        #min arr
        left=0 #O(1) 
        right=len(arr)  #O(n)
        while(left<right):  #O(n**2) 
            minindex=self.findminindex(arr,left,right)  #O(n) 
            temp=arr[left]  #O(1) 
            arr[left]=arr[minindex]  #O(1) 
            arr[minindex]=temp  #O(1) 
            left+=1  #O(1) 
        return arr

    def findminindex(self,arr,left,right):
        min=arr[left] #O(1)
        minindex=left #O(1) 
        for i in range (left,right,1): #O(n) 
            if(arr[i]<min): #O(1)
                min=arr[i] #O(1)
                minindex=i #O(1)
            
        return minindex
    
    def bubblesort(self,arr): #O(n*2) #O(1)
        #swap till max element reach end
        n=len(arr)-1#O(n)
        while(n>0):#O(n*2)#O(1)
            arr=self.maxtotheend(arr,n,0)#O(n)
            n-=1
        return arr

    def maxtotheend(self,arr,end,i):
        if(i>=end):
            return arr
        else:
            if(arr[i]>arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
            self.maxtotheend(arr,end,i+1)
        return arr
    
    
    def insertionsort(self,arr):#O(n*2)#o(1)
        n=1#O(1) 
        while(len(arr)>n):#O(n*2)
            arr=self.correct(arr,n,n)#O(n)
            n+=1
        return arr
        #puts right value in the correct index (compare adjacent element)
    def correct(self,arr,end,i):
        if(i<=0):
            return arr           
        if(arr[i]<arr[i-1]):
            temp=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=temp
        self.correct(arr,end,i-1)
        return arr
    def mergemain(self,arr):
        self.mergerec(arr,0,len(arr)-1)
        return arr
    
    def mergerec(self,arr,start,end):
        if(start>=end):
            return
        mid=((start+end)//2)  
        self.mergerec(arr,start,mid)
        self.mergerec(arr,mid+1,end)
        self.merge(arr,start,mid,end)

    def merge(self,arr,start,mid,end):
        z=[]
        p1=start
        p2=mid+1
        while(p1<=mid and p2<=end):
            if(arr[p1]>arr[p2]):
                z.append(arr[p2])
                p2+=1
            else:
                z.append(arr[p1])
                p1+=1
        while(p2<=end):
            z.append(arr[p2])
            p2+=1
        while(p1<=mid):
            z.append(arr[p1])
            p1+=1
        for i in range (start,end+1,1):
            arr[i]=z[i-start]
        return 
    def quicksort(self,arr):
        self.quicksort1(arr,0,len(arr)-1)
        return arr
    

    def quicksort1(self,arr,low,high):
        g=low
        l=high
        if(low<high):
            swappos=self.quicksort2(arr,low,high)
            self.quicksort1(arr,low,swappos-1)
            self.quicksort1(arr,swappos+1,high)

    
    def quicksort2(self,arr,low,high):
        pv=arr[low]
        g=low
        l=high
        while(g<l):
            while(arr[g]<=pv and g<=high-1):
                g+=1
            
            while(arr[l]>pv and l>=low+1 ):
                l-=1
            
            if(g<l):
                temp=arr[g]
                arr[g]=arr[l]
                arr[l]=temp
        temp=arr[low]git
        arr[low]=arr[l]
        arr[l]=temp
        return l
    


    #4 2 6 5 7 9 3 
    #4, 6, 2, 5, 7,9 ,1,3
    #        lg                
    #g=1 l=7
    #4, 3, 2, 5, 7,9 ,1,6

  
inputs = [[4, 6, 2, 5, 7,9 ,1,3 ]]
#exp =[1, 3, 2, 4, 7,9 ,5,6   ]
s=Sorting()
start = time.time()
for arr in inputs:
    print('INPUT: arr',arr)
    print('OUTPUT:',s.quicksort(arr))
    print('-'*25)
end = time.time()
print('TIME TAKEN:',(end-start)* 10**3, "ms")

	    