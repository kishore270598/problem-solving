import collections
class Slidingwindow:
    def lengthOfLongestSubstring_brute(self, s):
        max_=0
        if(len(s)==1):
            return 1
        for i in range(0,len(s),1):
            len_=0
            k=s[i]
            dict=list()
            dict.append(k)
            for j in range(i+1,len(s),1):
                if(s[j] not in dict):
                    dict.append(s[j])
                    k+=s[j]
                else:
                    len_=j-i
                    break
            max_=max(len_,max_)
        return max_
    #using 2 pointer (left,right) and a hash map 
    #we traverse the right pointer keeping left as 1 place
    # when we encouter the repeated the charcter we just update the new index in the existing hasmap and jump to that place for left
    # to skip the other checks
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        index_={}
        n=len(s)
        len_=0
        while(right<n):
            if ( ord(s[right]) in index_):#to jump
                left=max(index_[ord(s[right])]+1,left)
            index_[ord(s[right])]=right
            len_=max(len_,right-left+1)
            right+=1
        return len_
    


    def longestOnes(self, nums, k):
        len_=0
        left=0
        right=0
        n=len(nums)
        while(right<n):
            if(nums[right]==0):
                k-=1
            if(k<0):
                if(nums[left]==0):
                    k+=1
                left+=1
            right+=1  
        return right- left
    
    def totalFruit(self, fruits):
        #to store a distinct fruits u need a hashmap
        #left pointer marking 1 each time and right pointer will go from starting to end
        #when we think the count len is greater than 2 that means we out of basket and conditon is failed
        # we reduce the total and reduce the count  and move the left pointer when its empty we pop it
        left,right,total=0,0,0
        n=len(fruits)
        result=0
        count=collections.defaultdict(int)# to store the distinct fruits
        while(right<n):
            count[fruits[right]]+=1
            total+=1
            if (len(count)>2):# i have encountred thrid fruit
                f=fruits[left] #left pointer
                count[f]-=1
                total-=1 # to make sure we maintain the condition
                left+=1
                if count[f]==0:
                    count.pop(f)
            result=max(result,total)   
            right+=1  
        return result
    
    def characterReplacement(self, s, k):
        temp=k
        count={}
        res,left,right=0,0,0
        n=len(s)
        count[s[left]]=0
        while(left <n and right<n):
            if(s[right] in count):
               count[s[right]]+=1
               right+=1
            elif(k>0):
                k-=1
                right+=1
            else:
                k=temp
                res=max(res,count[s[left]]+temp)
                count.pop(s[left])
                if(left+1<n):
                    left+=1
                    right=0
                    count[s[left]]=0
        if(k==0):
            res=max(res,count[s[left]]+temp)
        else:
            res=max(res,count[s[left]]+k)    
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left=0
        maxf=0
        res=0
       #count.get(s[i], 0) gets the current count of the character s[i] from the count dictionary.
       # If the character s[i] is not already a key in the dictionary, count.get(s[i], 0)
       #  returns the default value of 0. 
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            maxf = max(maxf, count[s[right]])

            if  (right - left +1)-maxf > k :# base condition when we see its less it means that is not sliding window we are looking
                # so we reduce the current count of left and move the left pointer
                count[s[left]]-=1
                left+=1
            res=max(res,right -left +1)
        return res
    def numSubarraysWithSum(self, nums, goal):
        left=0
        right=0
        n=len(nums)
        presum=0
        count=0
        while (left <n):
            if(right<n):
                if(presum>goal):
                    left+=1
                    right=left
                    presum=0
                elif(presum<goal):
                    presum+=nums[right]
                    right+=1
                else:
                    count+=1
                    presum+=nums[right]
                    right+=1
            else:
                left+=1
                right=left
                presum=0
        return count
    
    def numSubarraysWithSum(self, nums, goal):
        count=collections.defaultdict(int)
        #to keep a default count[0]=1 which will hold  s--->s(pre sum) -- s-k=0 
        count[0]=1
        presum=0
        ans=0
        for right in nums:
            presum+=right
            ans+=count[presum-goal]
            count[presum]+=1
        return ans


    def numberOfSubarrays(self, nums, k):
        #same as prefix sum 
        # where we add the count for the odd numbers
        # when we see there is a k elements reached in right side we have found one subset which holds k odd numbers
        prefixsum=0
        dic=collections.defaultdict(int)
        dic[0]=1
        ans=0
        for i in nums:
            if i%2==1:
                prefixsum+=1
            ans+=dic[prefixsum-k]
            dic[prefixsum]+=1
        return ans   
    
    def numberOfSubstrings_firstmethod(self, s):
        left,right=0,0
        sub_count=0
        index={}
        while(left<len(s)):
            if(len(index)==3):
                sub_count+=len(s)-(right-left)+1
                left+=1
                right=left
                index.clear()
            else:
                if(right<=len(s)-1):
                    if(s[right] in index): 
                        index[s[right]]=right
                    else:
                        index[s[right]]=right
                else:
                    left+=1
                    right=left
            right+=1
        return sub_count
    
    def numberOfSubstrings(self, s):
        # we take the count of the a b c occurence
        # the base condition is all the count should be greater
        # when that is satsified we find sub_count as ans
        a,b,c=0,0,0
        ans, left, i,n = 0,0, 0, len(s) 
        for left in range(0,n,1):
            if(s[left]=='a'):
                a+=1
            elif(s[left]=='b'):
                b+=1
            else:
                c+=1
            while(a>0 and b>0 and c>0):
                ans += n-left                   # count possible substr, if a substr ends at j, then there are n-j substrs to the right that are containing all a/b/c
                if s[i] == 'a': a -= 1       # decrement counter accordingly
                elif s[i] == 'b': b -= 1
                else: c -= 1
                i += 1                       # move slow pointer
        return ans    

    def maxScore(self, cardPoints, k):
        #sliding window as k elements from the right
        #[[left(11),49,100],right(20),86,29,72]  from right to end we get the total value
        #each time we move right the sliding window, we add the left value inside and remove the right value
        left,right=0,len(cardPoints)-k
        total=sum(cardPoints[right:])
        res=total
        while right<len((cardPoints)):
            total+=(cardPoints[left]-cardPoints[right])
            left+=1
            right+=1
            res=max(res,total)
        return res 

    def kDistinctChars(self,k, str):
        left,right=0,0
        hold={}
        res=0
        #expanding the window
        while(right<len(str)):
            if(str[right] not in hold):
                hold[str[right]]=right# holding the index
                k-=1
            hold[str[right]]=right #already there updating with latest index
            while(k<0):#our base conditon 
                if hold[str[left]]==left: #starting index
                    k+=1
                    del hold[str[left]]
                left+=1
            res=max(right-left+1,res)
            right+=1
        return res
    
    def atmostk(self,n,k,nums):
        left=0
        right=0
        hold=collections.defaultdict(int)
        sub_count=0
        res=0
        while(right<len(nums)):
            hold[nums[right]]+=1
            while len(hold)>k:
                hold[nums[left]]-=1
                if hold[nums[left]]==0:
                    del hold[nums[left]]
                left+=1
            
            res+=right-left+1
            right+=1
        return res
    # If input = 1, 2, 1 and k = 2
    # then, the possible subarrays with atmost k distinct integers:
    # {[1], [2], [1], [1, 2], [2, 1], [1, 2, 1]} i.e. 6.
    # l = 0, r = 0 --> count += r-l+1 = 1
    # l = 0, r = 1 --> count += r-l+1 = 2
    # l = 0, r = 1 --> count += r-l+1 = 3
    # total to 6.
    # Similarly, whwn we do this keeping k-1, we get count = 3
    # We get the difference = 6-3 = 3.
    # Resultant array - {[1, 2], [2, 1], [1, 2, 1]}  

    def subarraysWithKDistinct(self, nums, k):
        return self.atmostk(len(nums),k,nums)-self.atmostk(len(nums),k-1,nums)

    def minWindow(self, s, t):
        #edge case
        if t=="":
            return ""
        countT,countWindow={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have,need=0,len(countT)
        res,result=[-1,-1],float('infinity')
        left=0
        for right in range(0,len(s),1):
            c=s[right]
            countWindow[c]=1+countWindow.get(c,0)
            if ((c in countT ) and countWindow[c]==countT[c]):
                have+=1
            while have==need:
                #update the result finding the min
                if( right -left +1 ) <result:
                    res=[right,left]
                    result=right -left +1
                #pop the left window 
                countWindow[s[left]]-=1
                #if the removed element is one of the T character and the countwindow is less the required
                if (s[left] in countT ) and countWindow[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        right,left=res
        return s[left:right+1] if result!=float('infinity') else ""
    
    def minWindow(S, T):
        # Initially our window is empty
        window = ""
        j = 0
        min_ = len(S) + 1
        i = 0
        while i < len(S):
            # If characters are same, then increment the j pointer
            if S[i] == T[j]:
                j = j + 1
                #  If we finally reach the end of string T, we can start shrinking our window
                if j == len(T):
                    end = i
                    j = j - 1
                    # We are doing j-- in order to minimise our window size
                    while j >= 0:
                        if S[i] == T[j]:
                            j = j - 1
                        i = i - 1
                    # Incrementing i and j for next iteration
                    j = j + 1
                    i = i + 1
                    # Updating our window, if we found an element of minimum length
                    if end - i < min_:
                        # updating minimum
                        min_ = end - i
                        # updating window
                        window = ""
                        for k in range(i, end + 1):
                            window += S[k]
            i += 1
        # returning our final answer, which is stored in window
        return window

            



s=Slidingwindow()
nums = [1,2,1,3,4]
nums="ADOBECODEBANC"
k="ABC"
ans=s.minWindow(nums,k)
print(ans)


