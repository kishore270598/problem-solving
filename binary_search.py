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
                    print(min_)
            else:   
                    if(arr[mid]<min_):
                        min_=arr[mid]
                        index=mid
                    high=mid-1 
                    print(min_)
        return min_
    
    def singleNonDuplicate(self, arr):
        low=0
        n=len(arr)
        high=n-1
        #all conditions
        if(n==1):
            return arr[0]
        if(arr[0]!=arr[1]):
            return arr[low]
        if(arr[n-1]!=arr[n-2]):
            return arr[n-1]
        #1 1 2 3 3 (arr[even],arr[odd]) are equal means eliminate left(single element is in right)
        #(arr[odd],arr[even]) are equal means eliminate right (single element is in left)
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]):
                return arr[mid]
            if((mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1])):
                low=mid+1
            else:
                high=mid-1

        return -1
    def findPeakElement_brute(self,arr):
        for i in range(0,len(arr),1):
            if((i==0 or arr[i-1]<arr[i]) and (i==(len(arr)-1) or arr[i]>arr[i+1])):
                return i
    
    def findPeakElement(self, arr):
        if(len(arr)==1):
            return 0
        if(arr[0]>arr[1]):
            return 0
        if(arr[len(arr)-1]>arr[len(arr)-2]):
            return len(arr)-1
        low=1
        high=(len(arr)-2)
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>arr[mid+1] and arr[mid-1]<arr[mid]):
                return mid
            elif(arr[mid]<arr[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return -1

    def floorSqrt(self,n):
        low=1
        high=n
        root=1
        while(low<=high):
            mid=(low+high)//2
            if((mid**2)<=n):
                root=mid
                low=mid+1
            else:
                high=mid-1
        return root
    def NthRoot(self,n: int, m: int) -> int:
            low=1
            high=m
            while(low<=high):
                mid=(low+high)//2
                midN = self.npower1(mid,n,m)
                if(midN==1):
                    return mid
                elif(midN==0):
                    low=mid+1
                else:
                    high=mid-1
            return -1
        
    def npower1(self,mid,n,m):
        ans=1
        for i in range(1,n+1,1):
            ans=ans*mid
            if(ans>m):
                return 2
        if(ans==m):
            return 1
        return 0

    
    def npower(self,mid,n):
        ans=1
        while(n>0):
            if(n%2==1):
                ans=ans*mid
                n=n-1
            else:
                mid=mid*mid
                n=n//2
        return ans
    #Koko Eating Bananas
    def minEatingSpeed_brute(self,piles,hours):
        n=max(piles)
        for i in range(1,n+1,1):
            required_time=self.calculate_time(i,piles,n)
            if(required_time<=hours):
                return i
    

    def calculate_time(self,piles,k):
        ans=0
        for i in range(0,len(piles),1):
            ans+=math.ceil(piles[i]/k)
        return ans
    
    def minEatingSpeed_binary(self,piles,hours):
        low=1
        ans=0
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            ans=self.calculate_time(piles,mid)
            if(ans<=hours):
                high=mid-1
            else:
                low=mid+1
        return low
    
    #we take min as the possible bloom of the day(low)
    #high as last day possible.. we need to check the possible adjancent days
    #that will be the possible flowers that need to be share for 1 Bouquet
    def minDays(self, bloomDay, m, k):
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(self.check(bloomDay,mid,m,k)==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def check(self,bloomDay,mid,m,k):
        count=0
        boq=0
        for i in range(0,len(bloomDay),1):
            if(bloomDay[i]<=mid):
                count+=1
            else:
                boq+=(count//k)
                count=0
        boq+=(count//k)
        if(boq>=m):
            return True
        else:
            return False

    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        ans=1
        while(low<=high):
            mid=(low+high)//2
            if(self.find_sum_div(nums,mid)<=threshold):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
    def find_sum_div(self,nums,mid):
        sum_=0
        for i in range(0,len(nums),1):
            sum_+=math.ceil(nums[i]/mid)
        return sum_
    
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        ans=1
        while(low<=high):
            mid=(low+high)//2
            if(self.find_min_days(weights,mid)<=days):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 
    def find_min_days(self,weights,mid):
        days=1
        load=0
        for i in range(0,len(weights),1):
            if(load+weights[i]>mid):
                days+=1
                load=weights[i]
            else:
                load+=weights[i]
        return days
    
    #arr    [2,3,4,7,11]
    #ind    [0,1,2,3,4]
    #missing[1,1,1,3,5] (missing = arr[i]-(index+1))
    #for missing we need to do the binary search  at last high and low will be boundaries of missing number
    # arr[high]+ more will be the result but arr[high] can go -1, so we take more=(k-missing)=--> arr[high] + k-arr[high]-(index+1)  -->
    #high+1+k that is low+k (since boundaries)

    def findKthPositive(self, arr, k):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid=(low+high)//2
            missing = (arr[mid] - (mid + 1))
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return k + high + 1
    #we are placeing a cow in starting position and finding the max distance that can be place in array
    # possibleplacecow function finds the possible cow can be place from the last.. once its place we set the last as placed one

    
    def aggressiveCows(self,stalls, k):
        stalls=sorted(stalls)
        low=1
        high=stalls[len(arr)-1] -stalls[0]
        while(low<=high):
            mid=(low+high)//2
            if(self.possibleplacecow(stalls,mid,k)==True):
               ans=mid
               low=mid+1
            else:
               high=mid-1
        return ans

    def possibleplacecow(self,stalls,dist,cows):
        cow=1
        last=stalls[0]
        for i in range(0,len(stalls),1):
            if(stalls[i]-last>=dist):
                cow+=1
                last=stalls[i]
        if(cow>=cows):
            return True
        else:
            return False
        
    def findPages(self,arr, n, m):
        low=max(arr)
        high=sum(arr)
        #possible pages can be set
        while(low<=high):
            mid=(low+high)//2
            students_=self.find_maxofstudents(arr,mid,m)
            if(students_>m):
                low=mid+1
                #to find the equal students  more pages is been divded to more students so we need to find more pages to equalizse student value
            else:
                high=mid-1
        return low
    
    def find_maxofstudents(self,arr,page_possible,m):
        student=1 
        noofpages=0
        for i in range(0,len(arr),1):
            if(noofpages+arr[i]<=page_possible):
                #allocating all the pages to the student itself
                noofpages+=arr[i]
            else:
                noofpages=arr[i]
                student+=1
                #if that pages got done add the remaning to other students and allocate
        return student
    
    def splitArray(self, nums, k):
        low=max(arr)
        high=sum(arr)
        while(low<=high):
            mid=(low+high)//2
            painter=self.find_maxofpainttime(arr,mid,k)
            if(painter>k):
                low=mid+1
            else:
                high=mid-1
        return low
    
    def find_maxofpainttime(self,arr,possibletime,m):
        painter=1 
        noftime=0
        for i in range(0,len(arr),1):
            if(noftime+arr[i]<=possibletime):
                noftime+=arr[i]
            else:
                noftime=arr[i]
                painter+=1
        return painter

    def minimiseMaxDistance(self,arr, k):
        high=0
        for i in range(0,len(arr)-1,1):
            high=max(high,(arr[i+1]-arr[i]))     
        low=0
        diff = 1e-6
        while(high-low > diff):
            mid=(low+high)/2.0
            station=self.place_gas_station(arr,mid)
            if(station>k):
                low=mid
            else:
                high=mid
        return high
    
    def place_gas_station(self,arr,distance):
        gas=0
        for i in range(1,len(arr),1):
            numberinbetween=((arr[i]-arr[i-1])/distance)
            if((arr[i]-arr[i-1]))==(distance * numberinbetween):
                numberinbetween-=1
            gas+=numberinbetween
        return gas
    


a=Binary_serach_prob()
arr=[1, 2, 3, 4, 5]
arr1=[1]
arr2=[1]
print(a.minimiseMaxDistance(arr,4))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)