class Solution {
    public int findNumbers(int[] nums) 
    {int num1=0;
     int count=0;
     int n=nums.length;
     for (int i=0;i<n;i++)
     {
         while (nums[i] < 0)
       {  nums[i]=nums[i]/10;
          count++;
        r 
             
         }
     }   
         
     System.out.println(count);
     
     
        
    } return count;
}