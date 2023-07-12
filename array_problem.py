import time
import math
class ArrayProblems:
    def largest_element_array(self,arr):
        #sample_io
        #input             output
        #[-2,4,5,1,2]       5
        #[0,2,1,5,10,10]    10
        #[-2,-4,-1,-3,-5,-6] -1

        #if array is empty return mothing
        #current max set it array starting element
        #travese a array
        # when i travese i should compare current value is greater than the max ---> set that current max else the max remains same
        #return largest element array (current max)
        if (len(arr)==0):
            return 
        current_max=arr[0]
        for i in range (0,len(arr),1):
            if(arr[i]>current_max):
                current_max=arr[i]
        return current_max 
    def second_largest_element_array(self,arr):
        #sample_io
        #input             output
        #[2,-2,5,7,8,1,10,9]  9
        #[-1,-4,-6,-2,-9,-10] -2
        #[10,10,2,1,5,6]      6

        #if there is no second max in array we should the second max(-1)
        #current max set it array starting element ,second max(-1)
        #travese a array (starting from 1st index to end)
        # when i travese i should compare current value is greater than the max ---> set that current max ,secondary max will be current max  else the 
        # current max remains the same, secondary max need to be checked with current element
        #return second largest element array (second current max)
        if (len(arr)<=1):
            return 
        current_max=arr[0]
        second_max=-1

        for i in range (1,len(arr),1):
            if(arr[i]>current_max):
                second_max=current_max
                current_max=arr[i]
            else:
                if(arr[i]>second_max and arr[i]!=current_max):
                    second_max=arr[i]
        return second_max
    def is_sorted(self,arr):
        if(len(arr)<=1):
            return True  
        p=0
        n=len(arr)
        lastelement=n-1
        for i in range (1,len(arr),1):
            if(arr[i]<arr[i-1]):
                p=i 
                break
        if(p==0):
            return True
        while(n>1):
            if(p==(lastelement)):
                if(arr[p]>arr[0]):
                    return False 
                p=0
            else:
                if(arr[p]>arr[p+1]):
                    return False
                p+=1
            n-=1
        return True
    def remove_duplicate(self,arr):
        #sample_io
        #input             output
        #[1 1 2 5 6 6 7]   [ 1 2 5 6 7 6 7] -5
        #[-1 -1 2 4 4]     [-1  2 4] -3
        # 2 pointers ( i will be starting from 0 to n-1)( j will be starting from i+1 to n-1)
        # if empty return 0. if size is 1 i should be return 1
        # traverse a array check the arr[i] starting element has a duplicate comparing with A[j] --increment j to find the non indentical element for arr[i]
        # then swap with the arr[i+1] element with the non indentical element- once j reach the length of array will not hold duplicate element till i+1 index
        if(len(arr)==1):
            return 1
        if(len(arr)==0):
            return 0
        first=0
        second=first+1
        while(second<len(arr)):
            while(second<len(arr) and arr[first]==arr[second]):
                second+=1
            if(first+1<len(arr) and second<len(arr)):
                arr[first+1]=arr[second]
                first+=1
        return first+1
    
    def rotate_array(self,arr,k):
        #sample_io
        #input             output
        #[4,5,6,1,2,4] k=3     [1,2,4,4,5,6]
        #[1,2,3,4] k=12        [1,2,3,4]
        #[8] k=4              [8]
        k=k%(len(arr))
        if(k==0):
            return arr
        print(k)
        arr=self.reverse(arr,0,k)
        print(arr)
        arr=self.reverse(arr,k+1,len(arr)-1)
        print(arr)
        arr=self.reverse(arr,0,len(arr)-1)
        print(arr)
        return arr
    def reverse(self,arr,start,end):
        if(len(arr)<=1 or start==end):
            return arr
        while(start<end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
        return arr
    def zero_to_end(sef,arr):
        #sample_io
        #input             output
        #[2,4,0,2,0,5,0]     [2,4,2,4,5,0,0,0]
        #[0,2,3,0] k=12        [2,3,0,0,]
        #[8] k=4              [8]
        #check the current 2 pointes starting with index 
        # check current 1 is not zero---> (check current 2 is not zero increment current2 ) out increment current 2
        # if its zero check the current 2 is not zero then swap it.. till u reach a value for current 2 incerment it to swap with i
        n=len(arr)-1
        if(n<1):
            return arr
        start=0
        next1=0
        while(next1<=n):
            if(arr[start]!=0):
                if(arr[next1]!=0):
                    next1+=1
                start+=1
            else:
                if(arr[next1]!=0):
                    temp=arr[start]
                    arr[start]=arr[next1]
                    arr[next1]=temp
                else:
                    next1+=1
        return arr
       
    def liner_serach(self,arr,k):
        n=len(arr)-1
        if(k>arr[n]):
            return -1           
        if(arr[0]==k):
            return 1
        for i in range(0,n+1,1):
            if(arr[i]==k):
                return 1
        return -1
    
    def find_union(self,arr1,n,arr2,m):
        z=[]
        #p1(arr1),p2(arr2) we need to compare which is less whether arr[p1] or arr[p2] 
        #put that in a new array z.. before putting check the element is already present in the z array 
        p1=0
        p2=0
        while(p1<n and p2<m):
            if(arr1[p1]<arr2[p2]):
                #checking if z is not empty and last element of z is current smallest
                if(self.is_value_present(arr1,p1,z)):
                    p1+=1
                else:
                    z.append(arr1[p1])
                    p1+=1
            else:
                if(self.is_value_present(arr2,p2,z)):
                    p2+=1
                else:
                    z.append(arr2[p2])
                    p2+=1 

        while(p1<n):
            if(self.is_value_present(arr1,p1,z)):
                p1+=1
            else:
                z.append(arr1[p1])
                p1+=1
        while(p2<n):
            if(self.is_value_present(arr2,p2,z)):
                p2+=1
            else:
                z.append(arr2[p2])
                p2+=1  
        return z     

    def is_value_present(self,arr,p,z):
        return (len(z)>0 and arr[p]==z[len(z)-1])
    
    def missing_number_brute(self,arr,k):
        #sample_io
        #input             output
        #[1 2 3 4] 5     [3]
        #[5,1]  5            [2,3,4]
        for i in range(1,k+1,1):
            found=False
            for item in arr: 
                if(item!=i): 
                    found=False 
                else:
                    found=True
                    break
            if(found!=True):
                return i
    def missing_number_better(self,arr,k):
        whole=set()
        for item in arr:
            whole.add(item)
        for i in range(1,k+1,1):
            if i not in whole:
                return i
    def missing_number_best(self,arr,k):
        total_sum=(k*(k+1))//2
        for item in arr:
            total_sum=total_sum-item
        return total_sum
    def max_rep_1(self,arr):
        #[0,1,1,1,0,1,1,0,1]     
        len1=0
        old_max=0
        for i in range(0,len(arr),1):
            if(arr[i]==1):
                len1+=1#3
            else:
                if(len1>old_max):
                    old_max=len1 #2
                len1=0
        if(len1>old_max):
          old_max=len1 
        return old_max
    
    def appears_once(self,arr):
        miss=0
        for i in range(0,len(arr),1):
            miss=miss^arr[i]
        return miss
    def len_of_long_subarr(self,arr,k):
        max_len=0 
        for i in range(0,len(arr),1):
            current_len=0
            current_sum=0
            for j in range(i,len(arr),1):
                current_sum+=arr[j]
                if(current_sum==k):
                    current_len=(j-i)+1
                    if(current_len>max_len):
                        max_len=current_len               
        return max_len
    #10,5,2,7,1,9  - k=10
    def len_of_long_subarr_better(self,arr,k):
        current_prefix_sum=0
        max_len=0
        pre_sum={}
        for i in range(0,len(arr),1):
            current_prefix_sum+=arr[i]
            if(current_prefix_sum==k):
                current_len=i+1
                if(current_len>max_len):
                    max_len=current_len
            to_search=current_prefix_sum-k
            if to_search in pre_sum:
                current_len=i-pre_sum[to_search]
                if(current_len>max_len):
                    max_len=current_len
            if current_prefix_sum not in pre_sum:
                pre_sum[current_prefix_sum]=i
        return  max_len  

    def required_sum_pairs(self,a,n,b,m,k):
        #sort first array since the requirment is (u1,v1) ,(u2,v2) u1<u2  
        #once its sorted put the second array in set ..
        #using while loop traverse array till n subtract first i element with the sum and check that remaning is avalible in set
        #if i that the case append it into a list with the arr[i], the sum
        i=0
        required_pair=[]
        s_a=sorted(a)
        b2=set()
        for j in b:
            b2.add(j)
        while(i<len(a)):
            to_search=k-s_a[i]
            if to_search in b2:
                required_pair.append([s_a[i],to_search])
            i+=1
        return required_pair
    
    def two_sum(self,a,n,k):
        #sort first array since the requirment is (u1,v1) ,(u2,v2) u1<u2  
        #once its sorted put the second array in set ..
        #using while loop traverse array till n subtract first i element with the sum and check that remaning is avalible in set
        #if i that the case append it into a list with the arr[i], the sum
        i=0
        b1=dict()
        for j in range(0,len(a),1):
            b1[a[j]]=j  
        while(i<len(a)):
            to_search=k-a[i] # 4
            if to_search in b1 and  b1[to_search]!=i:
                return [i,b1[to_search]]
            i+=1
    def sort012(self,arr,n):
        c_0=0
        c_1=0
        c_2=0
        for item in arr:
            if(item==0):
                c_0+=1
            if(item==1):
                c_1+=1
            if(item==2):
                c_2+=1
        for i in range(0,c_0,1):
            arr[i]=0
        for i in range(c_0,c_1+c_0,1):
            arr[i]=1
        for i in range(c_1+c_0,len(arr),1):
            arr[i]=2
        return arr
    
    def majority_element(self, arr):
        d=dict()
        for i in range(0,len(arr),1):
            key=arr[i]
            if key in d:
                d[key]+=1
            else:
                d[key]=1
        for key,value in d.items():
            if(value>len(arr)//2):
                return key  
        return -1
    
    def moore_voting_algorithm(self,arr):
        #majority's Algorithm,
        element=arr[0] #2
        count=1
        for i in range(1,len(arr),1):
            if(count==0):
                element=arr[i]
            if(arr[i]==element): #3==2  count=0
                count+=1
            else:
                count-=1
                       
        return element


    def majority_element_best(self, arr):
        required_v=self.moore_voting_algorithm(arr)
        count=0

        for i in range(0,len(arr),1):
            if(arr[i]==required_v):
                count+=1
        if(count>len(arr)//2):
            return required_v
        else:
            return -1
        

    def max_sub_array_sum(self,arr):
        sum=0
        start=0
        end=0
        z=[]
        for i in range(0,len(arr),1):
            for j in range(i,len(arr),1):
                sum2=0
                for k in range(i,j+1,1):
                    sum2+=arr[k]
                if(sum2>sum):
                    sum=sum2
                    start=i
                    end=j 
        if(start==end):
            return z       
        for i in range(start,end+1,1):
            z.append(arr[i])            
        return z
    
    def max_sub_array_opt(self,arr):
        #Kadane's Algorithm
        sum=0
        max_sum=arr[0]
        neg_present=False
        for i in range(0,len(arr),1):
            if(arr[i]<0):
                neg_present=True
                if(arr[i]>max_sum):
                    max_sum=arr[i]
            else:
                neg_present=False
                break
        if(neg_present==True):
            return max_sum
        else:
            max_sum=arr[0] 

        for i in range(0,len(arr),1):
            sum+=arr[i]
            if(sum<0):
                sum=0
            if(sum>max_sum):
                max_sum=sum
        return max_sum
    
    def pair_with_max_Sum_brute(self, arr):
        max_sub=0
        for i in range(0,len(arr),1):
            for j in range(i+1,len(arr),1):
                result=self.find_smallest_and_secondsmallest(arr,i,j)
                if(result>max_sub):
                    max_sub=result
        return max_sub 

    def find_smallest_and_secondsmallest(self,arr,i,j):
        small=arr[i]
        second_small=math.inf
        for k in range(i,j+1,1):
            if(arr[k]<small):
                second_small=small
                small=arr[k]
            if(arr[k]<second_small and arr[k]!=small):
                second_small=arr[k]
        if(second_small==math.inf):
            second_small=small
        return small+second_small
    
    def pair_with_max_Sum_better(self,arr):
        max=-math.inf
        for i in range(0,len(arr)-1,1):
            sum=arr[i]+arr[i+1]
            if(sum>max):
                max=sum
        return max
 #7 ,1, 5, 3 ,6   
    def stockBuyAndSell_2(self,prices):
        profit=0
        for i in range(0,len(prices)-1,1):
            if(prices[i]<prices[i+1]):
                profit+=prices[i+1]-prices[i]
        return profit
    
    def rearrange(self,arr):
        print("   ",arr[1:])
        pos=[]
        neg=[]
        for i in range(0,len(arr),1):
            if(arr[i]<0):
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        pos_len=len(pos)
        neg_len=len(neg)
        point=0
        neg_point=0
        pos_point=0
        while(point<len(arr)):
            if(point%2==0 and pos_len!=0 and  neg_len!=0):
                arr[point]=pos[pos_point]
                pos_point+=1
                pos_len-=1
                point+=1
            else:
                if(point%2==1 and pos_len!=0 and  neg_len!=0):
                    arr[point]=neg[neg_point]
                    neg_point+=1
                    neg_len-=1
                    point+=1
            
            if(pos_len==0 or neg_len==0 ):
                break
            

        while (pos_len>0):
            arr[point]=pos[pos_point]
            pos_point+=1
            pos_len-=1
            point+=1

        while (neg_len>0):
            arr[point]=neg[neg_point]
            neg_point+=1
            neg_len-=1
            point+=1
        return arr 
    
    def leaders(self, arr):
        lead=[]
        k=len(arr)-1
        if(len(arr)==1):
            return arr
        lead.append(arr[k])
        current_max=arr[k]
        for i in range (k-1,-1,-1):
            if(current_max<=arr[i]):
                lead.append(arr[i])
                current_max=arr[i]
        return lead[::-1]
    
    def longestSuccessiveElements_brute(self,arr):
        start=0
        current_max=1
        max1=1
        n=0
        k=0
        for i in range(0,len(arr),1):
            f=arr[i]
            if(current_max > max1):
                max1=current_max 
                current_max=1 
            current_max=1
            while(self.find(arr,f+1)==0):
                f+=1
                current_max+=1  
        if(current_max > max1):
            max1=current_max 
            current_max=1    
        return max1
    
    def find(self,arr,f):
        for i in range(0,len(arr),1):
            if(arr[i]==f):
                return 0
        return 1
    

    def longestSuccessiveElements_better(self,arr):
        max1=1
        current_max=1
        prev_element=1
        arr1=sorted(arr)
        if(len(arr)==1):
          return 1
        if(len(arr)==0):
          return 0
        for i in range(0,len(arr1),1):
            if(arr1[i]-1==prev_element):
                current_max+=1
                prev_element=arr1[i]
            else:
                if(arr1[i]!=prev_element):
                    if(current_max > max1):
                        max1=current_max   
                    current_max=1
                    prev_element=arr1[i]
        if(current_max > max1):
            max1=current_max   
        return max1
    
    def longestSuccessiveElements_optimal(self,arr):
        # make a set a with a given elements
        # traverse set elements.
        # check the element is starting point if( starting point then find the consective range)
        #else ignore find the max consective range
        max1=0
        unique_elements=set()
        for item in arr:
            unique_elements.add(item)
        
        for key in unique_elements:
            if key-1 not in unique_elements:
                count=self.find_consecutive_numberofelements(key,unique_elements)
                if(count>max1):
                    max1=count
        return max1

    def find_consecutive_numberofelements(self,start,unique_elements):
        #1 2 3 start 1
        count=0
        while (start in unique_elements):
            count+=1
            start+=1
        return count 


    def setZeroes(self, arr):
        ROWS=len(arr)
        COLS=len(arr[0])
        rows_toconvert=set()
        cols_toconvert=set()
        for i in range(0,ROWS,1):
            for j in range(0,COLS,1):
                if(arr[i][j]==0):
                    rows_toconvert.add(i)
                    cols_toconvert.add(j)
        for row in range(0,ROWS,1):
            for col in range (0,COLS,1):
                if (row in rows_toconvert ) or (col in cols_toconvert):
                    arr[row][col]=0
        return arr 
    
    def rotate(self, arr):
        ROWS=len(arr)
        COLS=len(arr[0])
        k=[]
        j_start=0
        for i in range(0,ROWS,1):
            for j in range(j_start,COLS,1):
                temp=arr[i][j]
                arr[i][j]=arr[j][i]
                arr[j][i]=temp
            j_start+=1
        for i in range(0,ROWS,1):
          arr=self.reverse_row(arr,i)
        return arr
    def reverse_row(self,arr,i):
        start=0
        end=len(arr[i])-1
        while(start<end):
            temp=arr[i][start]
            arr[i][start]=arr[i][end]
            arr[i][end]=temp
            start+=1
            end-=1
        return arr
    
    def spiralOrder(self, arr):
        left=0
        right=len(arr[0])-1
        bot=len(arr)-1
        top=0
        z=[]
        while(len(z)<(len(arr[0])*len(arr))):
            i=left
            while( i<=right):
                z.append(arr[top][i])
                i+=1
            top+=1
            i=top
            while(i<=bot):
                z.append(arr[i][right])
                i+=1
            right-=1
            i=right
            if(top<=bot):
                while(left<=i):
                    z.append(arr[bot][i])
                    i-=1
                bot-=1
            i=bot
            if(left<=right):
                while(i>=top):
                    z.append(arr[i][left])
                    i-=1
                left+=1
        return z

        


a=ArrayProblems()
arr=[[1, 2 ,3 ,4 ,6 ],[4,5,6,0,2,3],[1,2,0,0,5,6],[-2,1,0,5,9],[0,0,0,0,0],[2],[2,2,1,1,3,3,3],[10,9]]
arr1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr2=[-15 ,30 ,43 ,-18 ,-38, 38 ,36 ,78 ,-22 ,-68, 16 ,39 ,-41 ,-15, 98 ,69 ,-72, -32]
print(a.spiralOrder(arr1))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)

