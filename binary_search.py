import time
import math
class Binary_serach_prob:
    def search(self,arr,target):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return mid
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
    def search_op(self,arr,target):
        return self.search_rec(arr,0,len(arr)-1,target)
    
    def search_rec(self,arr,low,high,target):
        if(low>high):
            return -1
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(target>arr[mid]):
            return self.search_rec(arr,mid+1,high,target)
        else:
            return self.search_rec(arr,low,mid-1,target)
    
    def lowerBound(self,arr,target):
        return self.search_rec(arr,0,len(arr)-1,target)
 
    def search_rec(self,arr,low,high,target):
        value=len(arr)
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>=target):
                value=mid
                high=mid-1
            else:
                low=mid+1
        return value
    
    def upperbond(self,arr,target):
        return self.search_rec(arr,0,len(arr)-1,target)
 
    def search_rec(self,arr,low,high,target):
        value=len(arr)
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>target):
                value=mid
                high=mid-1
            else:
                low=mid+1
        return value
    # You are given a sorted array arr of distinct values and a target value . You need to search for the index of the target value in the array.
    # if already there is target value just return that index 
    def searchInsert(self, arr, target):
        return self.search_rec(arr,0,len(arr)-1,target)
    
    def search_rec(self,arr,low,high,target):
        if(low>high):
            return ((low+high)//2)+1 #( return the expected place where a target can be)
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid #(already target is there)
        elif(target>arr[mid]):
            return self.search_rec(arr,mid+1,high,target)
        else:
            return self.search_rec(arr,low,mid-1,target)
    

    def ceilingInSortedArray(self,arr,target):
        arr=sorted(arr)
        print(arr)
        floor=self.binary_search_floor(arr,target)
        ceil=self.binary_search_ceil(arr,target)
        return [floor,ceil]

    
    def binary_search_floor(self,arr,target):
        low=0
        high=len(arr)-1
        flr=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return arr[mid]
            elif(arr[mid]>target):
                high=mid-1
            else:
                flr=arr[mid]
                low=mid+1
        return flr
    
    def ce(self,arr,target):
        low=0
        high=len(arr)-1
        cel=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return arr[mid]
            elif(arr[mid]>target):
                cel=arr[mid]
                high=mid-1
            else:
                low=mid+1
        return cel
    

    def searchRange(self, arr, target):
        low=0
        high=len(arr)-1
        start=-1
        end=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                start=mid
                high=mid-1
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(arr)-1        
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                end=mid
                low=mid+1
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        return [start,end]
    
    def count(arr: [int], n: int, target: int) -> int:
        low=0
        high=len(arr)-1
        start=-1
        end=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                start=mid
                high=mid-1
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(arr)-1        
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                end=mid
                low=mid+1
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        if(start>=0 and end>=0):
            return (end-start)+1
        else:
            return 0
    
    def search_rotate_brute(self, arr, target):
        val_=dict()
        for i in range (0,len(arr),1):
            val_[arr[i]]=i
        arr=sorted(arr)
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return val_[arr[mid]]
            elif(target>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        return -1 
    
    def search_rotate_opt(self, arr, target):
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        #Output: 4
        low=0
        high=len(arr)-1
        start=-1
        end=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return mid 
            if(arr[low]<=arr[mid]):#left half sorted conditon 
                if(arr[low]<=target and target<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
        
            else:
                if(arr[mid]<=target and target <=arr[high]):#right half sorted conditon 
                    low=mid+1
                else:
                    high=mid-1
        return -1
    
    def search_rotate_opt1(self, arr, target):
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        #Output: 4
        low=0
        high=len(arr)-1
        start=-1
        end=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return True 
            if(arr[low]<=arr[mid]):#left half sorted conditon 
                if(arr[low]<=target and target<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
        
            else:
                if(arr[mid]<=target and target <=arr[high]):#right half sorted conditon 
                    low=mid+1
                else:
                    high=mid-1
        return False
    
    def search_rotate2_opt(self, arr, target):
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        #Output: 4
        low=0
        high=len(arr)-1
        start=-1
        end=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return True 
            if(arr[high]==arr[mid] and arr[low]==arr[mid]):
                high=high-1
                low=low+1
                continue
            if(arr[low]<=arr[mid]):#left half sorted conditon 
                if(arr[low]<=target and target<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
        
            else:
                if(arr[mid]<=target and target <=arr[high]):#right half sorted conditon 
                    low=mid+1
                else:
                    high=mid-1
        return False
    
    #find min in the roated sorted array 
    def findMin(self, arr):
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        #Output: 4
        low=0
        high=len(arr)-1
        min_=999999999999999
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):#left half sorted conditon 
                    min_=min(min_,arr[low])
                    low=mid+1
            else:   
                    min_=min(arr[mid],min_) 
                    high=mid-1       
        return min_
    
    def howmanyrotate_brute(self, arr):
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        #Output: 4
        low=0
        high=len(arr)-1
        min_=999999999999999
        index=0
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):#left half sorted conditon 
                    if(arr[low]<min_):
                        min_=arr[low]
                        index=low
                    low=mid+1
            else:   
                    if(arr[mid]<min_):
                        min_=arr[mid]
                        index=mid
                    high=mid-1 
        return index
    

a=Binary_serach_prob()
arr=[]
arr1=[1,2,3]
arr2=[1]
print(a.howmanyrotate_brute(arr1))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)