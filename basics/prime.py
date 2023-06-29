class Solution:
    def findmax(self,arr):
        #(2,5)(3,7)
        currentmax=0
        currentmaxindex=0
        for i in range (0,len(arr),1):
            item=arr[i] #(2,5)
            sped=item[1] # 5
            index=item[0] # 2 
            if(currentmax<sped):
                currentmax=sped
                currentmaxindex=index
        return [currentmaxindex,currentmax]
        
    def minJumps(self, arr, n):
        #possible km for each index
        count=0
        index_possiblekm=[]
        for i in range(0,n,1):
            index_possiblekm.append((i,arr[i]+i))
        print(index_possiblekm)
        #finding route
        current=0 #current=1
        goal=n-1    #
        while (current<=goal):
            possible_end_position=index_possiblekm[current][1] #--4
            #friends_end_dis
            a=index_possiblekm[current+1:possible_end_position+1] #(1,4) #count =1
            frndsmax=self.findmax(a)
            if(goal<=possible_end_position):
                return count
            else:
                current=frndsmax[0]
                count+=1



            
arr= [1,3,5,3,2,2,6,7,6,8,9,1,2,3,4]
n = len(arr)
#arr=[1,4,7,6,7,8...]
s=Solution()
print(s.minJumps(arr,n))

