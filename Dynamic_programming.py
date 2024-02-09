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

    def ninjaTraining(self,n, points):
        def f(day,last):#recur function
            if day==0:
                #if its 0 means ur starting u don't need any previous
                maxi=0
                for i in range(0,3,1):
                    if i!=last:
                        maxi=max(maxi,points[0][i])
                return maxi
            
            maxi=0
            for i in range(0,3,1):
                if i!=last:
                    points=points[day][i]+f(day-1,i) #this is to check the last guy and get the value what he did , making sure he is not doing the current task
                    maxi=max(maxi,points)
            return maxi
        return f(n-1,3)
    #memo
    def ninjaTraining(n: int, points: List[List[int]]) -> int:
            def f(day,last):#recur function
                if day==0:
                    #if its 0 means ur starting u don't need any previous
                    maxi=0
                    for i in range(0,3,1):
                        if i!=last:
                            maxi=max(maxi,points[0][i])
                    return maxi
                if dp[day][last]!=-1:
                    return dp[day][last]
                maxi=0
                for i in range(0,3,1):
                    if i!=last:
                        point=points[day][i]+f(day-1,i) #this is to check the last guy and get the value what he did , making sure he is not doing the current task
                        maxi=max(maxi,point)
                dp[day][last]=maxi
                return dp[day][last]
            dp=[]
            for i in range(n):
                temp=[]
                for j in range(4):
                    temp.append(-1)
                dp.append(temp)
            return f(n-1,3)
    #tab
    def ninjaTraining(n: int, points: List[List[int]]) -> int:
        dp=[]
        for i in range(n):
            temp=[]
            for j in range(4):
                temp.append(0)
            dp.append(temp)
        dp[0][0]=max(points[0][1],points[0][2])
        dp[0][1]=max(points[0][0],points[0][2])
        dp[0][2]=max(points[0][0],points[0][1])
        dp[0][3]=max(points[0][0],max(points[0][1],points[0][2]))
        for day in range(n):
            for last in range(4):
                dp[day][last]=0
                for task in range(3):
                    if task!=last:
                        point=points[day][task]+dp[day-1][task]
                        dp[day][last]=max(dp[day][last],point)
        return dp[n-1][3]
    #space 
    def ninjaTraining(n: int, points: List[List[int]]) -> int:
            prev=[0]*(4)
            prev[0]=max(points[0][1],points[0][2])
            prev[1]=max(points[0][0],points[0][2])
            prev[2]=max(points[0][0],points[0][1])
            prev[3]=max(points[0][0],max(points[0][1],points[0][2]))
            for day in range(1,n):
                temp=[0]*(4)
                for last in range(4):
                    temp[last]=0
                    for task in range(3):
                        if task!=last:
                            temp[last]=max(temp[last],points[day][task]+prev[task])
                prev=temp
            return prev[3]
    def uniquePaths(self, m, n):                    
        def f(i,j): #tc-2power (n*m)
            #top down
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            up=f(i-1,j)
            down=f(i,j-1)
            return up+down
        return f(m-1,n-1)
        #memo
    def uniquePaths(self, m, n):
        def f(i,j): #tc-O(n*m)
            #top down
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            down=f(i,j-1)
            dp[i][j]=up+down
            return dp[i][j]
        dp=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        return f(m-1,n-1)
        #tab 
    def uniquePaths(self, m, n):
        dp=[] #space= O(N*M)
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1 #changing into base case
                else:
                    up=0
                    down=0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        down=dp[i][j-1]
                    dp[i][j]=up+down
        return dp[m-1][n-1]












            



d=Dynamic_programing()
heights=[[1,2,5], [3 ,1 ,1] ,[3,3,3]]
ans=d.ninjaTraining(3,heights)
print('ANS',ans)

