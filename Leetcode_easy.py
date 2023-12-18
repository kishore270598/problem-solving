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
    
    def widthOfBinaryTree(self, root):
        #we need to index the each node
        # with the formula left(2*i +1) and right(2*i+2)
        #to overflow stack issue we take the min of the first element and sub then we find the left and right index
        # in a dict set you will hold a maximum and minum of the level ( we need to do  a level order traversal)
        dict_=dict()
        self.max_diff = 0
        def level_order(root,index_,level,dict_):
            if root is None:
                return None
            dict_.setdefault(level, [index_, index_])
            #min
            dict_[level][0]=min(dict_[level][0],index_)
            #max
            dict_[level][1]=max(dict_[level][1],index_)
            self.max_diff=max(self.max_diff,dict_[level][1]-dict_[level][0])
            level_order(root.right,2*index_,level+1,dict_)
            level_order(root.left,2*index_+1,level+1,dict_)
            

        level_order(root,0,0,dict_)
        return self.max_diff+1
             



            
a=Test()

nums=[10,12,13,14,15]
k=3
print(a.minimumCost(nums))



