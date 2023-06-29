n=4
num_line=n*2-1
#i=0
#STARTALP =E
#i=1
#start=D
#i=0 
#min=5
#max=0
#i=1
#min=4
#max=1

for i in range (0,num_line,1):
    numberofmax=i
    numberofmin=num_line-i
    #Printing min
    for j in range (0,numberofmin,1):
        print(n-min(i,j),end=' ')
    #printing max
    for j in range (numberofmin,numberofmin+numberofmax,1):
        print(max(i,j)-(n-2),end=' ')

        
    print('\n')
3 -1
4  -2
5   -3
6   -4


# 3 3 3 3 3. 
# 3 2 2 2. 3 
# 3 2 1. 2 3 
# 3 2. 2 2 3 
# 3. 3 3 3 3