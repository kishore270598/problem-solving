import math
class Dynamic_programing:
    def fibonacci(self,n):
        #memory method
        def f(n,dp):
            if n<=1:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n]=f(n-1,dp)+f(n-2,dp)
            return dp[n]
        dp=[-1]*(n+1)
        return f(n,dp)
    
    def fibonacci_tab(self,n):
        #tabulation method
        #TIME COMPLEX- TC O(N)
        #SPAEC COMPLEC- SC 0(1)
        prev2=0
        cur=0
        prev=1
        for i in range(2,n+1,1):
            cur=prev2+prev
            prev2=prev
            prev=cur
        return cur
    def climbStairs(self, n):
            # def f(n):
            #     if n==0 or n==1:
            #         return 1
            #     left=f(n-1)
            #     right=f(n-2)
            #     return left+right
            # return f(n)
            prev1=1
            prev2=1
            if n==1 or n==0:
                return 1
            cur=0
            for i in range(2,n+1,1):
                cur=prev1+prev2
                prev2=prev1
                prev1=cur
            return cur
  
    def frogJump(self,n, heights):
        # def f(n,dp):
        #     if n==0:
        #         return 0
        #     if dp[n]!=-1:
        #         return dp[n]
        #     left=f(n-1,dp)+abs(heights[n]-heights[n-1])
        #     right=float('inf')
        #     if n>1:
        #         right=f(n-2,dp)+abs(heights[n]-heights[n-2])
        #     dp[n]=min(left,right)
        #     return dp[n]
        #left,right=0,0
        #memo method
        # dp=[-1]*(n+1)
        # dp[0]=0
        # for i in range(1,n+1,1):
        #     left=dp[i-1]+abs(heights[i]-heights[i-1])
        #     right=float('inf')
        #     if i>1:
        #         right=dp[i-2]+abs(heights[i]-heights[i-2])
        #     dp[i]=min(left,right)
        # return dp[n-1]
        curr=0
        prev=0
        prev2=0
        for i in range(1,n+1,1):
            left=prev+abs(heights[i]-heights[i-1])
            right=float('inf')
            if i>1:
                right=prev2+abs(heights[i]-heights[i-2])
            curr=min(left,right)
            prev2=prev
            prev=curr
        return curr

    
    def minimizeCost(self,n, k, heights):
        dp=[-1]*(n)
        dp[0]=0
        for i in range(1,n,1):
            min_=float('inf')
            for j in range(1,k+1,1):
                if (i-j>=0):# jump is valid
                    jump=dp[i-j]+abs(heights[i]-heights[i-j])
                    min_=min(jump,min_)
            
            dp[i]=min_
        return dp[n-1]
    
    def rob(self, nums):
        #memo
        n=len(nums)-1
        def f(n):
            if n==0:
                return nums[n] #it means u have not picked 1
            if n<0:
                return 0 #to avoid the negative
            pick=nums[n]+f(n-2)
            #else
            notpick=f(n-1)
            return max(pick,notpick)
        return f(n)
    def rob(self, nums):
        #TAB
        n=len(nums)-1
        dp=[-1]*n
        def f(n):
            if n==0:
                return nums[n] #it means u have not picked 1
            if dp[n]!=-1:
                return dp[n]
            if n<0:
                return 0 #to avoid the negative
            pick=nums[n]+f(n-2)
            #else
            notpick=f(n-1)
            dp[n]=max(pick,notpick)
            return dp[n]
        return f(n)
    def rob(self, nums):
        #TAB  space
        n=len(nums)-1
        dp=[-1]*(n+1)
        dp[0]=nums[0]
        for i in range(1,len(nums),1):
            pick=nums[i]
            if (i>1):
                pick+=dp[i-2]
            nonpick=dp[i-1]
            dp[i]=max(pick,nonpick)
        return dp[n]
    
    def rob(self, nums):
        #TAB op space
        n=len(nums)-1
        prev=nums[0]
        prev2=0
        curr=0
        if n==0:
            return nums[0]
        for i in range(1,len(nums),1):
            pick=nums[i]
            if (i>1):
                # Calculate the maximum value when not picking the current element
                pick+=prev2
            #i-1 means prev # i-2 prev 2
            nonpick=0+prev
            curr=max(pick,nonpick)
            prev2=prev
            prev=curr
        return curr
    #follow up
    def rob(self, nums):
        def f(nums):
            #TAB  space
            n=len(nums)
            dp=[-1]*(n+1)
            dp[0]=nums[0]
            for i in range(1,len(nums),1):
                pick=nums[i]
                if (i>1):
                    pick+=dp[i-2]
                nonpick=dp[i-1]
                dp[i]=max(pick,nonpick)
            return dp[n-1]
        n=len(nums)
        arr1=[]
        arr2=[]
        if n==1:
            return nums[0]
        for i in range(n):
            if i != 0:
                arr1.append(nums[i])
            if i != n - 1:
                arr2.append(nums[i])

        ans1 = f(arr1)
        ans2 = f(arr2)

        return max(ans1, ans2)


    



d=Dynamic_programing()
heights=[10, 40, 30, 10]
ans=d.minimizeCost(4,2,heights)
print('ANS',ans)

