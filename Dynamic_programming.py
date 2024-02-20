import math
import sys
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
    def ninjaTraining(n, points):
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
    def ninjaTraining(n, points):
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
    def ninjaTraining(n, points):
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
    #normal re
    def uniquePathsWithObstacles(self, obstacleGrid):
        def f(i,j): #tc-2power (n*m)
            #top down
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            up=f(i-1,j)
            down=f(i,j-1)
            return up+down
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        return f(m-1,n-1)
    #memo
    def uniquePathsWithObstacles(self, obstacleGrid):
        def f(i,j): #tc-O(n*m)
            #top down
            if i==0 and j==0:
                return 1
            if obstacleGrid[i][j]==1:
                return 0
            if (i<0 or j<0):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            down=f(i,j-1)
            dp[i][j]=up+down
            return dp[i][j]
        dp=[]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        return f(m-1,n-1)
    #tab
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp=[] #space= O(N*M)
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue 
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
    def minPathSum(self, grid):
        def f(i,j,maxi):
            if i==0 and j==0:
                return grid[0][0]
            if j<0 or i<0:
                return float('inf')
            up=grid[i][j]+f(i-1,j,maxi)
            down=grid[i][j]+f(i,j-1,maxi)
            return min(up,down)
        maxi=float('inf')
        n=len(grid)
        m=len(grid[0])
        return f(n-1,m-1,maxi)
    #memo
    def minPathSum(self, grid):
        #tc O(N*M) SC --> O(PATH travel)
        def f(i,j,maxi):
            if i==0 and j==0:
                return grid[0][0]
            if j<0 or i<0:
                return float('inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+f(i-1,j,maxi)
            down=grid[i][j]+f(i,j-1,maxi)
            dp[i][j]=min(up,down)
            return min(up,down)
        maxi=float('inf')
        n=len(grid)
        m=len(grid[0])
        dp=[]
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(-1)
            dp.append(temp)
        return f(n-1,m-1,maxi)
    #tabulation 
    def minPathSum(self, grid):
            n=len(grid)
            m=len(grid[0])
            dp=[]
            for i in range(n):
                temp=[]
                for j in range(m):
                    temp.append(-1)
                dp.append(temp)
            for i in range(n):
                for j in range(m):
                    if i==0 and j==0:
                        dp[i][j]=grid[i][j]
                    else:
                        up=grid[i][j]
                        if i>0:
                            up+=dp[i-1][j]
                        else:
                            up+=int(1e9)
                        down=grid[i][j]
                        if j>0:
                            down+=dp[i][j-1]
                        else:
                            down+=int(1e9)
                        dp[i][j]=min(down,up)
            return dp[n-1][m-1]
    #space
    def minPathSum(self, grid):
        n=len(grid)
        m=len(grid[0])
        dp=[]
        #we required a prev 
        prev=[0]*m
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(-1)
            dp.append(temp)
        for i in range(n):
            curr=[0]*m
            for j in range(m):
                if i==0 and j==0:
                    curr[j]=grid[i][j]
                else:
                    up=grid[i][j]
                    if i>0:
                        #prev ROW j col
                        up+=prev[j]
                    else:
                        up+=int(1e9)
                    down=grid[i][j]
                    if j>0:
                        #current row j-1 col will be prev
                        down+=curr[j-1]
                    else:
                        down+=int(1e9)
                    curr[j]=min(down,up)
            prev=curr
        return prev[m-1]



    # rec
    def minimumTotal(self, triangle):
        def f(i,j):
                if i==n-1:
                        return triangle[i][j]
                dp=triangle[i][j]+f(i+1,j)
                da=triangle[i][j]+f(i+1,j+1)
                return min(dp,da)
        n=len(triangle)
        return f(0,0)
    # memo
    def minimumTotal(self, triangle):
        #memo
        dp_=[]
        n=len(triangle)
        for i in range(n):
            z=[]
            for j in range(n):
                z.append(-1)
            dp_.append(z)
            def f(i,j):
                if i==n-1:
                    return triangle[i][j]
                if dp_[i][j]!=-1:
                    return dp_[i][j]
                dp=triangle[i][j]+f(i+1,j)
                da=triangle[i][j]+f(i+1,j+1)
                dp_[i][j]=min(dp,da)
                return dp_[i][j]
        n=len(triangle)
        return f(0,0)
        

# tab
    def minimumTotal(self, triangle):
        dp=[]
        n=len(triangle)
        for i in range(n):
            z=[]
            for j in range(n):
                z.append(-1)
            dp.append(z)
        for j in range(n):
            #to store the last values
            dp[n-1][j]=triangle[n-1][j]
        #sine we starting from n-1
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d=triangle[i][j]+dp[i+1][j]
                da=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(d,da)
        return dp[0][0]
				
# tab space
    def minimumTotal(self, triangle):   
        n=len(triangle)
        front=[0]*n
        for j in range(n):
            #to store the last values
            front[j]=triangle[n-1][j]
        #sine we starting from n-1
        for i in range(n-2,-1,-1):
            curr=[0]*n
            for j in range(i,-1,-1):
                d=triangle[i][j]+front[j]
                da=triangle[i][j]+front[j+1]
                curr[j]=min(d,da)
            front=curr
        return front[0]
    def minFallingPathSum(self, matrix):
        #rec
        n=len(matrix)
        def f(i,j):
            if i==n-1:
                return matrix[i][j]
            d_anti=matrix[i][j]+f(i+1,j-1)
            d_bot=matrix[i][j]+f(i+1,j)
            d_dia=matrix[i][j]+f(i+1,j+1)
            return min(d_dia,min(d_bot,d_anti))
        min_=0
        for i in range(n):
            min_=min(min_,f(0,i))
        return min_
    # rec
    def minFallingPathSum(self, matrix):
        #rec
        n=len(matrix)
        def f(i,j):
            if j<0 or j>=n:
                return int(1e9)
            if i==0:
                return matrix[0][j]
            d_anti=matrix[i][j]+f(i-1,j-1)
            d_bot=matrix[i][j]+f(i-1,j)
            d_dia=matrix[i][j]+f(i-1,j+1)
            return min(d_dia,min(d_bot,d_anti))
        min_=float('inf')
        for i in range(n-1,-1,-1):
            min_=min(min_,f(n-1,i))
        return min_
    def minFallingPathSum(self, matrix):
        #memo
        n=len(matrix)
        def f(i,j):
            if j<0 or j>=n:
                return int(1e9)
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==0:
                return matrix[0][j]
            d_anti=matrix[i][j]+f(i-1,j-1)
            d_bot=matrix[i][j]+f(i-1,j)
            d_dia=matrix[i][j]+f(i-1,j+1)
            dp[i][j]=min(d_dia,min(d_bot,d_anti))
            return dp[i][j]
        min_=float('inf')
        for i in range(n-1,-1,-1):
            dp=[]
            for k in range(n):
                temp=[]
                for j in range(n):
                    temp.append(-1)
                dp.append(temp)
            min_=min(min_,f(n-1,i))
        return min_

    def minFallingPathSum(self, matrix):
        #tab
        n=len(matrix)
        min_=float('inf')
        dp=[]
        for k in range(n):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        for j in range(n):
            dp[0][j]=matrix[0][j]
        for i in range(1,n,1):
            for j in range(n):
                if j-1>=0:
                    d_anti=matrix[i][j]+dp[i-1][j-1]
                else:
                    d_anti=int(1e9)
                d_bot=matrix[i][j]+dp[i-1][j]
                if j+1<n:
                    d_dia=matrix[i][j]+dp[i-1][j+1]
                else:
                    d_dia=int(1e9)
                dp[i][j]=min(d_dia,min(d_bot,d_anti))
        mini=dp[n-1][0]
        for j in range(1,n,1):
            mini=min(mini,dp[n-1][j])
        return mini

        # space

    def minFallingPathSum(self, matrix):
        #tab
        n=len(matrix)
        min_=float('inf')
        dp=[]
        for k in range(n):
            temp=[]
            for j in range(n):
                temp.append(-1)
            dp.append(temp)
        prev=[0]*n
        for j in range(n):
            prev[j]=matrix[0][j]
        for i in range(1,n,1):
            cur=[0]*n
            for j in range(n):
                if j-1>=0:
                    d_anti=matrix[i][j]+prev[j-1]
                else:
                    d_anti=int(1e9)
                d_bot=matrix[i][j]+prev[j]
                if j+1<n:
                    d_dia=matrix[i][j]+prev[j+1]
                else:
                    d_di=int(1e9)
                cur[j]=min(d_dia,min(d_bot,d_anti))
            prev=cur
        mini=float('inf')
        for j in range(0,n,1):
            mini=min(mini,prev[j])
        return mini
        #MEMO
    def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
        def f(i,j1,j2):
            if j2>=c or j1>=c or j1<0 or j2<0:
                return int(-1e9)
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            if i==r-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            maxi = -sys.maxsize
            dir=[-1,0,1]
            for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1] + f(i + 1, j1 + di, j2 + dj)
                        else:
                            ans = grid[i][j1] + grid[i][j2] + f(i + 1, j1 + di, j2 + dj)
                        maxi = max(maxi, ans)
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]
        n=r
        m=c
        dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
        return f(0,0,c-1)


    # DP on Subsequences
    def subsetSumToK(n, k, arr):
    #recu
        def f(index,k):
            if k==0:
                return True
            if index==0:
                if arr[index]==k:
                    return True
                else:
                    return False
            not_include=f(index-1,k)
            include=False
            if arr[index]<=k:
                include=f(index-1,k-arr[index])
            return not_include or include
        return f(n-1,k)
        #memeo
    def subsetSumToK(n, k, arr):
        def f(index,k):
            if k==0:
                return True
            if dp[index][k]!=-1:
                return dp[index][k]
            if index==0:
                if arr[index]==k:
                    return True
                else:
                    return False
            not_include=f(index-1,k)
            include=False
            if arr[index]<=k:
                include=f(index-1,k-arr[index])
            dp[index][k]=not_include or include
            return dp[index][k]
        dp = [[-1 for j in range(k+1)] for i in range(n)]
        return f(n-1,k)
        

    
    def subsetSumToK(n, k, arr):
        #tab
        dp = [[False for j in range(k+1)] for i in range(n)]
        for i in range(n):
            dp[i][0]=True
            #whenever the target is zero it means true
        if arr[0] <= k:
            dp[0][arr[0]] = True
        for i in range(1,n):
            for target in range(1,k+1):
                not_include=dp[i-1][target]
                include=False
                if arr[i]<=target:
                    include=dp[i-1][target-arr[i]]
                dp[i][target]=not_include or include

        return dp[n-1][k]
    def subsetSumToK(n, k, arr):
    #tab
        prev = [False] * (k + 1)
        prev[0]=True
        if arr[0] <= k:
            prev[arr[0]] = True
        for i in range(1,n):
            cur = [False] * (k + 1)
            cur[0] = True
            for target in range(1,k+1):
                not_include=prev[target]
                include=False
                if arr[i]<=target:
                    include=prev[target-arr[i]]
                cur[target]=not_include or include
            prev=cur
        return prev[k]
    #416. Partition Equal Subset Sum
    #------------------------------------------------------
    def subsetSumToK(self,n, k, arr):
        #tab
        prev = [False] * (k + 1)
        prev[0]=True
        if arr[0] <= k:
            prev[arr[0]] = True
        for i in range(1,n):
            cur = [False] * (k + 1)
            cur[0] = True
            for target in range(1,k+1):
                not_include=prev[target]
                include=False
                if arr[i]<=target:
                    include=prev[target-arr[i]]
                cur[target]=not_include or include
            prev=cur
        return prev[k]
    def canPartition(self, arr):
        n=len(arr)
        sum_=sum(arr)
        if sum_%2!=0:
            return False
        return self.subsetSumToK(n,sum_//2,arr)
    #------------------------------------------------------
    #2035. Partition Array Into Two Arrays to Minimize Sum Difference
    #------------------------------------------------------
    def minSubsetSumDifference(arr, n ):
        totSum = sum(arr)
        dp = [[False for i in range(totSum + 1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = True

        if arr[0] <= totSum:
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for target in range(1, totSum + 1):
                # If the current element is not taken, the result is the same as the previous row.
                notTaken = dp[ind - 1][target]

                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]

                # Update the DP table with the result of taking or not taking the current element.
                dp[ind][target] = notTaken or taken

        # Initialize a variable to track the minimum absolute difference.
        mini = int(1e9)
        # Iterate through all possible sums.
        for i in range(totSum + 1):
            if dp[n - 1][i] == True:
                diff = abs(i - (totSum - i))
                mini = min(mini, diff)

        return mini
    #------------------------------------------------------
    #------------------------------------------------------
    #count the subset for sum k
    #------------------------------------------------------    
    #recu
    def findWays(arr: List[int], k: int) -> int:
        #recu
        n=len(arr)
        def f(index,sum_):
            if sum_==0:
                return 1
            if index==0:
                if arr[index]==sum_:
                    return 1
                else:
                    return 0
            notpick=f(index-1,sum_)
            pick=0
            if arr[index]<=k:
                pick=f(index-1,sum_-arr[index])
            return pick+notpick
        return f(n-1,k)
    #memeo
    #------------------------------------------------------    
    def findWays(arr: List[int], k: int) -> int:
        n=len(arr)
        dp = [[-1 for i in range(k + 1)] for j in range(n)]
        def f(index,sum_):
            if sum_==0:
                return 1
            if dp[index][sum_]!=-1:
                return dp[index][sum_]
            if index==0:
                if sum_==0 and arr[index]==0:
                    return 2
                elif sum_==0 or arr[index]==0:
                    return 1
                else:
                    return 0
            notpick=f(index-1,sum_)
            pick=0
            if arr[index]<=sum_:
                pick=f(index-1,sum_-arr[index])
            dp[index][sum_]=pick+notpick
            return dp[index][sum_]
        return f(n-1,k)
    #------------------------------------------------------    
    def findWays(arr: List[int], k: int) -> int:
        #tab
        n=len(arr)
        dp = [[0 for i in range(k + 1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1
        if arr[0] <= k:
            dp[0][arr[0]] = 1
        for index in range(1,n):
            for sum_ in range(1,k+1):
                notpick=dp[index-1][sum_]
                pick=0
                if arr[index]<=sum_:
                    pick=dp[index-1][sum_-arr[index]]
                dp[index][sum_]=pick+notpick
        return dp[n-1][k]
    #------------------------------------------------------   
    #space optimi 
    def findWays(arr: List[int], k: int) -> int:
        #tab space opt
        n=len(arr)
        dp = [[0 for i in range(k + 1)] for j in range(n)]
        prev=[0]*(k+1)
        prev[0] = 1
        if arr[0] <= k:
            prev[arr[0]] = 1
        for index in range(1,n):
            curr=[0]*(k+1)
            curr[0]=1
            for sum_ in range(1,k+1):
                notpick=prev[sum_]
                pick=0
                if arr[index]<=sum_:
                    pick=prev[sum_-arr[index]]
                curr[sum_]=pick+notpick
            prev=curr
        return prev[k]
    #------------------------------------------------------  
    #Count Partitions with Given Difference (DP - 18)
    mod =int(1e9+7)
    def countPartitions(n: int, d: int, arr: List[int]) -> int:
        def findWays(num, k):
            n=len(num)
            dp = [[0] * (k + 1) for _ in range(n)]
            if num[0] == 0:
                dp[0][0] = 2 # 2 cases - pick and not pick
            else:
                dp[0][0] = 1 # 1 case - not pick
            if num[0] != 0 and num[0] <= k:
                dp[0][num[0]] = 1 # 1 case - pick
            for index in range(1,n):
                for sum_ in range(k+1):
                    notpick=dp[index-1][sum_]
                    pick=0
                    if num[index]<=sum_:
                        pick=dp[index-1][sum_-num[index]]
                    dp[index][sum_]=(pick+notpick)% mod
            return dp[n-1][k]
        totSum = sum(arr)
        mod=int(1e9+7)
        # Checking for edge cases
        if (totSum - d) < 0 or (totSum - d) % 2:
            return 0
        return findWays(arr, (totSum - d) // 2)
    #------------------------------------------------------ 
    #0/1 Knapsack (DP - 19) recur method
    #------------------------------------------------------ 
    def knapSack(self,W, wt, val, n):
        #recur method
        def f(index,weight,Threshold):
            #base case
            if index==0:
                if wt[index]<=Threshold:
                    return val[0]
                else:
                    return 0
            notpic=f(index-1,weight,Threshold)
            pick=-sys.maxsize
            if wt[index]<=Threshold:
                pick=val[index]+f(index-1,weight,Threshold-weight[index])
            return max(pick,notpic)
        Threshold=W
        return f(n-1,wt,Threshold)
    #------------------------------------------------------ 
    #0/1 Knapsack (DP - 19) memo method
    #------------------------------------------------------ 
    def knapSack(self,W, wt, val, n):
        #memo method
        def f(index,weight,Threshold):
            #base case
            if index==0:
                if wt[index]<=Threshold:
                    return val[0]
                else:
                    return 0
            if dp[index][Threshold]!=-1:
                return dp[index][W]
            notpic=f(index-1,weight,Threshold)
            pick=-sys.maxsize
            if wt[index]<=Threshold:
                pick=val[index]+f(index-1,weight,Threshold-weight[index])
            dp[index][Threshold]=max(pick,notpic)
            return dp[index][Threshold]
        Threshold=W
        dp = [[-1 for j in range(W + 1)] for i in range(n)]
        return f(n-1,wt,Threshold)
    #------------------------------------------------------ 
    #tab
    def knapSack(self,W, wt, val, n):
        #tab method
        dp = [[0 for j in range(W + 1)] for i in range(n)]
        #for every value less than W index 0 we can steal it
        for i in range(wt[0],W+1):
            dp[0][i]=val[0]
        for index in range(1,n):
            for Threshold in range(W+1):
                notpic=dp[index-1][Threshold]
                pick=-sys.maxsize
                if wt[index]<=Threshold:
                    pick=val[index]+dp[index-1][Threshold-wt[index]]
                dp[index][Threshold]=max(pick,notpic)
        return dp[n-1][W]
    #------------------------------------------------------ 
    #tab space
    #------------------------------------------------------ 
    def knapSack(self,W, wt, val, n):
        #tab method space
        prev=[0]*(W+1)
        #for every value less than W index 0 we can steal it
        for i in range(wt[0],W+1):
            prev[i]=val[0]
        for index in range(1,n):
            for Threshold in range(W,-1,-1):
                notpic=prev[Threshold]
                pick=-sys.maxsize
                if wt[index]<=Threshold:
                    pick=val[index]+prev[Threshold-wt[index]]
                prev[Threshold]=max(pick,notpic)
        return prev[W]
    #------------------------------------------------------ 
    #recur
    #------------------------------------------------------ 
    def coinChange(self, coins, amount):
        def f(index, threshold):
            # Base case: If we reach the first coin, check if it can divide the amount
            if index == 0:
                if threshold % coins[0] == 0:
                    # Same coin value can be used multiple times, so return the count
                    return threshold / coins[0]
                # If the coin cannot divide the amount, return a large value indicating impossibility
                return 1e9
            # Recursive cases:
            # 1. Don't take the current coin and move to the next one
            dont_take = f(index - 1, threshold)
            # 2. Take the current coin if it doesn't exceed the threshold, and recursively check the remaining amount
            take = float('inf')
            if coins[index] <= threshold:
                take = 1 + f(index, threshold - coins[index])
            # Return the minimum of the two options
            return min(take, dont_take)
        # Main function
        n = len(coins)
        # Calculate the minimum number of coins needed using the recursive function
        ans = f(n - 1, amount)
        # If the minimum number of coins is still a large value, it means it's impossible to make the amount
        if ans >= 1e9:
            return -1
        # Return the minimum number of coins needed
        return ans
    #------------------------------------------------------ 
    #memeo
    #------------------------------------------------------ 
    def coinChange(self, coins, amount):
        #memo
        def f(index,threshold):
            #base
            if index==0:
                #check the element can divide the amount
                if threshold % coins[0]==0:
                    #same value can be divided mutiple time so that count
                    return threshold / coins[0]
                return 1e9
            if dp[index][threshold]!=-1:
                return dp[index][threshold]
            donttake=f(index-1,threshold)
            take=float('inf')
            if coins[index]<=threshold:
                take=1+f(index,threshold-coins[index])
            dp[index][threshold]=min(take,donttake)
            return dp[index][threshold]
        n=len(coins)
        dp=[[-1 for i in range(amount+1)] for i in range(n)]
        ans =  f(n-1, amount)
        if ans >= 1e9:
            return -1
        return ans
    #------------------------------------------------------ 
    #tab
    #------------------------------------------------------ 
    def coinChange(self, coins, amount):
        #tab
        n=len(coins)
        dp=[[-1 for i in range(amount+1)] for i in range(n)]
        for i in range(amount+1):
            if i % coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=int(1e9)
        for index in range(1,n):
            for threshold in range(amount+1):
                donttake=dp[index-1][threshold]
                take=int(1e9)
                if coins[index]<=threshold:
                    take=1+dp[index][threshold-coins[index]]
                dp[index][threshold]=min(take,donttake)
        ans = dp[n - 1][amount]
        # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
        if ans >= int(1e9):
            return -1
        return ans
    #------------------------------------------------------ 
    #space
    #------------------------------------------------------ 
    def coinChange(self, coins, amount):
        #tab
        n=len(coins)
        dp=[[-1 for i in range(amount+1)] for i in range(n)]
        prev=[0]*(amount+1)
        curr=[0]*(amount+1)
        for i in range(amount+1):
            if i % coins[0]==0:
                prev[i]=i//coins[0]
            else:
                prev[i]=int(1e9)
        for index in range(1,n):
            for threshold in range(amount+1):
                donttake=prev[threshold]
                take=int(1e9)
                if coins[index]<=threshold:
                    take=1+curr[threshold-coins[index]]
                curr[threshold]=min(take,donttake)
            prev=curr
        ans = prev[amount]
        # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
        if ans >= int(1e9):
            return -1
        return ans
    #518. Coin Change II
    #-----------------
    def change(self, amount, coins):
        # Initialize variables
        n = len(coins)
        dp = [[0 for i in range(amount + 1)] for i in range(n)]
        prev = [0] * (amount + 1)
        curr = [0] * (amount + 1)
        
        # Set initial values in prev based on the first coin
        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1
        
        # Iterate over the remaining coins
        for index in range(1, n):
            for threshold in range(amount + 1):
                # Calculate the number of ways to make change for the current threshold
                donttake = prev[threshold]
                take = 0
                
                # Check if the current coin can be taken to contribute to the change
                if coins[index] <= threshold:
                    take = curr[threshold - coins[index]]
                    
                # Update the current value in the dp array
                curr[threshold] = take + donttake
            
            # Update prev array for the next iteration
            prev = curr
        
        # The final result is stored in the last element of prev array for the given amount
        return prev[amount]

    def findTargetSumWays(self, arr, d):
        def findWays(num, k):
            n=len(num)
            dp = [[0] * (k + 1) for _ in range(n)]
            if num[0] == 0:
                dp[0][0] = 2 # 2 cases - pick and not pick
            else:
                dp[0][0] = 1 # 1 case - not pick
            if num[0] != 0 and num[0] <= k:
                dp[0][num[0]] = 1 # 1 case - pick
            for index in range(1,n):
                for sum_ in range(k+1):
                    notpick=dp[index-1][sum_]
                    pick=0
                    if num[index]<=sum_:
                        pick=dp[index-1][sum_-num[index]]
                    dp[index][sum_]=(pick+notpick)
            return dp[n-1][k]
        totSum = sum(arr)
        mod=int(1e9+7)
        # Checking for edge cases
        if (totSum - d) < 0 or (totSum - d) % 2:
            return 0
        return findWays(arr, (totSum - d) // 2)
    #DP on Subsequences
    #DP22 - Unbounded Knapsack #Memorization Approach
    #--------------------------------------------
    def unboundedKnapsack(n, W, val, wt):
    #Memorization Approach
        def f(ind,weight_threshold):
            if ind == 0:
                return (weight_threshold // wt[0]) * val[0]
            if dp[ind][weight_threshold] != -1:
                return dp[ind][weight_threshold]
            notTaken = f (ind - 1, weight_threshold)
            taken = -sys.maxsize
            if wt[ind] <= weight_threshold:
                taken = val[ind] + f(ind, weight_threshold - wt[ind])
            dp[ind][weight_threshold] = max(notTaken, taken)
            return dp[ind][weight_threshold]
        dp=[[-1 for i in range(W+1)] for i in range(n)]
        return f(n-1,W)
    #DP22 - Unbounded Knapsack #Tabulation Approach Approach
    #--------------------------------------------
    def unboundedKnapsack(n, W, val, wt):
    #tab Approach
        dp=[[-1 for i in range(W+1)] for i in range(n)]
        for i in range(W+1):
            dp[0][i]=(i // wt[0]) * val[0]
        for index in range(1,n):
            for target in range(W+1):
                notTaken = dp[index-1][target]
                taken = -sys.maxsize
                if wt[index] <= target:
                    taken = val[index] + dp[index][target-wt[index]]
                dp[index][target] = max(notTaken, taken)
        return dp[n-1][W]
    #DP22 - Unbounded Knapsack #Tabulation space Approach
    #--------------------------------------------
    def unboundedKnapsack(n, W, val, wt):
    #space optimi
        prev=[0]*(W+1)
        for i in range(W+1):
            prev[i]=(i // wt[0]) * val[0]
        for index in range(1,n):
            for target in range(W+1):
                notTaken = prev[target]
                taken = -sys.maxsize
                if wt[index] <= target:
                    taken = val[index] +prev[target-wt[index]]
                prev[target] = max(notTaken, taken)
        return prev[W]
    


d=Dynamic_programing()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
ans=d.minFallingPathSum(matrix)
print('ANS',ans)

