class Solution:
    def fact(self,n):
        last=len(n)-1
        start=0
        for i in range(0,(len(n)//2),1):
            temp=n[last] 
            n[last]=n[start]
            n[start]=temp
            start+=1
            last-=1
        return n
    def fact_recur1(self,l,s,arr):
        if(l<s):
            return arr
        else:
            temp=arr[l]
            arr[l]=arr[s]
            arr[s]=temp
        return self.fact_recur1(l-1,s+1,arr)       
    def fact_recur(self,arr):
        return self.fact_recur1(len(arr)-1,0,arr)

n=[1,2,3,4,5,6,7]
s=Solution()
print(s.fact_recur(n))









