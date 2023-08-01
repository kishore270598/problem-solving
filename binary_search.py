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
    
    def binary_search_ceil(self,arr,target):
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

a=Binary_serach_prob()
arr=[]
arr1=[3 ,44, 14, 39 ,41, 47 ,37 ,1, 21 ]
arr2=[1]
print(a.ceilingInSortedArray(arr1,35))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)