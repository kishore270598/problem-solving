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
            

    
a=Test()

nums=[1,3,2,3]
target = 2
print(a.countSubarrays(nums, target))



