import time
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



a=ArrayProblems()
arr=[[1, 2 ,3 ,4 ,6 ],[4,5,6,0,2,3],[1,2,0,0,5,6],[-2,1,0,5,9],[0,0,0,0,0],[2],[2,2,1,1,3,3,3],[10,9]]
arr1=[1, 35]
arr2=[1,1,2,2,3,4,4,5,5]
print(a.appears_once(arr2))
# for test in arr:
#     start = time.time()
#     print('Input',test)
#     result=a.find_union(arr1,6,arr2,4)
#     print('Output',result)
#     end = time.time()
#     print('TIME TAKEN:',(end-start)* 10**3, "ms")
#     print('-'*25)

