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

                

        
s=Slidingwindow()
nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
ans=s.longestOnes(nums,k)
print(ans)


