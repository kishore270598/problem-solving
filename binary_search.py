import time
import math
class Binary_serach_prob:
    def search(self,arr,target):
        low=0
        high=len(arr)-1
        for i in range(0,len(arr),1):
            mid=(low+high)//2
            while(low<=high):
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

a=Binary_serach_prob()
arr=[]
arr1=[1, 2, 2, 3]
arr2=[1]
print(a.lowerBound(arr1,2))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)