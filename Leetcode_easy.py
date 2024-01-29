from collections import defaultdict
class Test:
    def plusOne(self):
        digits=[9]
        val=10
        val=val**(len(digits)-1)
        sums=0
        i=0
        while(val>=1):
            sums+=val*digits[i]
            val=val//10
            i+=1
        if(digits[i-1]==9):
            k=i+1
        else:
            k=i
        sums=sums+1
        z=[]
        val=10
        val=val**(k-1)
        string = str(sums)
        for i in string:
            z.append(int(i))
        print(z)
    
    
    def getRow(self, rowIndex):
        z=[]
        i=0
        while(i<rowIndex):
            value=self.ncr(rowIndex,i)
            z.append(value)
            i+=1
        z.append(1)
        return z

    def ncr(self,k,r):
        return self.fact(k)//(self.fact(r) * self.fact(k-r))
    
    def fact(self,k):
        if k==0:
            return 1
        val=1
        for i in range (2,k+1,1):
            val*=i
        return val
    
            #coins = [1,4,10], target = 19

    #2952. Minimum Number of Coins to be Added
    def minimumAddedCoins(self,nums,target):
        ans=[]
        subset=[]
        sum_=set()  

        def findPowerSet(index):
            if index>=len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[index])
            findPowerSet(index+1)
            subset.pop()
            findPowerSet(index+1)
        #check the sum of subseq
        def findthesum(ans):
            for i in range(len(ans)):
                sum_.add(sum(ans[i]))
            sum_.remove(0)

        findPowerSet(0)
        findthesum(ans)
        coins_add=0
        for i in range(1,target+1,1):
            if i not in sum_:
                nums.append(i)
                coins_add+=1
                ans=[]
                subset=[]
                #check every time 
                findPowerSet(0)
                findthesum(ans)
                if(len(sum_)>=target):
                    break
        return coins_add
    def minimumAddedCoins(self,nums,target):
                nums.sort()
                coins_count=0
                current_sum=0
                index=0
                while current_sum<target:
                    if len(nums)>index and nums[index]<=current_sum+1:
                        current_sum+=nums[index]
                        index+=1
                    else:
                        current_sum+=current_sum+1
                        coins_count+=1
                return coins_count   
    def totalMoney(self, n: int) -> int:
        flag=1
        main_flag=1
        sum_=0
        k=1
        while(k<n+1):
            if(k%7==0):
                print(flag,'+')
                sum_+=flag
                flag=main_flag+1
                main_flag+=1

            else:
                print(flag,'+')
                sum_+=flag
                flag+=1
            k+=1
        return sum_
    #0 <= i < variables.length
    #((aibi % 10)ci) % mi == target

    def getGoodIndices(self, variables, target):
        res_index=[]
        for i in range(len(variables)):
                term1=((variables[i][0])**variables[i][1])%10
                term2=term1**variables[i][2]
                if (term2%variables[i][3]==target):
                    res_index.append(i)
        return res_index

    def countSubarrays(self, nums, k):
        n = len(nums)
        maxi = max(nums)
        i, j, cnt, ans = 0, 0, 0, 0
        while j < n:
            if nums[j] == maxi:
                cnt += 1
            if cnt >= k:
                while cnt >= k:
                    ans += n - j
                    if nums[i] == maxi:
                        cnt -= 1
                    i += 1
                    
            j += 1

        return ans
       
    def divideArray(self, nums, k):
        main_array=sorted(nums)
        ans=[]
        if len(nums)%3!=0:
                return ans
        required_sub=len(nums)//3
        left=0
        right=0
        flag=0
        sub_array=0
        temp=[]
        while left<=len(nums)-2 and right<=len(nums)-1:
                if abs(main_array[left]-main_array[right])<=k:
                        flag+=1
                        temp.append(main_array[right])
                right+=1
                if(flag%3==0):
                        sub_array+=1
                        ans.append(temp)
                        left=right
                        right=left
                        flag=0
                        temp=[]
        if (required_sub==sub_array):
                return ans
        else:
                return []
        
    def minimumCost(self, nums):
        min_=min(nums)
        max_=max(nums)
        min_cost_val=0
        min_cost=0

        def palindrome(x):
            rev =x
            sum = 0
            if x%10==0 or x<0:
                return False
            while rev > 0:
                r = rev % 10
                sum = sum * 10 + r
                rev = rev // 10
            if sum == x:
                return True
            
        for i in range(min_,max_+1,1):
             if palindrome(i):
                min_cost_val=i
                break
        for element in nums:
             min_cost+=abs(min_cost_val-element)
        return min_cost
    


    
    def halvesAreAlike(self, s):
        left=0
        right=len(s)-1
        l=0
        r=0
        while (left<right):
            if s[left].isalpha()==True:
                print(s[left])
                l+=1
            if s[right].isalpha()==True:
                r+=1
            left+=1
            right-=1
        print(r,l)
        if l==r:
            return True
        return False

    def beautifulIndices(self, s, a, b, k):
                        len_a=len(a)
                        len_b=len(b)
                        def check_string(str1,str2):
                                return str1==str2
                        res_a=[]
                        for i in range(0,len(s),1):
                                da=(len_a)
                                if da+i<=len(s):
                                        if(check_string(s[i:da+i],a)):
                                                res_a.append(i)
                        res_b=[]
                        for i in range(0,len(s),1):
                                db=len_b
                                if db+i<=len(s):
                                        if(check_string(s[i:db+i],b)):
                                                res_b.append(i)
                        res_a=sorted(res_a)
                        res_b=sorted(res_b)
                        ans=[]
                        for i in res_a:
                                for j in res_b:
                                # Check if substrings match and absolute difference <= k
                                    if abs(i - j) <= k:
                                        ans.append(i)
                                        break
                                
                                
                                
                                
                        # for element in ans:
                        #         z.append(element)
                        # z=sorted(z)
                        return ans           
    #contest 3019. Number of Changing Keys                                 
    def countKeyChanges(self, s):
                flag=0
                for i in range(0,len(s)-1,1):
                        if ord(s[i])+32!=ord(s[i+1]) and ord(s[i])!=ord(s[i+1])+32 and s[i]!=s[i+1]:
                                flag+=1
                return flag
    #contest 3020. Find the Maximum Number of Elements in Subset
    def maximumLength(self, nums):
                maxcount = 1
                freq=dict()
                for num in nums:
                        if num in freq:
                                freq[num] += 1
                        else:
                                freq[num] = 1

                # for every unique element in the array
                for x in freq.keys():
                        # we need atleast 2 x in array so there's no point checking further for x^2
                        if freq[x] == 1:
                                continue
                        if x == 1:
                                # special case
                                count = freq[x] if freq[x]%2 else freq[x]-1
                        else:
                                # set to 2 as we have already use current x
                                count = 2
                                p = x
                                while True:
                                        p*=p
                                        if p in freq:
                                                if freq[p]==1:
                                                        count+=1
                                                        break
                                                else:# use 2 p for left sub-subset and right
                                                        count+=2
                                        else:
                                                count-=1
                                                break
                        maxcount=max(maxcount,count)
                return maxcount
    #contest 3021. Alice and Bob Playing Flower Game
    def flowerGame(self, n, m):
                #Intuition 
                #To win alice  we need make sure that alice has more than the bob so odd counts
                #left ( anticlock (odd M)* EVEN N) + (CLOCK  (odd N)* even(m))
                even_count_n=0
                even_count_m=0
                odd_count_n=0
                odd_count_m=0
                for i in range(m):
                        if i%2==0:
                                even_count_m+=1
                        else:
                                odd_count_m+=1
                for i in range(n):
                        if i%2==0:
                                even_count_n+=1
                        else:
                                odd_count_n+=1

                return (even_count_n*odd_count_m)+(odd_count_n*even_count_m)
    def shortest_distance(self, matrix):
	    #Floyd Warshall
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=float('inf')
            
                if (i==j):
                    matrix[i][j]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(m):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
	        
	               
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=-1

        return matrix

    def findTheCity(self, n, edges, distanceThreshold):
        #Floyd Warshall
        cost=[]
        adj=defaultdict(list)
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(float('inf'))
            cost.append(temp)
        for start,end,distance in edges:
            cost[start][end]=distance
            cost[end][start]=distance
            cost[end][end]=0
            cost[start][start]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
        d=defaultdict()
        for i in range(n):
            c=0
            for j in range(n):
                if cost[i][j]<=distanceThreshold and i!=j:
                    c+=1
            d[i]=c
        m1=min(d.values())
        m2=0
        for k,v in d.items():
            if m1==v:
                m2=max(m2,k)
        return m2

    
a=Test()
nums=[10,12,13,14,15]
s="aAbBcC"
a="my"
b="squirrel"
k=15
print(a.countKeyChanges(s))



