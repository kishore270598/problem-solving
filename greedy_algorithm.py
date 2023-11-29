class greedy:
    #Assign Cookies
    def findContentChildren(self, g, s):
        g=sorted(g)
        s=sorted(s)
        left=0
        right=0
        while (left <len(g) and right<len(s)):
            if(g[left]<s[right]):
                left+=1
                right+=1
            else:
                right+=1
        return left
    

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x: x.value/x.weight ,reverse=True)
        weight=0
        currentweight=0
        finalvalue=0.0
        remain=0
        
        for i in range(0,len(arr),1):
            if currentweight+arr[i].weight <=W :
                currentweight+=arr[i].weight
                finalvalue+=arr[i].value
            else:
                remain=W-currentweight
                finalvalue+=(arr[i].value /arr[i].weight) *remain
                break
        return finalvalue 
    
    def minCoins(self, coins, M, V):
        right=0
        coins_=sorted(coins,reverse=True)
        res=set()
        current_sum=0
        for i in range(0,len(coins_),1):
            while V>=coins_[i]:
                V-=coins_[i]
                res.add(coins_[i])
        return res
    
    def lemonadeChange(self, bills):
        current_change=0
        if(bills[0]!=5):
            return False
        current_change=5    
        for i in range(1,len(bills),1):
            if(bills[i]==10):
                if(current_change<5):
                    return False
                current_change+=5
            elif(bills[i]==20):
                if(current_change<15):
                    return False
                else:
                    current_change-=10
            else:
                current_change+=5
        return True

    def checkValidString(self, s):
        #we will be holding 2 var 
        # with * possible as left left max and *  as right left min
        left_min=0
        left_max=0
        for c in s:
            if(c=='('):
                left_max+=1
                left_min+=1
            elif(c==')'):
                left_max-=1
                left_min-=1
            else:
                left_max+=1
                left_min-=1
            if(left_max<0):
                return False
            if(left_min<0):
                left_min=0
        return left_min==0
    
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if(numOnes>=k):
            return k
        current_max=0
        while(k>0):
            if(numOnes!=0 and numOnes<k):
                current_max+=numOnes
                k-=1*(numOnes)
                numOnes=0
            elif(numZeros!=0 and k!=0):
                k-=1*(numZeros)
                numZeros=0
            elif(k!=0):
                current_max+=k*(-1)
                k=0
        return current_max
    def maximumMeetings(start, end):
            meetings=[]
            current_meeting=0
            max_meeting=0
            no_meeting=0
            left,right=0,0
            for i in range(0,len(start),1):
                meetings.append((end[i],start[i]))
            meetings=sorted(meetings)
            #current_meeting
            while (left<len(meetings)):
                if(right<len(meetings) and current_meeting<=meetings[right][1]):
                    current_meeting=meetings[right][0]
                    no_meeting+=1
                if(right==len(meetings)):
                    max_meeting=max(max_meeting,no_meeting)
                    no_meeting=0
                    left+=1
                    right=left
                    current_meeting=0
                else:
                    right+=1
            return max_meeting    


class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Train:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    
    def __lt__(self,other): # other (train(arr,dep))
        return self.start <other.start

class Solution1:
    def maxMeetings(self, s, e, n) :
        meet = [meeting(s[i], e[i], i + 1) for i in range(n)]
        sorted(meet, key=lambda x: (x.end, x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1, n):
            if meet[i].start > limit:
                limit = meet[i].end
                answer.append(meet[i].pos)
        print("The order in which the meetings will be performed is ")
        for i in answer:
            print(i, end=" ")


    def canJump(self, nums):
        goal=0
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:# u can able to reach it so greater than
                goal=i # since greedy apporch we are reducing the goal to reach our starting point

        if(goal==0):
            return True # we have reached the starting point
        else:
            return False

    def jump2(self, nums):
        #2 pointers to decide the boundary using sliding window 
        # [ [2],[3(l),1(r)],1,4] 
        # each index holds the value the maximum jump with that we see set the boundary( min ,max) the max is farest
        # we have far var which holds the maximum index it can reach
        #farest value will be the min value to reach the last index in lesser time 
        left=0
        right=0
        res=0

        while right <len(nums)-1:
            farest=0
            for i in range(left ,right+1,1):# looping through the boundary
                farest=max(farest,i+nums[i])
            res+=1
            left+=1 # setting to the boundary 
            right=farest # setting to the boundary
        return res

    def minimumPlatform(self,n,at,dt):
        at.sort()
        dt.sort()
        plat=1
        res=1
        left,right=0,1
        while (left<n and right<n):
            if(at[right]<=dt[left]):
                plat+=1
                right+=1
            elif(at[right]>dt[left]):
                plat-=1
                left+=1
            res=max(res,plat)
        return res

class job:
    def __int__(self,jobid,deadline,profit):
        self.jobid=jobid
        self.deadline=deadline
        self.profit=profit
    


class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
                # we sort in reverse to make a maxmium profit
        # finding the maximum job deadline to make sure we maximum profit doing that slot
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        max_job=Jobs[0].deadline
        for i in range(1, len(Jobs)):
            max_job = max(max_job, Jobs[i].deadline)
        slot=[-1]*(max_job+1)
        countJobs=0
        jobprofit=0
        for i in range(len(Jobs)):# we assign the last date
        #to make sure we complete other jobs before that
            for j in range(Jobs[i].deadline,0,-1):
                if(slot[j]==-1):# if the slot is empty we reduce to less deadline and complete that on time
                    slot[j]=i
                    countJobs+=1
                    jobprofit+=Jobs[i].profit
                    break
        return countJobs,jobprofit
    
    def candy(self, ratings: List[int]) -> int:
        #intuition  
        # when a element [ 1,2]  2 IS Greater than 1 so we just add the (candy of 1 ) + for 2 this is left right
        # same we follow left to right to set the candy but we put max since already we have assigned some when going left to right
        arr=[1]*len(ratings)
        for i in range(1,len(ratings),1):
            if ratings[i-1]<ratings[i]:
                arr[i]=ratings[i-1]+1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                arr[i]=max(arr[i],ratings[i+1]+1)
        return sum(arr)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #case 1: where new intervals are lesser than the current intervals-->
        # we return the new interval and plus the intervals
        #case 2 : where the new intervals are overlapping we take the min of the first range and max of of the last range

        res=[] #be the new result 
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:] 
            elif intervals[i][1] <newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
            
        res.append(newInterval)
        return res

        
            


k=Solution()
Jobs = [[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
ans=k.jobScheduling(Jobs,len(Jobs))
print(ans)