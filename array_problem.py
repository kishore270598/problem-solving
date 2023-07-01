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
    



a=ArrayProblems()
arr=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],[4,5,6,1,2,3],[1,2,3,4,5,6],[-2,1,0,5,9],[0,0,0,0,0],[2],[2,2,1,1,3,3,3],[10,9]]
for test in arr:
    start = time.time()
    print('Input',test)
    result=a.rotate_array(test,9944)
    print('Output',result)
    end = time.time()
    print('TIME TAKEN:',(end-start)* 10**3, "ms")
    print('-'*25)

